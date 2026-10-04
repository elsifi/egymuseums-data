"""Shared helpers for the EgyMuseums seed pipeline (stdlib only)."""
import json
import os
import time
import urllib.parse
import urllib.request

UA = "EgyMuseumsSeed/0.1 (mo.elsifi@gmail.com)"
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
CACHE = os.path.join(HERE, "cache")
CHECKED_AT = "2026-10-04"
SPARQL = "https://query.wikidata.org/sparql"

os.makedirs(CACHE, exist_ok=True)


def http(url, data=None, headers=None, retries=4, timeout=90):
    h = {"User-Agent": UA}
    h.update(headers or {})
    if isinstance(data, dict):
        data = urllib.parse.urlencode(data).encode()
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=data, headers=h)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001
            if attempt == retries - 1:
                raise
            wait = 5 * (attempt + 1)
            print(f"  retry {attempt + 1} after {e!r} (sleep {wait}s)")
            time.sleep(wait)


def sparql(query):
    """POST a SPARQL query to WDQS and return the bindings list."""
    raw = http(SPARQL, data={"query": query},
               headers={"Accept": "application/sparql-results+json"})
    return json.loads(raw)["results"]["bindings"]


def qid(uri):
    return uri.rsplit("/", 1)[-1]


def val(b, k):
    v = b.get(k)
    return v["value"] if v else None


def load_json(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


# Egypt's 27 governorates: kebab id -> (Wikidata QID, en, ar)
GOVERNORATES = {
    "cairo": ("Q30805", "Cairo", "القاهرة"),
    "giza": ("Q30832", "Giza", "الجيزة"),
    "alexandria": ("Q29943", "Alexandria", "الإسكندرية"),
    "qalyubia": ("Q31075", "Qalyubia", "القليوبية"),
    "sharqia": ("Q31074", "Sharqia", "الشرقية"),
    "dakahlia": ("Q31068", "Dakahlia", "الدقهلية"),
    "gharbia": ("Q30835", "Gharbia", "الغربية"),
    "monufia": ("Q30786", "Monufia", "المنوفية"),
    "beheira": ("Q30630", "Beheira", "البحيرة"),
    "kafr-el-sheikh": ("Q30946", "Kafr El Sheikh", "كفر الشيخ"),
    "damietta": ("Q30644", "Damietta", "دمياط"),
    "port-said": ("Q31079", "Port Said", "بورسعيد"),
    "ismailia": ("Q31067", "Ismailia", "الإسماعيلية"),
    "suez": ("Q31070", "Suez", "السويس"),
    "north-sinai": ("Q30662", "North Sinai", "شمال سيناء"),
    "south-sinai": ("Q30815", "South Sinai", "جنوب سيناء"),
    "red-sea": ("Q30831", "Red Sea", "البحر الأحمر"),
    "matrouh": ("Q30682", "Matrouh", "مطروح"),
    "new-valley": ("Q30650", "New Valley", "الوادي الجديد"),
    "faiyum": ("Q30656", "Faiyum", "الفيوم"),
    "beni-suef": ("Q30683", "Beni Suef", "بني سويف"),
    "minya": ("Q30675", "Minya", "المنيا"),
    "asyut": ("Q29965", "Asyut", "أسيوط"),
    "sohag": ("Q30669", "Sohag", "سوهاج"),
    "qena": ("Q31065", "Qena", "قنا"),
    "luxor": ("Q30797", "Luxor", "الأقصر"),
    "aswan": ("Q29937", "Aswan", "أسوان"),
}
# Defunct / overlapping Wikidata admin units mapped to current governorates.
EXTRA_GOV_QIDS = {
    "Q328134": "giza",    # 6th of October Governorate (merged back into Giza 2011)
    "Q475035": "cairo",   # Helwan Governorate (merged back into Cairo 2011)
}
GOV_BY_QID = {v[0]: k for k, v in GOVERNORATES.items()}
GOV_BY_QID.update(EXTRA_GOV_QIDS)
