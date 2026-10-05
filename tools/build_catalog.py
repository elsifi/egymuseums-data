#!/usr/bin/env python3
"""Merge data/seed/places.json with enriched data/places/<id>.json into v1/places.json + v1/meta.json.

Enriched files replace the seed record with the same id. Ids listed in tools/seed/excluded.json (duplicates and
records that are not real visitable places) are left out of the catalog; their seed records stay for provenance.
Output is what the app bundles and fetches via jsDelivr.

Versioning: `schemaVersion` is the major version and changes only on breaking changes; apps built for 1 keep
working. `schemaMinor` counts additive changes: 1.1 (2026-10-04) added optional prices.status,
prices.tiers[].onlineAmount and prices.extras[].audience/group/onlineAmount. Clients should ignore unknown fields.
"""
import json, pathlib, datetime, hashlib

SCHEMA_VERSION = 1  # major: bump only for breaking changes
SCHEMA_MINOR = 4    # minor: additive fields only (1.1 = 2026-10-04)

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXCLUDED_FILE = ROOT / "tools/seed/excluded.json"
excluded = {e["id"] for e in json.loads(EXCLUDED_FILE.read_text())} if EXCLUDED_FILE.exists() else set()
seed = {p["id"]: p for p in json.loads((ROOT / "data/seed/places.json").read_text()) if p["id"] not in excluded}
enriched = 0
for f in sorted((ROOT / "data/places").glob("*.json")) if (ROOT / "data/places").exists() else []:
    rec = json.loads(f.read_text())
    if rec["id"] in excluded:
        continue
    seed[rec["id"]] = rec
    enriched += 1
places = sorted(seed.values(), key=lambda p: ({"major": 0, "notable": 1, "minor": 2}[p.get("tier", "minor")], p["governorate"], p["name"]["en"]))
out = ROOT / "v1"
out.mkdir(exist_ok=True)
body = json.dumps(places, ensure_ascii=False, separators=(",", ":"))
(out / "places.json").write_text(body)
meta = {
    "schemaVersion": SCHEMA_VERSION,
    "schemaMinor": SCHEMA_MINOR,
    "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "count": len(places),
    "enriched": enriched,
    "excluded": len(excluded),
    "sha256": hashlib.sha256(body.encode()).hexdigest(),
}
(out / "meta.json").write_text(json.dumps(meta, indent=1))
print(meta)
