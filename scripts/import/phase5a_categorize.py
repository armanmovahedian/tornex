"""Phase 5 prep: best-effort keyword mapping of each barghsan product to one of
Tornex's 26 real product_category terms (4 parents x 22 children). No LLM --
pure keyword matching against product name + barghsan attribute terms, so we
can see the real scale of the mismatch before deciding how to handle it.
Writes data/category_mapping_report.json (counts) and data/category_mapping.json
(per-product decision: matched term id/name, or null if nothing matched).
"""
import json
import os
import re

HERE = os.path.dirname(__file__)
DATA_DIR = os.path.join(HERE, "..", "..", "data")
RAW_PATH = os.path.join(DATA_DIR, "raw_products.jsonl")
CATS_PATH = os.path.join(DATA_DIR, "tornex_categories.json")
OUT_MAP = os.path.join(DATA_DIR, "category_mapping.json")
OUT_REPORT = os.path.join(DATA_DIR, "category_mapping_report.json")

# Ordered most-specific-first: each Tornex category name maps to a list of
# keywords/phrases. First category (in this list order) whose keyword is found
# in the product's searchable text wins.
KEYWORD_RULES = [
    ("باکس و اسپلایس فیبر نوری", ["اسپلایس", "باکس فیبر", "جوینت باکس", "اسپلیس"]),
    ("پچ پنل شبکه", ["پچ پنل"]),
    ("پچ کورد شبکه", ["پچ کورد شبکه", "پچ کورد کت", "پچ کورد utp", "پچ کورد rj"]),
    ("پچ کورد فیبر نوری", ["پچ کورد فیبر", "پچ کورد اپتیک", "پچ کورد نوری", "fiber patch"]),
    ("پریز شبکه", ["پریز شبکه", "کیستون", "فیس پلیت"]),
    ("ترانکینگ و اکسسوری", ["ترانکینگ", "داکت", "کانال کابل شبکه"]),
    ("سوییچ و مبدل شبکه", ["سوییچ شبکه", "سوئیچ شبکه", "مبدل فیبر", "مدیا کانورتور", "کانورتور"]),
    ("کابل شبکه", ["کابل شبکه", "کابل کت", "کابل utp", "کابل cat6", "کابل cat5", "کابل patch"]),
    ("کابل فیبر نوری", ["کابل فیبر", "کابل نوری", "فیبر نوری"]),
    ("چندراهی برق", ["چندراهی"]),
    ("روشنایی اضطراری", ["روشنایی اضطراری", "چراغ اضطراری"]),
    ("فیوز مینیاتوری", ["فیوز مینیاتور", "مینیاتوری"]),
    ("کلید و پریز", ["کلید و پریز", "کلید برق", "پریز برق"]),
    ("لوله و کانال کابل", ["لوله برق", "لوله خرطومی", "کانال کابل"]),
    ("محافظ جان", ["محافظ جان", "کلید محافظ جان", "rcd", "rccb"]),
    ("کابل آلومینیوم", ["کابل آلومینیوم", "کابل الومینیوم"]),
    ("کابل زره‌دار", ["زره‌دار", "زرهدار", "زره دار"]),
    ("کابل زمینی", ["کابل زمینی", "کابل زیرزمینی", "nyy", "n2xy"]),
    ("کابل شیلددار", ["شیلددار", "شیلد دار"]),
    ("کابل کنترل", ["کابل کنترل"]),
    ("سیم افشان", ["سیم افشان"]),
    ("کابل افشان", ["کابل افشان"]),
]

CAT_NAME_TO_ID = {}


def load_categories():
    with open(CATS_PATH, "r", encoding="utf-8") as f:
        cats = json.load(f)
    for c in cats:
        CAT_NAME_TO_ID[c["name"]] = c["id"]
    return cats


def strip_html(s):
    return re.sub(r"<[^>]+>", " ", s or "")


def searchable_text(p):
    parts = [p.get("name", "")]
    for attr in p.get("attributes", []):
        parts.append(attr.get("name", ""))
        for t in attr.get("terms", []):
            parts.append(t.get("name", ""))
    for c in p.get("categories", []):
        parts.append(c.get("name", ""))
    return strip_html(" ".join(parts)).lower()


def match_category(text):
    for cat_name, keywords in KEYWORD_RULES:
        for kw in keywords:
            if kw.lower() in text:
                return cat_name
    return None


def main():
    load_categories()

    with open(RAW_PATH, "r", encoding="utf-8") as f:
        products = [json.loads(line) for line in f]

    results = []
    counts = {}
    unmatched = []

    for p in products:
        text = searchable_text(p)
        cat = match_category(text)
        results.append({
            "id": p["id"],
            "slug": p["slug"],
            "name": strip_html(p["name"]),
            "matched_category": cat,
            "matched_category_id": CAT_NAME_TO_ID.get(cat) if cat else None,
            "barghsan_categories": [c["name"] for c in p.get("categories", [])],
        })
        key = cat or "(بدون تطابق)"
        counts[key] = counts.get(key, 0) + 1
        if not cat:
            unmatched.append({"name": strip_html(p["name"]), "barghsan_categories": [c["name"] for c in p.get("categories", [])]})

    with open(OUT_MAP, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    report = {
        "total_products": len(products),
        "matched": len(products) - len(unmatched),
        "unmatched": len(unmatched),
        "counts_by_category": dict(sorted(counts.items(), key=lambda kv: -kv[1])),
        "unmatched_sample": unmatched[:40],
    }
    with open(OUT_REPORT, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"total: {len(products)}  matched: {report['matched']}  unmatched: {report['unmatched']}")


if __name__ == "__main__":
    main()
