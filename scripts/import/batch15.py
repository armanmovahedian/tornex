# -*- coding: utf-8 -*-
"""Batch 15: 20 products -- Schneider Acti9 4-pole Curve B (1-3A)
and 3-pole Curve B/C (2-63A) MCBs."""
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

POLE_APP = {
    4: "حفاظت از مدارهای سه‌فاز به همراه نول در ساختمان‌های تجاری و صنعتی با نیاز به حفاظت کامل خط نول",
    3: "حفاظت از مدارهای سه‌فاز در ورودی آپارتمان‌ها، مصرف‌کننده‌های صنعتی و کولرهای گازی",
}

CURVE_DESC = {
    "C": "برای مدارهایی با جریان هجومی راه‌اندازی متوسط مانند موتورها و تجهیزات القایی",
    "B": "برای مدارهای عمومی روشنایی و پریز با جریان راه‌اندازی پایین",
}


def schneider_content(amp, poles, curve):
    curve_desc = CURVE_DESC[curve]
    if poles == 4:
        dims = "ارتفاع ۸۵ میلی‌متر، عرض ۷۲ میلی‌متر و عمق ۷۸.۵ میلی‌متر با وزن ۵۰۰ گرم"
        pole_fa = "چهار پل"
    else:
        dims = "ارتفاع ۸۵ میلی‌متر، عرض ۵۴ میلی‌متر و عمق ۷۸.۵ میلی‌متر با وزن ۳۷۵ گرم"
        pole_fa = "سه پل"
    return f"""<p>کلید مینیاتوری {pole_fa} {amp} آمپر کلاس {curve} اشنایدر از سری Acti9 با ولتاژ عایقی ۵۰۰ ولت و ولتاژ ضربه‌ای ۶ کیلوولت، ظرفیت قطع ۶ کیلوآمپر دارد و برای شبکه‌های AC و DC تا ۴۰۰ ولت مناسب است. منحنی قطع {curve} این کلید {curve_desc}.</p>
<p>این کلید با درجه حفاظت IP20، دوام مکانیکی ۲۰۰۰۰ سیکل و دوام الکتریکی ۱۰۰۰۰ سیکل تولید شده و در دمای کاری ۳۵- تا ۷۰+ درجه سانتی‌گراد (و نگهداری تا ۸۵+ درجه) کار می‌کند. ابعاد آن {dims} است. روی ریل DIN نصب می‌شود و ترمینال‌های آن سیم‌های مفتولی تا ۲۵ میلی‌متر مربع و سیم‌های نرم تا ۱۶ میلی‌متر مربع را می‌پذیرند.</p>"""


AUTHORED = [
    {"amp": 3, "poles": 4, "curve": "B"},
    {"amp": 2, "poles": 4, "curve": "B"},
    {"amp": 1, "poles": 4, "curve": "B"},
    {"amp": 63, "poles": 3, "curve": "C"},
    {"amp": 40, "poles": 3, "curve": "C"},
    {"amp": 25, "poles": 3, "curve": "C"},
    {"amp": 16, "poles": 3, "curve": "C"},
    {"amp": 10, "poles": 3, "curve": "C"},
    {"amp": 4, "poles": 3, "curve": "C"},
    {"amp": 2, "poles": 3, "curve": "C"},
    {"amp": 63, "poles": 3, "curve": "B"},
    {"amp": 50, "poles": 3, "curve": "B"},
    {"amp": 40, "poles": 3, "curve": "B"},
    {"amp": 32, "poles": 3, "curve": "B"},
    {"amp": 25, "poles": 3, "curve": "B"},
    {"amp": 20, "poles": 3, "curve": "B"},
    {"amp": 16, "poles": 3, "curve": "B"},
    {"amp": 10, "poles": 3, "curve": "B"},
    {"amp": 50, "poles": 3, "curve": "C"},
    {"amp": 32, "poles": 3, "curve": "C"},
]

assert len(AUTHORED) == len(slugs), f"{len(AUTHORED)} authored vs {len(slugs)} slugs"

batch = []
for slug, a in zip(slugs, AUTHORED):
    pre = pre_by_slug[slug]
    batch.append({
        "slug": pre["slug"],
        "title": pre["title"],
        "excerpt_html": pre["excerpt_html"],
        "content_html": schneider_content(a["amp"], a["poles"], a["curve"]),
        "extra_specs": pre["extra_specs"],
        "category_name": "فیوز مینیاتوری",
        "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "",
                   "standard": SCHNEIDER_STD, "application": POLE_APP[a["poles"]]},
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
    with open(os.path.join(DATA_DIR, "batch15_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch15_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch15_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
