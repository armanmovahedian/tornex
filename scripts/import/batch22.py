# -*- coding: utf-8 -*-
"""Batch 22: 20 products -- Yaghout SIFGL (double-layer silicone+
fiberglass) and SIF (single-layer silicone) heat-resistant wires,
one Khorasan Afsharnejad NYMHY flexible cable, and five Khorasan
Afsharnejad NYA solid earth wires."""
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

KHORASAN_PARENT = "سیم و کابل خراسان افشارنژاد"
SIFGL_STD = "IEC 60228، IEC 61034-2، IEC 60754-1/2، IEC 60332-1-2، IEC 60245-1"
SIF_STD = "IEC 60228، IEC 61034-2، IEC 60754-1/2، IEC 60332-1-2"
SIFGL_APP = "سیم‌کشی داخلی تجهیزات صنعتی و کوره‌ها با دمای کاری بسیار بالا"
GROUND_WIRE_STD = "IEC 60227، ISIRI 607، DIN VDE 0271، IEC 60228"
GROUND_WIRE_APP = "سیم‌کشی ثابت اتصال زمین (ارت) در ساختمان‌های مسکونی، تجاری و صنعتی"
FLEX_APP = "سیم‌کشی داخلی ساختمان و تابلوهای برق با نیاز به چند رشته هم‌زمان (فاز، نول، ارت)"


def sifgl_content(size, tar_count, resistance, dia, weight_100m, tar_dia=None):
    tar_clause = f" (هر تار به قطر {tar_dia} میلی‌متر)" if tar_dia else ""
    res_clause = f" مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} اهم بر کیلومتر است." if resistance else ""
    return f"""<p>سیم سیلیکون دو روکش بافت {size} یاقوت (SIFGL) از هادی مس قلع‌اندود افشان کلاس ۵ ({tar_count} تار{tar_clause}) ساخته شده است. لایه داخلی سیلیکون رابر عایق‌بندی الکتریکی مطمئنی ایجاد می‌کند و لایه بیرونی بافته‌شده از فایبرگلاس، مقاومت حرارتی سیم را در بازه ۶۰- تا ۳۰۰+ درجه سانتی‌گراد تضمین می‌کند.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight_100m} در هر کلاف ۱۰۰ متری است.{res_clause} با ولتاژ نامی ۳۰۰/۵۰۰ ولت، تست ولتاژ ۲ کیلوولت را پاس کرده و مطابق IEC 60332-1-2 و IEC 60754-1/2 دود کم و بدون هالوژن تولید می‌کند. برای تجهیزات صنعتی و کوره‌های با دمای بالا مناسب است.</p>"""


def sif_content(size, tar_count, resistance, dia, weight, insulation, tar_dia=None):
    tar_clause = f" (هر تار به قطر {tar_dia} میلی‌متر)" if tar_dia else ""
    res_clause = f" مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است." if resistance else ""
    return f"""<p>سیم سیلیکون افشان تک‌روکش {size} یاقوت (SIF) از هادی مس قلع‌اندود افشان کلاس ۵ ({tar_count} تار{tar_clause}) ساخته شده است. عایق آن از سیلیکون رابر به ضخامت {insulation} میلی‌متر است که مقاومت حرارتی سیم را در بازه ۶۰- تا ۲۰۰+ درجه سانتی‌گراد تضمین می‌کند و در برابر گسترش شعله مطابق IEC 60332-1-2 مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است.{res_clause} با ولتاژ نامی ۳۰۰/۵۰۰ ولت، تست ولتاژ ۲ کیلوولت را پاس کرده و مطابق IEC 60754-1/2 دود کم و بدون هالوژن تولید می‌کند. برای سیم‌کشی داخلی تجهیزات صنعتی با دمای بالا مناسب است.</p>"""


def ground_wire_content(size, resistance, dia, weight, voltage, insulation):
    return f"""<p>سیم مفتول ارت {size} خراسان افشارنژاد (NYA) از هادی مسی تک‌رشته‌ای کلاس ۱ (مفتول) با عایق PVC به ضخامت {insulation} میلی‌متر و رنگ زرد-سبز استاندارد ارت ساخته شده است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است. با ولتاژ نامی {voltage} و تست ولتاژ ۲.۵ کیلوولت، عایق آن در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد دوام می‌آورد و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای سیم‌کشی ثابت اتصال زمین ساختمان‌ها مناسب است.</p>"""


