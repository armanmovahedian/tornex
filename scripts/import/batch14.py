# -*- coding: utf-8 -*-
"""Batch 14: 20 products -- Schneider Acti9 4-pole MCBs, Curve C (4-63A)
and Curve B (4-63A) variants."""
import json
import os
import urllib.request

HERE = os.path.dirname(__file__)
DATA_DIR = os.path.join(HERE, "..", "..", "data")
ENDPOINT = "https://tornex.ir/tornex-import.php?token=d6b9392341097d07d63e7cf5804498bb"

with open(os.path.join(DATA_DIR, "batch_slugs.json"), encoding="utf-8") as f:
    slugs = json.load(f)

pre_by_slug = {}
with open(os.path.join(DATA_DIR, "preprocessed_products.jsonl"), encoding="utf-8") as f:
    for line in f:
        row = json.loads(line)
        if row["slug"] in slugs:
            pre_by_slug[row["slug"]] = row

SCHNEIDER_STD = "EN 60898-1، EN 60947-2، IEC 60947-2، IEC 60898-1"
POLE_APP = "حفاظت از مدارهای سه‌فاز به همراه نول در ساختمان‌های تجاری و صنعتی با نیاز به حفاظت کامل خط نول"

CURVE_DESC = {
    "C": "برای مدارهایی با جریان هجومی راه‌اندازی متوسط مانند موتورها و تجهیزات القایی",
    "B": "برای مدارهای عمومی روشنایی و پریز با جریان راه‌اندازی پایین",
}


def schneider4p_content(amp, curve):
    curve_desc = CURVE_DESC[curve]
    return f"""<p>کلید مینیاتوری چهار پل {amp} آمپر کلاس {curve} اشنایدر از سری Acti9 با ولتاژ عایقی ۵۰۰ ولت و ولتاژ ضربه‌ای ۶ کیلوولت، برای مدارهای سه‌فاز همراه با نول طراحی شده است. ظرفیت قطع آن ۶ کیلوآمپر است و برای شبکه‌های AC و DC تا ۴۰۰ ولت مناسب است. منحنی قطع {curve} این کلید {curve_desc}.</p>
<p>این کلید با درجه حفاظت IP20، دوام مکانیکی ۲۰۰۰۰ سیکل و دوام الکتریکی ۱۰۰۰۰ سیکل تولید شده و در دمای کاری ۳۵- تا ۷۰+ درجه سانتی‌گراد (و نگهداری تا ۸۵+ درجه) کار می‌کند. ابعاد آن ارتفاع ۸۵ میلی‌متر، عرض ۷۲ میلی‌متر و عمق ۷۸.۵ میلی‌متر با وزن ۵۰۰ گرم است. روی ریل DIN نصب می‌شود و ترمینال‌های آن سیم‌های مفتولی تا ۲۵ میلی‌متر مربع و سیم‌های نرم تا ۱۶ میلی‌متر مربع را می‌پذیرند.</p>"""


AUTHORED = [
    {"amp": 4, "curve": "C"},
    {"amp": 6, "curve": "C"},
    {"amp": 10, "curve": "C"},
    {"amp": 16, "curve": "C"},
    {"amp": 20, "curve": "C"},
    {"amp": 25, "curve": "C"},
    {"amp": 32, "curve": "C"},
    {"amp": 40, "curve": "C"},
    {"amp": 50, "curve": "C"},
    {"amp": 63, "curve": "C"},
    {"amp": 63, "curve": "B"},
    {"amp": 50, "curve": "B"},
    {"amp": 40, "curve": "B"},
    {"amp": 32, "curve": "B"},
    {"amp": 25, "curve": "B"},
    {"amp": 20, "curve": "B"},
    {"amp": 16, "curve": "B"},
    {"amp": 10, "curve": "B"},
    {"amp": 6, "curve": "B"},
    {"amp": 4, "curve": "B"},
]

assert len(AUTHORED) == len(slugs), f"{len(AUTHORED)} authored vs {len(slugs)} slugs"

batch = []
for slug, a in zip(slugs, AUTHORED):
    pre = pre_by_slug[slug]
    batch.append({
        "slug": pre["slug"],
        "title": pre["title"],
        "excerpt_html": pre["excerpt_html"],
        "content_html": schneider4p_content(a["amp"], a["curve"]),
        "extra_specs": pre["extra_specs"],
        "category_name": "فیوز مینیاتوری",
        "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "",
                   "standard": SCHNEIDER_STD, "application": POLE_APP},
        "price": pre["price"],
        "datasheet_url": pre["datasheet_url"],
        "source_url": pre["source_url"],
    })

if __name__ == "__main__":
    body = json.dumps(batch, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=body,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "Mozilla/5.0"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=240) as resp:
        result = resp.read().decode("utf-8")
    with open(os.path.join(DATA_DIR, "batch14_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch14_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch14_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
