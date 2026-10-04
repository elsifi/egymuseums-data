"""Helper used while curating sites_curated.json: search Wikidata for a name and
print candidate items (with country, P31 and coordinates) so a human can pick
the right QID. Usage: python3 wd_search.py "Karnak" "Luxor Temple" ...
or: python3 wd_search.py -f names.txt   (one name per line)."""
import json
import sys
import urllib.parse

from common import http, sparql, qid


def search(term, lang="en", limit=6):
    url = ("https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json"
           f"&language={lang}&uselang={lang}&type=item&limit={limit}&search="
           + urllib.parse.quote(term))
    return [r["id"] for r in json.loads(http(url)).get("search", [])]


def describe(qids):
    if not qids:
        return {}
    q = """SELECT ?item ?l ?d ?c ?co (GROUP_CONCAT(DISTINCT ?tl; separator=",") AS ?types) WHERE {
      VALUES ?item { %s }
      OPTIONAL { ?item rdfs:label ?l FILTER(lang(?l)="en") }
      OPTIONAL { ?item schema:description ?d FILTER(lang(?d)="en") }
      OPTIONAL { ?item wdt:P17 ?c }
      OPTIONAL { ?item wdt:P625 ?co }
      OPTIONAL { ?item wdt:P31 ?t . ?t rdfs:label ?tl FILTER(lang(?tl)="en") }
    } GROUP BY ?item ?l ?d ?c ?co""" % " ".join("wd:" + x for x in qids)
    out = {}
    for b in sparql(q):
        out.setdefault(qid(b["item"]["value"]), b)
    return out


def main():
    args = sys.argv[1:]
    if args and args[0] == "-f":
        args = [l.strip() for l in open(args[1], encoding="utf-8") if l.strip()]
    for term in args:
        lang = "ar" if any("؀" <= ch <= "ۿ" for ch in term) else "en"
        ids = search(term, lang)
        info = describe(ids)
        print(f"## {term}")
        for i in ids:
            b = info.get(i, {})
            g = lambda k: b.get(k, {}).get("value", "")
            eg = "EG" if g("c").endswith("/Q79") else (qid(g("c")) if g("c") else "--")
            print(f"   {i:11} {eg:5} {g('l')[:45]:45} | {g('d')[:50]:50} | {g('types')[:60]} | {'C' if g('co') else '-'}")


if __name__ == "__main__":
    main()
