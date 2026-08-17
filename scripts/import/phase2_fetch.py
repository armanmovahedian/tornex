"""Phase 2: fetch structured product data from barghsan.com's WooCommerce Store API.
Saves every record to data/raw_products.jsonl (one JSON object per line).
Cross-checks against data/reference_products.json (the sitemap list from phase 1)
and writes any slugs missing from the API into data/missing_from_api.json.
"""
import json
import os
import time
import urllib.request
import urllib.error

UA = "Mozilla/5.0 (compatible; TornexImportBot/1.0; +https://tornex.ir)"
BASE = "https://www.barghsan.com/wp-json/wc/store/v1/products"
DELAY = 0.4

HERE = os.path.dirname(__file__)
DATA_DIR = os.path.join(HERE, "..", "..", "data")
REF_PATH = os.path.join(DATA_DIR, "reference_products.json")
RAW_PATH = os.path.join(DATA_DIR, "raw_products.jsonl")
MISSING_PATH = os.path.join(DATA_DIR, "missing_from_api.json")


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8")
    # Some pages leak a stray <style> block (a misfiring plugin hook on barghsan's
    # side) before the actual JSON array -- strip anything before the first '['.
    start = body.find("[")
    if start > 0:
        body = body[start:]
    return json.loads(body)


def main():
    with open(REF_PATH, "r", encoding="utf-8") as f:
        reference = json.load(f)
    ref_slugs = {r["slug"] for r in reference}

    per_page = 100
    page = 1
    all_products = []

    while True:
        url = f"{BASE}?per_page={per_page}&page={page}"
        try:
            batch = fetch_json(url)
        except urllib.error.HTTPError as e:
            if per_page != 20:
                print(f"per_page={per_page} failed ({e.code}), retrying with per_page=20")
                per_page = 20
                page = 1
                all_products = []
                time.sleep(DELAY)
                continue
            raise
        if not batch:
            break
        all_products.extend(batch)
        print(f"page {page}: +{len(batch)} (total {len(all_products)})")
        page += 1
        time.sleep(DELAY)

    with open(RAW_PATH, "w", encoding="utf-8") as f:
        for p in all_products:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    api_slugs = {p["slug"] for p in all_products}
    missing = sorted(ref_slugs - api_slugs)
    with open(MISSING_PATH, "w", encoding="utf-8") as f:
        json.dump(missing, f, ensure_ascii=False, indent=2)

    print(f"\ntotal fetched from Store API: {len(all_products)}")
    print(f"reference (sitemap) count: {len(ref_slugs)}")
    print(f"in sitemap but missing from API: {len(missing)} -> {MISSING_PATH}")
    print(f"raw data saved -> {RAW_PATH}")


if __name__ == "__main__":
    main()
