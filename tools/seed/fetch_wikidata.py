"""Fetch Wikidata (CC0) identity + coordinates for museums and curated sites.

Steps
  1. Enumerate museums in Egypt (queries MUSEUMS_P17 and MUSEUMS_P131 below).
  2. Read the QIDs of curated sites from sites_curated.json and of manual
     museum additions from museums_manual.json.
  3. Fetch details for every QID in batches (labels, aliases, P31, P625,
     governorate via P131*, direct P131, sitelinks, website, OSM ids,
     dissolution / state-of-use hints).

Output: tools/seed/cache/wikidata.json  {"museumQids": [...], "entities": {QID: {...}}}
"""
import os
import sys

from common import (CACHE, GOV_BY_QID, HERE, chunks, load_json, qid, save_json,
                    sparql, val)

MUSEUMS_P17 = """
SELECT DISTINCT ?item WHERE {
  ?item wdt:P17 wd:Q79 .
  ?item wdt:P31/wdt:P279* wd:Q33506 .
}"""

# Museums whose P131 is an Egyptian admin unit but which lack P17=Egypt.
# (A single "P131+ wd:Q79" path query times out on WDQS, hence two queries.)
MUSEUMS_P131 = """
SELECT DISTINCT ?item WHERE {
  ?adm wdt:P17 wd:Q79 .
  ?item wdt:P131 ?adm .
  FILTER NOT EXISTS { ?item wdt:P17 wd:Q79 }
  ?item wdt:P31/wdt:P279* wd:Q33506 .
}"""

DETAILS_BASIC = """
SELECT ?item ?en ?ar ?mul ?arz ?other ?coord ?enwiki ?arwiki ?website ?osmRel ?osmWay ?osmNode
       ?dissolved ?closed ?inception ?country WHERE {
  VALUES ?item { %s }
  OPTIONAL { ?item rdfs:label ?en FILTER(lang(?en)="en") }
  OPTIONAL { ?item rdfs:label ?ar FILTER(lang(?ar)="ar") }
  OPTIONAL { ?item rdfs:label ?mul FILTER(lang(?mul)="mul") }
  OPTIONAL { ?item rdfs:label ?arz FILTER(lang(?arz)="arz") }
  OPTIONAL { ?item rdfs:label ?other FILTER(lang(?other) IN ("de","fr","tr")) }
  OPTIONAL { ?item wdt:P625 ?coord }
  OPTIONAL { ?enwiki schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> }
  OPTIONAL { ?arwiki schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> }
  OPTIONAL { ?item wdt:P856 ?website }
  OPTIONAL { ?item wdt:P402 ?osmRel }
  OPTIONAL { ?item wdt:P10689 ?osmWay }
  OPTIONAL { ?item wdt:P11693 ?osmNode }
  OPTIONAL { ?item wdt:P576 ?dissolved }
  OPTIONAL { ?item wdt:P3999 ?closed }
  OPTIONAL { ?item wdt:P571 ?inception }
  OPTIONAL { ?item wdt:P17 ?country }
}"""

DETAILS_ALIASES = """
SELECT ?item ?alias WHERE {
  VALUES ?item { %s }
  ?item skos:altLabel ?alias FILTER(lang(?alias)="en" || lang(?alias)="ar")
}"""

DETAILS_TYPES = """
SELECT ?item ?type ?typeLabel WHERE {
  VALUES ?item { %s }
  ?item wdt:P31 ?type .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}"""

DETAILS_ADMIN = """
SELECT ?item ?adm ?admEn ?admAr WHERE {
  VALUES ?item { %s }
  ?item wdt:P131 ?adm .
  OPTIONAL { ?adm rdfs:label ?admEn FILTER(lang(?admEn)="en") }
  OPTIONAL { ?adm rdfs:label ?admAr FILTER(lang(?admAr)="ar") }
}"""

DETAILS_GOV = """
SELECT DISTINCT ?item ?gov WHERE {
  VALUES ?item { %s }
  VALUES ?gov { %s }
  { ?item wdt:P131* ?gov } UNION { ?item wdt:P276/wdt:P131* ?gov }
  UNION { ?item wdt:P361/wdt:P131* ?gov }
}"""

