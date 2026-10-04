"""Build data/seed/places.json from the cached seed sources.

Inputs (run the fetch_* scripts first):
  cache/wikidata.json        identity, labels, coordinates, sitelinks (CC0)
  cache/egymonuments.json    portal page list (URLs/titles only)
  cache/wikipedia_lists.json Wikipedia museum lists (cross-check)
  cache/osm_crosscheck.json  OSM tags-only cross-check (ids only are used)
  sites_curated.json         curated archaeological / heritage sites
  museums_manual.json        museum exclusions, merges, additions, overrides

Output: data/seed/places.json and cache/build_notes.json (used by make_report.py)
"""
import os
import re
import unicodedata

from common import (CACHE, CHECKED_AT, GOVERNORATES, HERE, REPO, load_json,
                    save_json)

WD = "https://www.wikidata.org/wiki/"
EGYM = "https://egymonuments.gov.eg/en/"
MOTA_PDF = "https://mota.gov.eg/media/5a2ja2iu/ticket-english-5-11-2024-1.pdf"
EGYM_SITEMAP = "https://egymonuments.gov.eg/en/sitemap.aspx"

# Tie-break when Wikidata places an item in several governorates (stale admin
# units such as Qena-before-Luxor, or Giza/Cairo river-island ambiguity).
GOV_PRECEDENCE = ["luxor", "cairo"] + [g for g in GOVERNORATES if g not in ("luxor", "cairo")]

NOT_CITY = {"Q79", "Q1144287", "Q1072006"}  # Egypt, Lower Egypt, Upper Egypt


