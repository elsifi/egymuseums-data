"""Enumerate places listed on egymonuments.gov.eg (MoTA portal).

Sources:
  * https://egymonuments.gov.eg/en/sitemap.aspx and /ar/sitemap.aspx
  * the portal's own map-pin endpoint (Umbraco/Api/MapsWebAPI/GetAllMapPins),
    which returns every museum / archaeological-site / monument page with its
    EN and AR title.

Only identity data is kept: page id, section, URL and EN/AR title. Descriptions
and the portal's coordinates are deliberately dropped (licensing: we only use the
portal to enumerate and to record URLs).

Output: tools/seed/cache/egymonuments.json
"""
import json
import os
import re

from common import CACHE, http, save_json

BASE = "https://egymonuments.gov.eg"
SECTIONS = ("museums", "archaeological-sites", "monuments", "sunken-monuments",
            "world-heritage")


def sitemap(lang):
    raw = http(f"{BASE}/{lang}/sitemap.aspx").decode("utf-8", "replace")
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", raw)


def pins(lang):
    raw = http(f"{BASE}/Umbraco/Api/MapsWebAPI/GetAllMapPins", data=b"{}",
               headers={"culture": lang, "Content-Type": "application/json"})
    return json.loads(raw)["Data"]["ListItems"]


def main():
    out = {}
    for lang in ("en", "ar"):
        for p in pins(lang):
            rec = out.setdefault(p["Id"], {"portalId": p["Id"]})
            path = p["ContentUrlName"].strip()
            rec["section"] = path.strip("/").split("/")[1]
            rec[f"url_{lang}"] = BASE + path + "/"
            rec[f"title_{lang}"] = re.sub(r"\s+", " ", p["Title"]).strip()
    # Sitemap entries for the listed sections that the pin feed lacks.
    seen = {r.get("url_en") for r in out.values()}
    extra = []
    for u in sitemap("en"):
        parts = u.replace(BASE, "").strip("/").split("/")
        if len(parts) == 3 and parts[1] in SECTIONS and u not in seen:
            extra.append({"section": parts[1], "url_en": u, "slug": parts[2]})
    data = {"pins": sorted(out.values(), key=lambda r: (r["section"], r["portalId"])),
            "sitemapOnly": extra}
    save_json(os.path.join(CACHE, "egymonuments.json"), data)
    from collections import Counter
    print("pins:", Counter(r["section"] for r in data["pins"]))
    print("sitemap-only entries:", len(extra))


if __name__ == "__main__":
    main()