DETAILS_MISC = """
SELECT ?item ?prop ?v ?vLabel WHERE {
  VALUES ?item { %s }
  VALUES (?prop ?p) { ("operator" wdt:P137) ("owner" wdt:P127) ("partOf" wdt:P361)
                      ("location" wdt:P276) ("stateOfUse" wdt:P5817)
                      ("heritage" wdt:P1435) ("replacedBy" wdt:P1366) }
  ?item ?p ?v .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}"""


def values(qids):
    return " ".join(f"wd:{q}" for q in qids)


def fetch_details(qids, ents):
    govs = " ".join(f"wd:{q}" for q in GOV_BY_QID)
    for batch in chunks(sorted(qids), 80):
        v = values(batch)
        print(f"  details for {len(batch)} items ...")
        for b in sparql(DETAILS_BASIC % v):
            e = ents.setdefault(qid(b["item"]["value"]), {})
            for k in ("en", "ar", "mul", "arz", "other", "enwiki", "arwiki", "website", "osmRel", "osmWay",
                      "osmNode", "dissolved", "closed", "inception"):
                x = val(b, k)
                if x and not e.get(k):
                    e[k] = x
            c = val(b, "coord")
            if c and c.startswith("Point("):
                lng, lat = c[6:-1].split()
                e.setdefault("coords", [])
                pt = [round(float(lat), 6), round(float(lng), 6)]
                if pt not in e["coords"]:
                    e["coords"].append(pt)
            if val(b, "country"):
                e.setdefault("countries", set()).add(qid(val(b, "country")))
        for b in sparql(DETAILS_ALIASES % v):
            e = ents.setdefault(qid(b["item"]["value"]), {})
            e.setdefault("aliases", []).append(
                {"lang": b["alias"]["xml:lang"], "value": b["alias"]["value"]})
        for b in sparql(DETAILS_TYPES % v):
            e = ents.setdefault(qid(b["item"]["value"]), {})
            t = [qid(b["type"]["value"]), val(b, "typeLabel")]
            e.setdefault("types", [])
            if t not in e["types"]:
                e["types"].append(t)
        for b in sparql(DETAILS_ADMIN % v):
            e = ents.setdefault(qid(b["item"]["value"]), {})
            a = {"qid": qid(b["adm"]["value"]), "en": val(b, "admEn"), "ar": val(b, "admAr")}
            e.setdefault("admin", [])
            if a not in e["admin"]:
                e["admin"].append(a)
        for b in sparql(DETAILS_GOV % (v, govs)):
            e = ents.setdefault(qid(b["item"]["value"]), {})
            g = GOV_BY_QID[qid(b["gov"]["value"])]
            e.setdefault("govs", [])
            if g not in e["govs"]:
                e["govs"].append(g)
        for b in sparql(DETAILS_MISC % v):
            e = ents.setdefault(qid(b["item"]["value"]), {})
            m = e.setdefault("misc", {}).setdefault(val(b, "prop"), [])
            x = [qid(b["v"]["value"]) if "entity/" in b["v"]["value"] else b["v"]["value"],
                 val(b, "vLabel")]
            if x not in m:
                m.append(x)
    for e in ents.values():
        if isinstance(e.get("countries"), set):
            e["countries"] = sorted(e["countries"])


def main():
    out_path = os.path.join(CACHE, "wikidata.json")
    print("museum enumeration ...")
    museums = sorted({qid(b["item"]["value"]) for q in (MUSEUMS_P17, MUSEUMS_P131)
                      for b in sparql(q)})
    print(f"  {len(museums)} museum items")
    sites = load_json(os.path.join(HERE, "sites_curated.json"), [])
    manual = load_json(os.path.join(HERE, "museums_manual.json"), {})
    extra = [s["qid"] for s in sites if s.get("qid")]
    extra += [d for s in sites for d in s.get("dups", [])]
    extra += [a["qid"] for a in manual.get("add", []) if a.get("qid")]
    extra += list(manual.get("merge", {})) + list(manual.get("merge", {}).values())
    extra += sys.argv[1:]
    qids = sorted(set(museums) | set(extra))
    ents = {}
    fetch_details(qids, ents)
    save_json(out_path, {"museumQids": museums, "entities": ents,
                         "queries": {"MUSEUMS_P17": MUSEUMS_P17.strip(),
                                     "MUSEUMS_P131": MUSEUMS_P131.strip()}})
    print(f"wrote {out_path} ({len(ents)} entities)")


if __name__ == "__main__":
    main()
