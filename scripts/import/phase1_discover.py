"""Phase 1: discover the reference list of all barghsan.com product URLs from the sitemap."""
import re
import time
import urllib.request
import json
import os

UA = "Mozilla/5.0 (compatible; TornexImportBot/1.0; +https://tornex.ir)"
SITEMAP_URL = "https://www.barghsan.com/product-sitemap.xml"
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "reference_products.json")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def main():
    xml = fetch(SITEMAP_URL)
    locs = re.findall(r"<loc>(.*?)</loc>", xml)
    product_urls = [u for u in locs if "/product/" in u]

    slugs = []
    for url in product_urls:
        slug = url.rstrip("/").rsplit("/", 1)[-1]
        slugs.append({"url": url, "slug": slug})

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(slugs, f, ensure_ascii=False, indent=2)

    print(f"total <loc> entries: {len(locs)}")
    print(f"product URLs (/product/): {len(product_urls)}")
    print(f"other (non-product) URLs: {len(locs) - len(product_urls)}")
    print(f"saved -> {OUT_PATH}")


if __name__ == "__main__":
    main()
