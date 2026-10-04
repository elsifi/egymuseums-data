"""Validate data/seed/places.json against data/schema/place.schema.json.

Uses `jsonschema` if it happens to be installed; otherwise a small stdlib
validator covering the keywords used by the schema (type, enum, required,
properties, additionalProperties, items, minItems, uniqueItems, pattern,
minimum, maximum, minLength, format=uri, $ref to #/$defs). Also checks
dataset-level rules: unique ids, unique wikidataIds, sort order.
"""
import json
import os
import re
import sys

from common import REPO

SCHEMA = os.path.join(REPO, "data", "schema", "place.schema.json")
DATA = os.path.join(REPO, "data", "seed", "places.json")

TYPES = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}


def is_type(v, t):
    if t == "integer":
        return isinstance(v, int) and not isinstance(v, bool)
    if t == "number":
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    return isinstance(v, TYPES[t])


def check(v, s, root, path, errs):
    if "$ref" in s:
        ref = s["$ref"]
        assert ref.startswith("#/")
        node = root
        for part in ref[2:].split("/"):
            node = node[part]
        return check(v, node, root, path, errs)
    if "type" in s:
        ts = s["type"] if isinstance(s["type"], list) else [s["type"]]
        if not any(is_type(v, t) for t in ts):
            errs.append(f"{path}: expected {ts}, got {type(v).__name__}")
            return
    if "enum" in s and v not in s["enum"]:
        errs.append(f"{path}: {v!r} not in enum")
    if isinstance(v, str):
        if "minLength" in s and len(v) < s["minLength"]:
            errs.append(f"{path}: shorter than {s['minLength']}")
        if "pattern" in s and not re.search(s["pattern"], v):
            errs.append(f"{path}: {v!r} does not match {s['pattern']}")
        if s.get("format") == "uri" and not re.match(r"^https?://\S+$", v):
            errs.append(f"{path}: {v!r} is not an http(s) URI")
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        if "minimum" in s and v < s["minimum"]:
            errs.append(f"{path}: {v} < {s['minimum']}")
        if "maximum" in s and v > s["maximum"]:
            errs.append(f"{path}: {v} > {s['maximum']}")
    if isinstance(v, dict):
        for r in s.get("required", []):
            if r not in v:
                errs.append(f"{path}: missing required '{r}'")
        props = s.get("properties", {})
        for k, x in v.items():
            if k in props:
                check(x, props[k], root, f"{path}.{k}", errs)
            elif s.get("additionalProperties") is False:
                errs.append(f"{path}: unexpected property '{k}'")
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


def main():
    schema = json.load(open(SCHEMA, encoding="utf-8"))
    data = json.load(open(DATA, encoding="utf-8"))
    errs = []
    try:
        import jsonschema  # noqa: F401
        v = jsonschema.Draft202012Validator(schema)
        for i, p in enumerate(data):
            for e in v.iter_errors(p):
                errs.append(f"[{i}] {p.get('id')}: {e.message}")
        engine = "jsonschema"
    except ImportError:
        for i, p in enumerate(data):
            check(p, schema, schema, f"[{i}]{p.get('id')}", errs)
        engine = "stdlib"
    ids = [p["id"] for p in data]
    if len(ids) != len(set(ids)):
        errs.append("duplicate ids: " + ", ".join(sorted({i for i in ids if ids.count(i) > 1})))
    q = [p["wikidataId"] for p in data if p.get("wikidataId")]
    if len(q) != len(set(q)):
        errs.append("duplicate wikidataIds: " + ", ".join(sorted({i for i in q if q.count(i) > 1})))
    key = [(p["governorate"], p["name"]["en"].lower()) for p in data]
    if key != sorted(key):
        errs.append("places.json is not sorted by governorate then name.en")
    for e in errs:
        print("ERROR", e)
    print(f"{engine} validation: {len(data)} records, {len(errs)} errors")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
