"""Download the MoTA ticket-price list (PDF, Nov 2024) and extract its text lines
with a tiny stdlib PDF text extractor. Used ONLY to enumerate which sites and
museums sell tickets (the `mota` flags in sites_curated.json /
museums_manual.json were set by reading this output). Prices/hours are NOT
taken into the seed; they will be sourced and dated per place later.

Output: tools/seed/cache/mota_tickets.txt
"""
import os
import re
import zlib

from common import CACHE, http

URL = "https://mota.gov.eg/media/5a2ja2iu/ticket-english-5-11-2024-1.pdf"


def lit(s):
    return re.sub(rb"\\([()\\])", rb"\1", s).decode("latin-1")


def extract(pdf):
    lines, page = [], 0
    for s in re.findall(rb"stream\r?\n(.*?)\r?\nendstream", pdf, re.S):
        try:
            t = zlib.decompress(s)
        except zlib.error:
            continue
        if b"BT" not in t:
            continue
        page += 1
        lines.append(f"=== page {page}")
        rows = {}
        for bt in re.findall(rb"BT(.*?)ET", t, re.S):
            m = re.search(rb"1 0 0 1 ([\d.]+) ([\d.]+) Tm", bt)
            if not m:
                continue
            x, y = float(m.group(1)), float(m.group(2))
            parts = []
            for arr in re.findall(rb"\[(.*?)\]\s*TJ", bt, re.S):
                parts += [lit(p) for p in re.findall(rb"\(((?:\\.|[^\\)])*)\)", arr)]
            txt = "".join(parts)
            if txt.strip():
                rows.setdefault(round(y), []).append((x, txt))
        for y in sorted(rows, reverse=True):
            lines.append(" | ".join(t.strip() for _, t in sorted(rows[y]) if t.strip()))
    return lines


def main():
    pdf = http(URL)
    lines = extract(pdf)
    path = os.path.join(CACHE, "mota_tickets.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# source: {URL}\n" + "\n".join(lines) + "\n")
    print(f"wrote {path} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
