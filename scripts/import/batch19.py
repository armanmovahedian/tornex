# -*- coding: utf-8 -*-
"""Batch 19: 20 products -- Schneider Multi9 C60N MCBs (1/2/3/4-pole,
Curve B/C, 2-50A)."""
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

MULTI9_STD = "EN 60947-2، IEC 60947-2، IEC 60898"

POLE_APP = {
    1: "حفاظت از مدارهای تک‌فاز روشنایی و پریز در ساختمان‌های مسکونی و تجاری",
    2: "حفاظت از مدارهای الکتریکی تک‌فاز در تابلوهای برق، ساختمان‌های مسکونی و تجاری",
    3: "حفاظت از مدارهای سه‌فاز در ورودی آپارتمان‌ها، مصرف‌کننده‌های صنعتی و کولرهای گازی",
    4: "حفاظت از مدارهای سه‌فاز به همراه نول در ساختمان‌های تجاری و صنعتی با نیاز به حفاظت کامل خط نول",
}

CURVE_DESC = {
    "C": "برای مدارهایی با جریان هجومی راه‌اندازی متوسط مانند موتورها و تجهیزات القایی",
    "B": "برای مدارهای عمومی روشنایی و پریز با جریان راه‌اندازی پایین",
}

POLE_WIDTH = {1: "18", 2: "36", 3: "54", 4: "72"}
POLE_WEIGHT = {1: "120", 2: "240", 3: "360", 4: "480"}
POLE_FA = {1: "تک پل", 2: "دو پل", 3: "سه پل", 4: "چهار پل"}


def multi9_content(amp, poles, curve):
    curve_desc = CURVE_DESC[curve]
    return f"""<p>کلید مینیاتوری {POLE_FA[poles]} {amp} آمپر کلاس {curve} اشنایدر از سری Multi9 (خانواده C60N) با تکنولوژی تریپ حرارتی-مغناطیسی، در برابر اضافه‌بار طولانی‌مدت و اتصال کوتاه ناگهانی محافظت می‌کند. ظرفیت قطع آن ۶ کیلوآمپر است و منحنی قطع {curve} این کلید {curve_desc}.</p>
<p>نصب آن روی ریل استاندارد DIN (۳۵ میلی‌متری) ساده است. ابعاد آن ارتفاع ۸۱ میلی‌متر، عرض {POLE_WIDTH[poles]} میلی‌متر و عمق ۷۳ میلی‌متر با وزن {POLE_WEIGHT[poles]} گرم است و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد (نگهداری تا ۴۰- تا ۷۰+ درجه) کار می‌کند.</p>"""


AUTHORED = [
    {"amp": 32, "poles": 4, "curve": "C"},
    {"amp": 25, "poles": 3, "curve": "C"},
    {"amp": 6, "poles": 3, "curve": "C"},
    {"amp": 2, "poles": 3, "curve": "C"},
    {"amp": 20, "poles": 2, "curve": "C"},
    {"amp": 40, "poles": 4, "curve": "C"},
    {"amp": 50, "poles": 3, "curve": "C"},
    {"amp": 40, "poles": 3, "curve": "C"},
    {"amp": 32, "poles": 3, "curve": "C"},
    {"amp": 16, "poles": 2, "curve": "C"},
    {"amp": 10, "poles": 2, "curve": "C"},
    {"amp": 6, "poles": 2, "curve": "C"},
    {"amp": 32, "poles": 1, "curve": "B"},
    {"amp": 25, "poles": 1, "curve": "B"},
    {"amp": 20, "poles": 1, "curve": "B"},
    {"amp": 16, "poles": 1, "curve": "B"},
    {"amp": 10, "poles": 1, "curve": "B"},
    {"amp": 6, "poles": 1, "curve": "B"},
    {"amp": 20, "poles": 1, "curve": "C"},
    {"amp": 16, "poles": 1, "curve": "C"},
]

assert len(AUTHORED) == len(slugs), f"{len(AUTHORED)} authored vs {len(slugs)} slugs"

batch = []
for slug, a in zip(slugs, AUTHORED):
    pre = pre_by_slug[slug]
    batch.append({
        "slug": pre["slug"],
        "title": pre["title"],
        "excerpt_html": pre["excerpt_html"],
        "content_html": multi9_content(a["amp"], a["poles"], a["curve"]),
        "extra_specs": pre["extra_specs"],
        "category_name": "فیوز مینیاتوری",
        "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "",
                   "standard": MULTI9_STD, "application": POLE_APP[a["poles"]]},
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
    with open(os.path.join(DATA_DIR, "batch19_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch19_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch19_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
