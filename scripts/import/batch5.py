# -*- coding: utf-8 -*-
"""Batch 5: 12 Schneider MCB variants (Multi9 C60N), hand-rewritten."""
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

MCB_STD = "IEC 60947-2، IEC 60898"

POLE_APP = {
    "دو پل": "حفاظت از مدارهای الکتریکی تک‌فاز در تابلوهای برق، ساختمان‌های مسکونی و تجاری",
    "سه پل": "حفاظت از مدارهای سه‌فاز در کارگاه‌ها، تابلوهای کنترل صنعتی و تجهیزات پرمصرف مانند موتورهای الکتریکی",
    "چهار پل": "حفاظت از مدارهای سه‌فاز به همراه نول در ساختمان‌های تجاری و صنعتی با نیاز به حفاظت کامل خط نول",
}


def mcb_content(amp, poles, curve):
    curve_desc = {
        "B": "برای مدارهای عمومی روشنایی و پریز با جریان راه‌اندازی پایین",
        "C": "برای مدارهایی با جریان هجومی راه‌اندازی متوسط مانند موتورها و تجهیزات القایی",
    }[curve]
    return f"""<p>کلید مینیاتوری {poles} {amp} آمپر کلاس {curve} اشنایدر از سری Multi9 (خانواده C60N) با تکنولوژی تریپ حرارتی-مغناطیسی، در برابر اضافه‌بار طولانی‌مدت و اتصال کوتاه ناگهانی محافظت می‌کند. ظرفیت قطع آن ۶ کیلوآمپر است و طول عمر مکانیکی آن تا ۲۰۰۰۰ سیکل عملکرد تست شده است.</p>
<p>منحنی قطع {curve} این کلید {curve_desc}. نصب آن روی ریل استاندارد DIN ساده است و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


AUTHORED = [
    {"amp": 6, "poles": "دو پل", "curve": "B"},
    {"amp": 25, "poles": "چهار پل", "curve": "C"},
    {"amp": 16, "poles": "چهار پل", "curve": "C"},
    {"amp": 63, "poles": "سه پل", "curve": "C"},
    {"amp": 20, "poles": "سه پل", "curve": "C"},
    {"amp": 16, "poles": "سه پل", "curve": "C"},
    {"amp": 10, "poles": "سه پل", "curve": "C"},
    {"amp": 4, "poles": "سه پل", "curve": "C"},
    {"amp": 63, "poles": "دو پل", "curve": "C"},
    {"amp": 50, "poles": "دو پل", "curve": "C"},
    {"amp": 40, "poles": "دو پل", "curve": "C"},
    {"amp": 32, "poles": "دو پل", "curve": "C"},
]

assert len(AUTHORED) == len(slugs), f"{len(AUTHORED)} authored vs {len(slugs)} slugs"

batch = []
for slug, a in zip(slugs, AUTHORED):
    pre = pre_by_slug[slug]
    batch.append({
        "slug": pre["slug"],
        "title": pre["title"],
        "excerpt_html": pre["excerpt_html"],
        "content_html": mcb_content(a["amp"], a["poles"], a["curve"]),
        "extra_specs": pre["extra_specs"],
        "category_name": "فیوز مینیاتوری",
        "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "",
                   "standard": MCB_STD, "application": POLE_APP[a["poles"]]},
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
    with urllib.request.urlopen(req, timeout=180) as resp:
        result = resp.read().decode("utf-8")
    with open(os.path.join(DATA_DIR, "batch5_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch5_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch5_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
