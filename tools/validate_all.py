#!/usr/bin/env python3
"""Validate every place record against data/schema/place.schema.json (stdlib only).

Checks:
  * data/places/*.json  (one enriched place per file)
  * data/seed/places.json (array of seed places)

Schema keywords supported: $ref (to #/...), type (single or list), enum,
required, properties, additionalProperties (false), items, minItems,
uniqueItems, pattern, minLength, minimum, maximum, format=uri.
Any other keyword found in the schema is reported, so the validator cannot
silently skip a rule that a future schema edit introduces.

Dataset rules (errors):
  * ids unique within each dataset; enriched file name == "<id>.json"
Editorial rules for enriched files (errors):
  * every localized field that has `en` text also has `ar` text
  * every highlight has non-empty title and desc in both languages
  * at least one photo
Schema v1.1 rules (errors, enriched and seed):
  * prices.status "unconfirmed" -> no tiers, extras or freeGroups
  * prices.status "free" -> every tier amount is 0
  * prices.status "confirmed" (or absent) with a prices object -> at least one tier
  * onlineAmount (tiers and extras) differs from amount
  * no duplicate (audience, group) tier
  * hours exceptions: from <= to; a Ramadan exception (rule starts "Ramadan") has from and to
  * a dayHours entry with open and close has open < close (split sessions use separate entries)

Exit code 0 when there are no errors. Usage: python3 tools/validate_all.py [-q]
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "data/schema/place.schema.json"
PLACES = ROOT / "data/places"
SEED = ROOT / "data/seed/places.json"

SUPPORTED = {
    "$ref", "type", "enum", "required", "properties", "additionalProperties", "items",
    "minItems", "uniqueItems", "pattern", "minLength", "minimum", "maximum", "format",
    # annotations (no validation effect)
    "$schema", "$id", "$comment", "$defs", "title", "description",
}
TYPES = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}
URI = re.compile(r"^https?://[^\s/$.?#][^\s]*$")


def schema_keyword_audit(node, path="#"):
    """Return keywords in the schema that this validator does not implement."""
    bad = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k not in SUPPORTED:
                bad.append(f"{path}/{k}")
            if k in ("properties", "$defs"):
                for name, sub in v.items():
                    bad += schema_keyword_audit(sub, f"{path}/{k}/{name}")
            elif k in ("items",) or (k == "additionalProperties" and isinstance(v, dict)):
                bad += schema_keyword_audit(v, f"{path}/{k}")
    return bad


def is_type(v, t):
    if t == "integer":
        return isinstance(v, int) and not isinstance(v, bool)
    if t == "number":
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    return isinstance(v, TYPES[t])


def resolve(root, ref):
    if not ref.startswith("#/"):
        raise ValueError(f"unsupported $ref {ref}")
    node = root
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def check(v, s, root, path, errs):
    if "$ref" in s:
        check(v, resolve(root, s["$ref"]), root, path, errs)
        # sibling keywords next to $ref (e.g. description) are annotations only
        return
    if "type" in s:
        ts = s["type"] if isinstance(s["type"], list) else [s["type"]]
        if not any(is_type(v, t) for t in ts):
            errs.append(f"{path}: expected {'/'.join(ts)}, got {type(v).__name__}")
            return
    if "enum" in s and v not in s["enum"]:
        errs.append(f"{path}: {v!r} not in enum")
    if isinstance(v, str):
        if "minLength" in s and len(v) < s["minLength"]:
            errs.append(f"{path}: shorter than {s['minLength']}")
        if "pattern" in s and not re.search(s["pattern"], v):
            errs.append(f"{path}: {v!r} does not match {s['pattern']}")
        if s.get("format") == "uri" and not URI.match(v):
            errs.append(f"{path}: {v!r} is not an http(s) URI")
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        if "minimum" in s and v < s["minimum"]:
            errs.append(f"{path}: {v} < minimum {s['minimum']}")
        if "maximum" in s and v > s["maximum"]:
            errs.append(f"{path}: {v} > maximum {s['maximum']}")
    if isinstance(v, dict):
        for r in s.get("required", []):
            if r not in v:
                errs.append(f"{path}: missing required '{r}'")
        props = s.get("properties", {})
        addl = s.get("additionalProperties", True)
        for k, x in v.items():
            if k in props:
                check(x, props[k], root, f"{path}.{k}", errs)
            elif addl is False:
                errs.append(f"{path}: unexpected property '{k}'")
            elif isinstance(addl, dict):
                check(x, addl, root, f"{path}.{k}", errs)
    if isinstance(v, list):
        if "minItems" in s and len(v) < s["minItems"]:
            errs.append(f"{path}: fewer than {s['minItems']} items")
        if s.get("uniqueItems"):
            dumped = [json.dumps(x, sort_keys=True) for x in v]
            if len(set(dumped)) != len(dumped):
                errs.append(f"{path}: items not unique")
        if "items" in s:
            for i, x in enumerate(v):
                check(x, s["items"], root, f"{path}[{i}]", errs)


def localized_gaps(v, path, out):
    """Find {en: text, ar: null/empty} pairs anywhere in a record."""
    if isinstance(v, dict):
        if set(v) <= {"ar", "en"} and "en" in v:
            if isinstance(v.get("en"), str) and v["en"].strip() and not (isinstance(v.get("ar"), str) and v["ar"].strip()):
                out.append(f"{path}: Arabic missing")
            return
        for k, x in v.items():
            if k not in ("sources", "curationNote"):
                localized_gaps(x, f"{path}.{k}", out)
    elif isinstance(v, list):
        for i, x in enumerate(v):
            localized_gaps(x, f"{path}[{i}]", out)


def v11_rules(rec, path):
    """Cross-field rules for the schema v1.1 additions (prices.status, onlineAmount, dated exceptions)."""
    errs = []
    p = rec.get("prices")
    if isinstance(p, dict):
        status = p.get("status", "confirmed")
        tiers = p.get("tiers") or []
        if status == "unconfirmed":
            for k in ("tiers", "extras", "freeGroups"):
                if p.get(k):
                    errs.append(f"{path}.prices: status 'unconfirmed' must not carry {k}")
        elif status == "free":
            if any(isinstance(t, dict) and t.get("amount") for t in tiers):
                errs.append(f"{path}.prices: status 'free' but a tier has a non-zero amount")
        elif not tiers:
            errs.append(f"{path}.prices: status 'confirmed' needs at least one tier (use 'unconfirmed' or 'free')")
        seen = set()
        for i, t in enumerate(tiers):
            if not isinstance(t, dict):
                continue
            key = (t.get("audience"), t.get("group"))
            if key in seen:
                errs.append(f"{path}.prices.tiers[{i}]: duplicate tier {key}")
            seen.add(key)
        for kind in ("tiers", "extras"):
            for i, t in enumerate(p.get(kind) or []):
                if isinstance(t, dict) and "onlineAmount" in t and t.get("onlineAmount") == t.get("amount"):
                    errs.append(f"{path}.prices.{kind}[{i}]: onlineAmount equals amount (omit it)")
    hours = rec.get("hours")
    if isinstance(hours, dict):
        def day_rules(days, where):
            for i, d in enumerate(days or []):
                if isinstance(d, dict) and d.get("open") and d.get("close") and d["open"] >= d["close"]:
                    errs.append(f"{where}[{i}]: open {d['open']} is not before close {d['close']}")
        day_rules(hours.get("weekly"), f"{path}.hours.weekly")
        for i, e in enumerate(hours.get("exceptions") or []):
            if not isinstance(e, dict):
                continue
            w = f"{path}.hours.exceptions[{i}]"
            if e.get("from") and e.get("to") and e["from"] > e["to"]:
                errs.append(f"{w}: from {e['from']} is after to {e['to']}")
            if str(e.get("rule", "")).lower().startswith("ramadan") and not (e.get("from") and e.get("to")):
                errs.append(f"{w}: Ramadan exception needs from/to dates")
            day_rules(e.get("weekly"), f"{w}.weekly")
    return errs


def editorial(rec, path):
    errs = []
    localized_gaps(rec, path, errs)
    for i, h in enumerate(rec.get("highlights") or []):
        if not isinstance(h, dict):
            continue  # already reported by the schema check
        for part in ("title", "desc"):
            for lang in ("en", "ar"):
                loc = h.get(part)
                val = loc.get(lang) if isinstance(loc, dict) else None
                if not (isinstance(val, str) and val.strip()):
                    errs.append(f"{path}.highlights[{i}].{part}.{lang}: empty")
    if not rec.get("photos"):
        errs.append(f"{path}.photos: at least one photo required")
    return errs


def main():
    quiet = "-q" in sys.argv
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errors = []
    unsupported = schema_keyword_audit(schema)
    if unsupported:
        errors += [f"schema: keyword not implemented by validator: {k}" for k in unsupported]

    # enriched places
    ids = {}
    files = sorted(PLACES.glob("*.json"))
    for f in files:
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{f.name}: invalid JSON: {e}")
            continue
        errs = []
        check(rec, schema, schema, f.stem, errs)
        if isinstance(rec, dict):
            if rec.get("id") != f.stem:
                errs.append(f"{f.name}: id {rec.get('id')!r} does not match file name")
            if rec.get("id") in ids:
                errs.append(f"{f.name}: duplicate id (also in {ids[rec['id']]})")
            ids[rec.get("id")] = f.name
            errs += editorial(rec, f.stem)
            errs += v11_rules(rec, f.stem)
        errors += errs
        if not quiet:
            print(f"{'ok ' if not errs else 'ERR'} data/places/{f.name}" + (f"  ({len(errs)} errors)" if errs else ""))

    # seed
    seed = json.loads(SEED.read_text(encoding="utf-8"))
    seed_errs = []
    if not isinstance(seed, list):
        seed_errs.append("seed: top level must be an array")
        seed = []
    seen = set()
    for i, rec in enumerate(seed):
        pid = rec.get("id", f"#{i}") if isinstance(rec, dict) else f"#{i}"
        check(rec, schema, schema, f"seed[{pid}]", seed_errs)
        if isinstance(rec, dict):
            seed_errs += v11_rules(rec, f"seed[{pid}]")
        if pid in seen:
            seed_errs.append(f"seed[{pid}]: duplicate id")
        seen.add(pid)
    errors += seed_errs
    if not quiet:
        print(f"{'ok ' if not seed_errs else 'ERR'} data/seed/places.json ({len(seed)} records)" + (f"  ({len(seed_errs)} errors)" if seed_errs else ""))

    for e in errors:
        print("  -", e)
    print(f"\n{len(files)} place files + {len(seed)} seed records checked: {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