def slugify(text):
    text = re.sub(r"\(.*?\)", "", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    text = re.sub(r"^the-", "", text)
    return text


def pick_gov(govs):
    for g in GOV_PRECEDENCE:
        if g in (govs or []):
            return g
    return None


def osm_id(e):
    if e.get("osmRel"):
        return "relation/" + e["osmRel"]
    if e.get("osmWay"):
        return "way/" + e["osmWay"]
    if e.get("osmNode"):
        return "node/" + e["osmNode"]
    return None


def merged_view(qid, dup_qids, ents):
    """Primary entity with gaps filled from duplicate items."""
    base = dict(ents.get(qid, {})) if qid else {}
    for d in dup_qids:
        e = ents.get(d, {})
        for k, v in e.items():
            if k in ("aliases",):
                continue
            if not base.get(k):
                base[k] = v
    return base


def aliases_for(e, dup_qids, ents, names, extra):
    out = []
    for a in e.get("aliases", []):
        out.append(a["value"])
    for d in dup_qids:
        de = ents.get(d, {})
        for k in ("en", "ar"):
            if de.get(k):
                out.append(de[k])
        out += [a["value"] for a in de.get("aliases", [])]
    for k in ("en", "ar", "mul"):
        if e.get(k):
            out.append(e[k])
    out += extra or []
    seen, res = set(n.strip().lower() for n in names if n), []
    for a in out:
        a = a.strip()
        if a and a.lower() not in seen:
            seen.add(a.lower())
            res.append(a)
    return res[:12]


def city_for(e, gov):
    for a in e.get("admin", []):
        if a["qid"] in NOT_CITY or (a["en"] or "").endswith("Governorate") \
                or a["en"] in ("Lower Egypt", "Upper Egypt", "Egypt"):
            continue
        if a["qid"] in {v[0] for v in GOVERNORATES.values()}:
            continue
        if a["en"] or a["ar"]:
            return {"en": a["en"], "ar": a["ar"]}
    return None


def wiki_links(e):
    return {
        "wikipediaEn": e.get("enwiki"),
        "wikipediaAr": e.get("arwiki"),
    }


def status_from(e):
    misc = e.get("misc", {})
    states = {x[1] for x in misc.get("stateOfUse", []) if x[1]}
    if e.get("dissolved") or e.get("closed") or states & {"out of service", "demolished or destroyed", "closed", "destroyed"}:
        return "closed", "Wikidata records a dissolution/closing date or out-of-use state."
    return "unknown", None


MUSEUM_TYPE_CATEGORY = [
    ("children", "children"), ("art", "modern-art"), ("natural history", "science-natural"),
    ("science", "science-natural"), ("military", "military"), ("police", "military"),
    ("palace", "royal-palace"), ("egyptolog", "pharaonic"), ("archaeolog", "mixed"),
    ("railway", "specialised"), ("postal", "specialised"), ("literary", "specialised"),
    ("historic house", "specialised"), ("medical", "specialised"),
]


def guess_category(e):
    types = " ".join((t[1] or "") for t in e.get("types", [])).lower()
    for key, cat in MUSEUM_TYPE_CATEGORY:
        if key in types:
            return cat
    return "specialised"


def make_record(kind, rid, qid, e, dup_qids, ents, cur, egym_paths, notes, via):
    name_en = cur.get("en") or e.get("en") or e.get("mul") or e.get("other")
    name_ar = cur.get("ar") or e.get("ar") or e.get("arz")
    if not name_en:
        name_en = name_ar
        notes["needsEnglishName"].append(rid)
    gov = cur.get("gov") or pick_gov(e.get("govs"))
    if not gov:
        for d in dup_qids:
            gov = pick_gov(ents.get(d, {}).get("govs"))
            if gov:
                break
    rec = {"id": rid, "kind": kind, "wikidataId": qid,
           "name": {"en": name_en, "ar": name_ar}}
    al = aliases_for(e, dup_qids, ents, [name_en, name_ar], cur.get("aliases"))
    if al:
        rec["aliases"] = al
    rec["category"] = cur.get("category") or guess_category(e)
    rec["operator"] = cur.get("operator") or (
        "mota-sca" if kind == "site" or cur.get("mota") else "unknown")
    rec["governorate"] = gov
    city = None
    if cur.get("city"):
        city = {"en": cur["city"][0], "ar": cur["city"][1]}
    else:
        city = city_for(e, gov)
    if city:
        rec["city"] = city
    coords = e.get("coords") or []
    if coords:
        rec["lat"], rec["lng"] = coords[0]
        if len(coords) > 1:
            notes["multipleCoords"].append({"id": rid, "coords": coords})
    else:
        rec["lat"] = rec["lng"] = None
        notes["missingCoords"].append(rid)
    # closure facts only from the primary item (a merged duplicate may be e.g.
    # the historic city that "ended" centuries ago)
    st, stnote = status_from(ents.get(qid, {}) if qid else {})
    rec["status"] = cur.get("status") or st
    if cur.get("statusNote") or stnote:
        rec["statusNote"] = cur.get("statusNote") or stnote
    links = {"egymonuments": EGYM + egym_paths[0] + "/" if egym_paths else None}
    links.update(wiki_links(e))
    links["osm"] = osm_id(e) or cur.get("osmId")
    rec["links"] = links
    rec["tier"] = cur.get("tier") or "minor"
    src = []
    if qid:
        src.append({"field": "identity,name,coordinates,links", "url": WD + qid, "checkedAt": CHECKED_AT})
        for d in dup_qids:
            src.append({"field": "duplicate-wikidata-item", "url": WD + d, "checkedAt": CHECKED_AT})
    for p in egym_paths or []:
        src.append({"field": "enumeration", "url": EGYM + p + "/", "checkedAt": CHECKED_AT})
    if cur.get("mota"):
        src.append({"field": "enumeration,ticketed", "url": MOTA_PDF, "checkedAt": CHECKED_AT})
    for v in via or []:
        src.append({"field": "enumeration", "url": v, "checkedAt": CHECKED_AT})
    if not src:
        src.append({"field": "enumeration", "url": EGYM_SITEMAP, "checkedAt": CHECKED_AT})
    rec["sources"] = src
    conf = cur.get("confidence")
    if not conf:
        if not qid:
            conf = "low"
        elif rec["lat"] is None or not name_ar or not gov:
            conf = "medium"
        else:
            conf = "high"
    rec["confidence"] = conf
    if not gov:
        notes["missingGovernorate"].append(rid)
    return rec


def main():
    wd = load_json(os.path.join(CACHE, "wikidata.json"))
    ents = wd["entities"]
    egym = load_json(os.path.join(CACHE, "egymonuments.json"))
    wl = load_json(os.path.join(CACHE, "wikipedia_lists.json"), {})
    osm = load_json(os.path.join(CACHE, "osm_crosscheck.json"), [])
    sites = load_json(os.path.join(HERE, "sites_curated.json"))
    man = load_json(os.path.join(HERE, "museums_manual.json"))

    notes = {k: [] for k in ("needsEnglishName", "missingCoords", "multipleCoords",
                             "missingGovernorate", "duplicateIds")}
    ar_list_url = wl.get("ar", {}).get("page")
    en_list_url = wl.get("en", {}).get("page")
    ar_qids = {r.get("qid") for r in wl.get("ar", {}).get("rows", []) if r.get("qid")}
    en_qids = {r.get("qid") for r in wl.get("en", {}).get("rows", []) if r.get("qid")}

    places = []

    # ---- museums -------------------------------------------------------
    exclude = man["exclude"]
    merge = man["merge"]
    overrides = man["overrides"]
    egym_map = man["egym"]
    mota = set(man["mota"])
    museum_qids = set(wd["museumQids"]) | {a["qid"] for a in man["add"] if a.get("qid")}
    site_qids = {s["qid"] for s in sites if s.get("qid")}
    dups_of = {}
    for d, p in merge.items():
        dups_of.setdefault(p, []).append(d)
    primaries = sorted(q for q in museum_qids
                       if q not in exclude and q not in merge and q not in site_qids)
    for q in primaries:
        dq = dups_of.get(q, [])
        e = merged_view(q, dq, ents)
        cur = dict(overrides.get(q, {}))
        cur["mota"] = q in mota
        egp = [egym_map[q]] if q in egym_map else []
        via = []
        if ar_list_url and (q in ar_qids or any(d in ar_qids for d in dq)):
            via.append(ar_list_url)
        if en_list_url and (q in en_qids or any(d in en_qids for d in dq)):
            via.append(en_list_url)
        name = cur.get("en") or e.get("en") or e.get("mul") or e.get("other") or e.get("ar") or q
        rid = cur.get("id") or slugify(e.get("en") or e.get("mul") or e.get("other") or name) or q.lower()
        places.append(make_record("museum", rid, q, e, dq, ents, cur, egp, notes, via))
    for a in man["add"]:
        if a.get("qid"):
            continue
        cur = dict(a)
        via = []
        if "arwiki" in a.get("via", "") and ar_list_url:
            via.append(ar_list_url)
        if "enwiki" in a.get("via", "") and en_list_url:
            via.append(en_list_url)
        if a.get("osm"):
            via.append("https://www.openstreetmap.org/" + a["osm"])
            cur.setdefault("osmId", a["osm"])
        places.append(make_record("museum", a["id"], None, {}, [], ents, cur,
                                  a.get("egym", []), notes, via))

    # ---- sites ---------------------------------------------------------
    for s in sites:
        q = s.get("qid")
        dq = s.get("dups", [])
        e = merged_view(q, dq, ents)
        places.append(make_record("site", s["id"], q, e, dq, ents, s, s.get("egym", []), notes, []))

    # ---- OSM ids by explicit wikidata tag (ids only) ----------------------
    osm_by_q = {}
    for o in osm:
        if o.get("wikidata"):
            osm_by_q.setdefault(o["wikidata"], []).append(o["osm"])
    for p in places:
        if not p["links"].get("osm") and p["wikidataId"] in osm_by_q:
            ids = sorted(osm_by_q[p["wikidataId"]], key=lambda x: ("relation way node".split().index(x.split("/")[0]), x))
            p["links"]["osm"] = ids[0]

    # ---- unique ids ----------------------------------------------------
    seen = {}
    for p in places:
        if p["id"] in seen:
            notes["duplicateIds"].append(p["id"])
            p["id"] = f"{p['id']}-{p['governorate']}"
        seen[p["id"]] = True

    places.sort(key=lambda p: (p["governorate"] or "zzz", p["name"]["en"].lower()))
    save_json(os.path.join(REPO, "data", "seed", "places.json"), places)
    save_json(os.path.join(CACHE, "build_notes.json"), notes)
    print(f"{len(places)} places "
          f"({sum(p['kind'] == 'museum' for p in places)} museums, "
          f"{sum(p['kind'] == 'site' for p in places)} sites)")
    for k, v in notes.items():
        if v:
            print(f"  {k}: {len(v)}")


if __name__ == "__main__":
    main()
