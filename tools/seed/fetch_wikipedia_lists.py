"""Enumerate museums from Wikipedia list articles (cross-check only).

  * ar: قائمة متاحف مصر  (rows: name + section)
  * en: List of museums in Egypt

Only article titles / row names and section headings are kept, plus the
Wikidata QID each linked article resolves to. No descriptive text is copied.

Output: tools/seed/cache/wikipedia_lists.json
"""
import json
import os
import re
import urllib.parse

from common import CACHE, chunks, http, save_json

PAGES = {
    "ar": "قائمة متاحف مصر",
    "en": "List of museums in Egypt",
}


def api(lang, **params):
    params.setdefault("format", "json")
    params.setdefault("formatversion", "2")
    url = f"https://{lang}.wikipedia.org/w/api.php?" + urllib.parse.urlencode(params)
    return json.loads(http(url))


def wikitext(lang, title):
    d = api(lang, action="parse", page=title, prop="wikitext", redirects=1)
    return d["parse"]["wikitext"]


def rows_ar(w):
    """Rows of the AR list are table header cells: '![[Title|label]]' or '!plain name'."""
    sec, out = None, []
    for line in w.split("\n"):
        m = re.match(r"^(=+)\s*(.*?)\s*=+\s*$", line)
        if m:
            sec = m.group(2)
            continue
        if not line.startswith("!") or line.startswith("! scope") or line.startswith("!'"):
            continue
        cell = line[1:].strip()
        if cell in ("نبذة", "مرجع", ""):
            continue
        lk = re.match(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", cell)
        if lk:
            out.append({"section": sec, "title": lk.group(1).strip(),
                        "label": (lk.group(2) or lk.group(1)).strip()})
        else:
            out.append({"section": sec, "title": None, "label": cell})
    return out


def rows_en(w):
    """EN list: wikitable rows; take the first wikilink of each row's first cell."""
    sec, out = None, []
    for line in w.split("\n"):
        m = re.match(r"^(=+)\s*(.*?)\s*=+\s*$", line)
        if m:
            sec = m.group(2)
            continue
        if line.startswith("|-"):
            continue
        m = re.match(r"^[|*!]\s*(?:'')?\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]", line)
        if m and not m.group(1).lower().startswith(("file:", "image:", "category:")):
            out.append({"section": sec, "title": m.group(1).strip(),
                        "label": (m.group(2) or m.group(1)).strip()})
    return out


def resolve(lang, titles):
    res = {}
    for batch in chunks(sorted(set(titles)), 40):
        d = api(lang, action="query", titles="|".join(batch), prop="pageprops",
                ppprop="wikibase_item", redirects=1)
        q = d["query"]
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        redir = {r["from"]: r["to"] for r in q.get("redirects", [])}
        pages = {p["title"]: p for p in q["pages"]}
        for t in batch:
            t2 = norm.get(t, t)
            t2 = redir.get(t2, t2)
            p = pages.get(t2, {})
            res[t] = {"resolved": t2, "qid": p.get("pageprops", {}).get("wikibase_item"),
                      "missing": bool(p.get("missing"))}
    return res


def main():
    out = {}
    for lang, title in PAGES.items():
        w = wikitext(lang, title)
        rows = rows_ar(w) if lang == "ar" else rows_en(w)
        ids = resolve(lang, [r["title"] for r in rows if r["title"]])
        for r in rows:
            if r["title"]:
                r.update(ids[r["title"]])
        out[lang] = {"page": f"https://{lang}.wikipedia.org/wiki/"
                     + urllib.parse.quote(title.replace(" ", "_")),
                     "rows": rows}
        print(f"{lang}: {len(rows)} rows, {sum(1 for r in rows if r.get('qid'))} with QID")
    save_json(os.path.join(CACHE, "wikipedia_lists.json"), out)


if __name__ == "__main__":
    main()