RECORDS = [
    {  # 1 - SIFGL 10mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "10", "conductor_material": "مس قلع اندود",
                   "standard": SIFGL_STD, "application": SIFGL_APP},
        "content_html": sifgl_content("10", 77, "1.95", "7.5", "13 کیلوگرم"),
    },
    {  # 2 - Afsharnejad flexible cable 5x1 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x1", "conductor_material": "مس",
                   "standard": "IEC 60227-7، IEC 60228، ISIRI 607-5", "application": FLEX_APP},
        "content_html": """<p>کابل برق افشان ۵×۱ خراسان افشارنژاد (NYMHY) از پنج رشته هادی مسی افشان با رنگ‌بندی استاندارد (مشکی، قهوه‌ای، قرمز، آبی و زرد-سبز برای ارت) تشکیل شده و برای تامین برق سیستم‌های سه‌فاز همراه با نول و ارت مناسب است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد ۱۹.۵ اهم بر کیلومتر است و عایق آن تست ولتاژ ۲۰۰۰ ولت را پاس کرده است.</p>
<p>قطر کلی کابل ۸.۴۴ میلی‌متر و وزن آن حدود ۱۱۶ گرم بر متر است. با ولتاژ نامی ۳۰۰/۵۰۰ ولت، جریان اتصال کوتاه تا ۰.۱۱۱ کیلوآمپر را در یک ثانیه تحمل می‌کند و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است. در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و برای ساختمان‌ها، سیستم‌های صنعتی و تاسیسات برق مناسب است.</p>""",
    },
    {  # 3 - SIFGL 6mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "6", "conductor_material": "مس قلع اندود",
                   "standard": SIFGL_STD, "application": SIFGL_APP},
        "content_html": sifgl_content("6", 84, "3.39", "5.9", "8.3 کیلوگرم", tar_dia="0.282"),
    },
    {  # 4 - SIFGL 1.5mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "1.5", "conductor_material": "مس قلع اندود",
                   "standard": SIFGL_STD, "application": SIFGL_APP},
        "content_html": sifgl_content("1.5", 32, "13.7", "3.4", "2.4 کیلوگرم", tar_dia="0.227"),
    },
    {  # 5 - SIFGL 0.75mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "0.75", "conductor_material": "مس قلع اندود",
                   "standard": SIFGL_STD, "application": SIFGL_APP},
        "content_html": sifgl_content("0.75", 24, "26.7", "2.8", "1.4 کیلوگرم", tar_dia="0.186"),
    },
    {  # 6 - SIFGL 0.5mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "0.5", "conductor_material": "مس قلع اندود",
                   "standard": SIFGL_STD, "application": SIFGL_APP},
        "content_html": sifgl_content("0.5", 16, "40.1 میلی‌اهم بر متر", "2.8", "1.2 کیلوگرم", tar_dia="0.186"),
    },
    {  # 7 - SIFGL 0.35mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "0.35", "conductor_material": "مس قلع اندود",
                   "standard": SIFGL_STD, "application": SIFGL_APP},
        "content_html": sifgl_content("0.35", 7, None, "2.5", "۱.۹ کیلوگرم (کلاف ۲۰۰ متری)", tar_dia="0.231"),
    },
    {  # 8 - SIF 0.5mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "0.5", "conductor_material": "مس قلع اندود",
                   "standard": SIF_STD, "application": SIFGL_APP},
        "content_html": sif_content("0.5", 16, "40.1 میلی‌اهم بر متر", "2", "1.6 کیلوگرم (کلاف ۲۰۰ متری)", "0.6", tar_dia="0.186"),
    },
    {  # 9 - SIF 0.75mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "0.75", "conductor_material": "مس قلع اندود",
                   "standard": SIF_STD, "application": SIFGL_APP},
        "content_html": sif_content("0.75", 24, "26.7 میلی‌اهم بر متر", "2.25", "2 کیلوگرم (کلاف ۲۰۰ متری)", "0.6", tar_dia="0.186"),
    },
    {  # 10 - SIF 10mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "10", "conductor_material": "مس قلع اندود",
                   "standard": SIF_STD, "application": SIFGL_APP},
        "content_html": sif_content("10", 77, "1.95 اهم بر کیلومتر", "6.9", "11.3 کیلوگرم", "1", tar_dia="0.386"),
    },
    {  # 11 - SIF 6mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "6", "conductor_material": "مس قلع اندود",
                   "standard": SIF_STD, "application": SIFGL_APP},
        "content_html": sif_content("6", 84, "3.39 میلی‌اهم بر متر", "5.4", "7.4 کیلوگرم", "0.8", tar_dia="0.282"),
    },
    {  # 12 - SIF 4mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "4", "conductor_material": "مس قلع اندود",
                   "standard": SIF_STD, "application": SIFGL_APP},
        "content_html": sif_content("4", 56, None, "4.35", "4.8 کیلوگرم", "0.8", tar_dia="0.282"),
    },
    {  # 13 - SIF 2.5mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "2.5", "conductor_material": "مس قلع اندود",
                   "standard": SIF_STD, "application": SIFGL_APP},
        "content_html": sif_content("2.5", 52, "8.21 میلی‌اهم بر متر", "3.5", "مقداری متناسب با کلاف ۱۰۰ متری", "0.8", tar_dia="0.227"),
    },
    {  # 14 - SIF 1.5mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "1.5", "conductor_material": "مس قلع اندود",
                   "standard": SIF_STD, "application": SIFGL_APP},
        "content_html": sif_content("1.5", 32, "13.7 میلی‌اهم بر متر", "2.95", "1.95 کیلوگرم", "0.7", tar_dia="0.227"),
    },
    {  # 15 - SIF 0.25mm2
        "category_name": "سیم مقاوم در برابر حرارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "یاقوت", "size_diameter": "0.25", "conductor_material": "مس قلع اندود",
                   "standard": SIF_STD, "application": SIFGL_APP},
        "content_html": sif_content("0.25", 7, None, "1.6", "2.3 کیلوگرم (کلاف ۵۰۰ متری)", "0.4", tar_dia="0.195"),
    },
    {  # 16 - NYA ground wire 1mm2
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": ground_wire_content("۱", "۱۸.۱ اهم بر کیلومتر", "2.33", "1.3 کیلوگرم (کلاف ۱۰۰ متری)", "۳۰۰/۵۰۰ ولت", "0.6"),
    },
    {  # 17 - NYA ground wire 1.5mm2
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1.5", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": ground_wire_content("۱.۵", "۱۲.۱ اهم بر کیلومتر", "2.77", "1.9 کیلوگرم (کلاف)", "۴۵۰/۷۵۰ ولت", "0.7"),
    },
    {  # 18 - NYA ground wire 2.5mm2
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2.5", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": ground_wire_content("۲.۵", "۷.۴۱ اهم بر کیلومتر", "3.35", "3.1 کیلوگرم (کلاف ۱۰۰ متری)", "۴۵۰/۷۵۰ ولت", "0.8"),
    },
    {  # 19 - NYA ground wire 4mm2
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": ground_wire_content("۴", "۴.۶۱ اهم بر کیلومتر", "3.85", "4.5 کیلوگرم (کلاف)", "۴۵۰/۷۵۰ ولت", "0.8"),
    },
    {  # 20 - NYA ground wire 6mm2
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "6", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": ground_wire_content("۶", "۳.۰۸ اهم بر کیلومتر", "4.34", "6.4 کیلوگرم (کلاف)", "۴۵۰/۷۵۰ ولت", "0.8"),
    },
]

assert len(RECORDS) == len(slugs), f"{len(RECORDS)} authored vs {len(slugs)} slugs"

batch = []
for slug, r in zip(slugs, RECORDS):
    pre = pre_by_slug[slug]
    batch.append({
        "slug": pre["slug"],
        "title": pre["title"],
        "excerpt_html": pre["excerpt_html"],
        "content_html": r["content_html"],
        "extra_specs": pre["extra_specs"],
        "category_name": r["category_name"],
        "category_parent_name": r["category_parent_name"],
        "specs": r["specs"],
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
    with open(os.path.join(DATA_DIR, "batch22_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch22_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch22_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
