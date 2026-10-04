#!/usr/bin/env python3
"""Merge data/seed/places.json with enriched data/places/<id>.json into v1/places.json + v1/meta.json.

Enriched files replace the seed record with the same id. Output is what the app bundles and fetches via jsDelivr.
"""
import json, pathlib, datetime, hashlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
seed = {p["id"]: p for p in json.loads((ROOT / "data/seed/places.json").read_text())}
enriched = 0
for f in sorted((ROOT / "data/places").glob("*.json")) if (ROOT / "data/places").exists() else []:
    rec = json.loads(f.read_text())
    seed[rec["id"]] = rec
    enriched += 1
places = sorted(seed.values(), key=lambda p: ({"major": 0, "notable": 1, "minor": 2}[p.get("tier", "minor")], p["governorate"], p["name"]["en"]))
out = ROOT / "v1"
out.mkdir(exist_ok=True)
body = json.dumps(places, ensure_ascii=False, separators=(",", ":"))
(out / "places.json").write_text(body)
meta = {
    "schemaVersion": 1,
    "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "count": len(places),
    "enriched": enriched,
    "sha256": hashlib.sha256(body.encode()).hexdigest(),
}
(out / "meta.json").write_text(json.dumps(meta, indent=1))
print(meta)
