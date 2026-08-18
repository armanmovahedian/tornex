# -*- coding: utf-8 -*-
"""Batch 23: 20 products -- Khorasan Afsharnejad NYA (solid/semi-
stranded) and NYAF (stranded, class 5) earth wires across sizes
1-185mm2."""
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
GROUND_WIRE_STD = "IEC 60227، ISIRI 607، DIN VDE 0271، IEC 60228"
GROUND_WIRE_STD_AF = "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228"
GROUND_WIRE_APP = "سیم‌کشی اتصال زمین (ارت) در ساختمان‌های مسکونی، تجاری و صنعتی"


def nya_content(size, conductor_desc, resistance, dia, weight, insulation, voltage="450/750 ولت"):
    return f"""<p>سیم ارت {size} خراسان افشارنژاد (NYA) از هادی مسی {conductor_desc} با عایق PVC به ضخامت {insulation} میلی‌متر و رنگ زرد-سبز استاندارد ارت ساخته شده است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است. با ولتاژ نامی {voltage} و تست ولتاژ ۲.۵ کیلوولت، عایق آن در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد دوام می‌آورد و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای سیم‌کشی اتصال زمین ساختمان‌ها و تاسیسات صنعتی مناسب است.</p>"""


def nyaf_content(size, tar_count, resistance, dia, weight, insulation, voltage="450/750 ولت", tar_dia=None):
    tar_clause = f" به قطر {tar_dia} میلی‌متر" if tar_dia else ""
    res_clause = f" مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است." if resistance else ""
    return f"""<p>سیم ارت افشان {size} خراسان افشارنژاد (NYAF) از هادی مسی آنیل‌شده افشان کلاس ۵ ({tar_count} تار{tar_clause}) با عایق PVC به ضخامت {insulation} میلی‌متر و رنگ زرد-سبز استاندارد ارت ساخته شده است. ساختار افشان انعطاف‌پذیری بالایی در نصب مسیرهای پرپیچ‌وخم و داخل لوله‌ها فراهم می‌کند و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است.{res_clause} با ولتاژ نامی {voltage} و تست ولتاژ ۲.۵ کیلوولت، عایق آن در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد دوام می‌آورد و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای سیستم‌های ارتینگ ساختمان‌ها، تابلوهای برق و تجهیزات صنعتی مناسب است.</p>"""


