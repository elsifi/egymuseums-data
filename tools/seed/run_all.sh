#!/bin/sh
# Re-run the whole seed pipeline (network: egymonuments.gov.eg, mota.gov.eg,
# Wikipedia API, Wikidata Query Service, Overpass). Python 3 stdlib only.
set -e
cd "$(dirname "$0")"
python3 fetch_egymonuments.py
python3 fetch_mota_tickets.py
python3 fetch_wikipedia_lists.py
python3 fetch_wikidata.py
python3 fetch_osm_crosscheck.py
python3 build_places.py
python3 validate.py
python3 make_report.py
