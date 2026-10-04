"""Cross-check against OpenStreetMap via Overpass (ODbL) - CROSS-CHECK ONLY.

Fetches tags only (`out tags;`, no geometry) for museums, archaeological sites
and a few heritage tags in Egypt. Nothing from here is copied into the dataset
except OSM element ids (type/id) for places matched by an explicit `wikidata`
tag. Coordinates are never requested.

Output: tools/seed/cache/osm_crosscheck.json
"""
import json
import os

from common import CACHE, http, save_json

OVERPASS = "https://overpass-api.de/api/interpreter"
QUERY = """
[out:json][timeout:180];
area["ISO3166-1"="EG"][admin_level=2]->.eg;
(
  nwr["tourism"="museum"](area.eg);
  nwr["historic"="archaeological_site"]["wikidata"](area.eg);
  nwr["historic"="archaeological_site"]["tourism"="attraction"](area.eg);
  nwr["historic"~"^(monastery|castle|fort|palace|temple|tomb|pyramid)$"]["wikidata"](area.eg);
);
out tags;
"""


def main():
    raw = http(OVERPASS, data={"data": QUERY}, timeout=240)
    els = json.loads(raw)["elements"]
    out = []
    for e in els:
        t = e.get("tags", {})
        out.append({
            "osm": f"{e['type']}/{e['id']}",
            "wikidata": t.get("wikidata"),
            "name": t.get("name:en") or t.get("name"),
            "nameAr": t.get("name:ar"),
            "tourism": t.get("tourism"),
            "historic": t.get("historic"),
        })
    save_json(os.path.join(CACHE, "osm_crosscheck.json"), out)
    print(f"{len(out)} OSM elements (tags only)")


if __name__ == "__main__":
    main()