RECORDS = [
    {  # 1 - NYA 10mm2 (class1 solid)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "10", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۱۰", "تک‌رشته‌ای کلاس ۱ (مفتول) به قطر ۳.۵۲ میلی‌متر", "۱.۸۳ اهم بر کیلومتر", "5.52", "10.7 کیلوگرم (کلاف)", "1.0"),
    },
    {  # 2 - NYA 16mm2 (class2, 7 tar 1.68mm)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "16", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۱۶", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۱.۶۸ میلی‌متر)", "۱.۱۵ اهم بر کیلومتر", "7.04", "167 گرم بر متر", "1.0"),
    },
    {  # 3 - NYA 25mm2 (class2, 7 tar 2.1mm)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "25", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۲۵", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۱ میلی‌متر)", "۰.۷۲۷ اهم بر کیلومتر", "8.7", "مقداری متناسب با کلاف", "1.2"),
    },
    {  # 4 - NYA 35mm2 (class2, 7 tar 2.47mm)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "35", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۳۵", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۴۷ میلی‌متر)", "۰.۵۲۴ اهم بر کیلومتر", "مطابق دیتاشیت", "344 گرم بر متر", "1.2"),
    },
    {  # 5 - NYAF 1mm2 (300/500V)
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۱", "32", "۱۹.۴۸۷ اهم بر کیلومتر", "مطابق دیتاشیت", "1.36 کیلوگرم (کلاف)", "0.6", voltage="۳۰۰/۵۰۰ ولت"),
    },
    {  # 6 - NYAF 1.5mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1.5", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۱.۵", "30", "۱۳.۳۰ اهم بر کیلومتر", "2.92", "مقداری متناسب با کلاف", "0.7", tar_dia="0.24"),
    },
    {  # 7 - NYAF 2.5mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2.5", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۲.۵", "50", None, "3.57", "3.1 کیلوگرم (کلاف ۱۰۰ متری)", "0.8", tar_dia="0.24"),
    },
    {  # 8 - NYA 50mm2 (class2, 19 tar 1.75mm)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "50", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۵۰", "نیمه‌افشان کلاس ۲ (۱۹ تار به قطر ۱.۷۵ میلی‌متر)", "۰.۳۸۷ اهم بر کیلومتر", "11.55", "480 گرم بر متر", "1.4"),
    },
    {  # 9 - NYA 70mm2 (class2, 19 tar 2.11mm)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "70", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۷۰", "نیمه‌افشان کلاس ۲ (۱۹ تار به قطر ۲.۱۱ میلی‌متر)", "۰.۲۶۸ اهم بر کیلومتر", "13.35", "663 گرم بر متر", "1.4"),
    },
    {  # 10 - NYA 95mm2 (class2, 19 tar)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "95", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۹۵", "نیمه‌افشان کلاس ۲ (۱۹ تار)", "۰.۱۹۳ اهم بر کیلومتر", "15.55", "914 گرم بر متر", "1.6"),
    },
    {  # 11 - NYA 120mm2 (class2, 37 tar 2mm)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "120", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۱۲۰", "نیمه‌افشان کلاس ۲ (۳۷ تار به قطر ۲ میلی‌متر)", "۰.۱۵۳ اهم بر کیلومتر", "17.2", "1.1 کیلوگرم بر متر", "1.6"),
    },
    {  # 12 - NYAF 4mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۴", "56", "۴.۹۵ اهم بر کیلومتر", "مطابق دیتاشیت", "مقداری متناسب با کلاف", "0.8", tar_dia="0.29"),
    },
    {  # 13 - NYAF 6mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "6", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۶", "84", "۳.۳۰ اهم بر کیلومتر", "4.71", "6.3 کیلوگرم (کلاف ۱۰۰ متری)", "0.8", tar_dia="0.29"),
    },
    {  # 14 - NYAF 10mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "10", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۱۰", "80", None, "6.1", "مقداری متناسب با کلاف", "1.0", tar_dia="0.39"),
    },
    {  # 15 - NYA 150mm2 (class2, 37 tar 2.2mm)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "150", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۱۵۰", "نیمه‌افشان کلاس ۲ (۳۷ تار به قطر ۲.۲ میلی‌متر)", "۰.۱۲۴ اهم بر کیلومتر", "19", "1.436 کیلوگرم بر متر", "1.8"),
    },
    {  # 16 - NYAF 16mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "16", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۱۶", "126", "۱.۲۱ اهم بر کیلومتر", "مطابق دیتاشیت", "مقداری متناسب با کلاف", "1.0", tar_dia="0.39"),
    },
    {  # 17 - NYAF 25mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "25", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۲۵", "189", "۰.۷۸ اهم بر کیلومتر", "9.2", "25.4 کیلوگرم (کلاف ۱۰۰ متری)", "1.2", tar_dia="0.39"),
    },
    {  # 18 - NYAF 35mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "35", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۳۵", "266", None, "10.4", "مقداری متناسب با کلاف", "1.2", tar_dia="0.39"),
    },
    {  # 19 - NYAF 50mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "50", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۵۰", "384", "۰.۳۸۶ اهم بر کیلومتر", "12.4", "495 گرم بر متر", "1.4", tar_dia="0.39"),
    },
    {  # 20 - NYA 185mm2 (class2, 37 tar)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "185", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("۱۸۵", "نیمه‌افشان کلاس ۲ (۳۷ تار)", "مطابق دیتاشیت", "21.3", "1.8 کیلوگرم بر متر", "2.0"),
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
    with open(os.path.join(DATA_DIR, "batch23_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch23_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch23_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
