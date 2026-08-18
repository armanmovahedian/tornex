# -*- coding: utf-8 -*-
"""Batch 24: 20 products -- Khorasan Afsharnejad NYA/NYAF earth wires
(sizes 70-300mm2) and NYA general-purpose colored solid/semi-stranded
wires (sizes 1-95mm2)."""
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
GENERAL_WIRE_APP = "سیم‌کشی ثابت عمومی در تاسیسات ساختمانی، تابلوهای برق و پست‌های توزیع"


def nya_content(size, conductor_desc, resistance, dia, weight, insulation, voltage="450/750 ولت", app=GROUND_WIRE_APP):
    tail = "برای سیم‌کشی اتصال زمین ساختمان‌ها و تاسیسات صنعتی مناسب است." if app is GROUND_WIRE_APP else "برای سیم‌کشی ثابت عمومی در تاسیسات ساختمانی و تابلوهای برق مناسب است."
    return f"""<p>سیم {"ارت " if app is GROUND_WIRE_APP else ""}{size} خراسان افشارنژاد (NYA) از هادی مسی {conductor_desc} با عایق PVC به ضخامت {insulation} میلی‌متر ساخته شده است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است. با ولتاژ نامی {voltage} و تست ولتاژ ۲.۵ کیلوولت، عایق آن در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد دوام می‌آورد و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. {tail}</p>"""


def nyaf_content(size, tar_count, resistance, dia, weight, insulation, voltage="450/750 ولت", tar_dia=None):
    tar_clause = f" به قطر {tar_dia} میلی‌متر" if tar_dia else ""
    res_clause = f" مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است." if resistance else ""
    return f"""<p>سیم ارت افشان {size} خراسان افشارنژاد (NYAF) از هادی مسی آنیل‌شده افشان کلاس ۵ ({tar_count} تار{tar_clause}) با عایق PVC به ضخامت {insulation} میلی‌متر و رنگ زرد-سبز استاندارد ارت ساخته شده است. ساختار افشان انعطاف‌پذیری بالایی در نصب مسیرهای پرپیچ‌وخم فراهم می‌کند و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است.{res_clause} با ولتاژ نامی {voltage} و تست ولتاژ ۲.۵ کیلوولت، عایق آن در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد دوام می‌آورد و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای سیستم‌های ارتینگ ساختمان‌ها، تابلوهای برق و تجهیزات صنعتی مناسب است.</p>"""


def nya_general_content(size, conductor_desc, resistance, dia, weight, insulation, voltage="450/750 ولت"):
    return f"""<p>سیم مفتول رنگی {size} خراسان افشارنژاد (NYA) از هادی مسی {conductor_desc} با عایق PVC به ضخامت {insulation} میلی‌متر ساخته شده و در رنگ‌های آبی، زرد، قرمز، سبز، قهوه‌ای، مشکی، طوسی یا رنگ سفارشی مشتری تولید می‌شود. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است. با ولتاژ نامی {voltage} و تست ولتاژ ۲.۵ کیلوولت، عایق آن در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد دوام می‌آورد و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای سیم‌کشی ثابت عمومی در تاسیسات ساختمانی، تابلوهای برق و پست‌های توزیع مناسب است.</p>"""


RECORDS = [
    {  # 1 - NYA 240mm2 earth (class2, 61 tar 2.2mm)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "240", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("ارت ۲۴۰", "نیمه‌افشان کلاس ۲ (۶۱ تار به قطر ۲.۲ میلی‌متر)", "۰.۰۷۵۴ اهم بر کیلومتر", "24.2", "2.3 کیلوگرم بر متر", "2.2"),
    },
    {  # 2 - NYAF 70mm2 earth
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "70", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۷۰", "350", "۰.۲۷۲ اهم بر کیلومتر", "14.4", "مقداری متناسب با کلاف", "1.4", tar_dia="0.49"),
    },
    {  # 3 - NYAF 95mm2 earth
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "95", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۹۵", "456", "۰.۲۰۶ اهم بر کیلومتر", "16.7", "913 گرم بر متر", "1.6", tar_dia="0.49"),
    },
    {  # 4 - NYAF 120mm2 earth
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "120", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۱۲۰", "570", "۰.۱۶۱ اهم بر کیلومتر", "مطابق دیتاشیت", "مقداری متناسب با کلاف", "1.6", tar_dia="0.49"),
    },
    {  # 5 - NYAF 240mm2 earth
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "240", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۲۴۰", "1170", "۰.۰۸۰۱ اهم بر کیلومتر", "25.4", "2.253 کیلوگرم بر متر", "2.2", tar_dia="0.49"),
    },
    {  # 6 - NYAF 185mm2 earth
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "185", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۱۸۵", "875", "۰.۱۰۶ اهم بر کیلومتر", "مطابق دیتاشیت", "مقداری متناسب با کلاف", "2.0", tar_dia="0.49"),
    },
    {  # 7 - NYAF 150mm2 earth
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "150", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۱۵۰", "722", None, "20.1", "1.4 کیلوگرم بر متر", "1.8", tar_dia="0.49"),
    },
    {  # 8 - NYAF 300mm2 earth
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "300", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD_AF, "application": GROUND_WIRE_APP},
        "content_html": nyaf_content("۳۰۰", "1480", "۰.۰۶۴۱ اهم بر کیلومتر", "28.2", "مقداری متناسب با کلاف", "2.4", tar_dia="0.49"),
    },
    {  # 9 - NYA 300mm2 earth (class2, 61 tar 2.47mm)
        "category_name": "سیم مفتول ارت", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "300", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GROUND_WIRE_APP},
        "content_html": nya_content("ارت ۳۰۰", "نیمه‌افشان کلاس ۲ (۶۱ تار به قطر ۲.۴۷ میلی‌متر)", "۰.۰۶۰۱ اهم بر کیلومتر", "27.25", "3 کیلوگرم بر متر", "2.4"),
    },
    {  # 10 - NYA colored wire 1.5mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1.5", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۱.۵", "تک‌رشته‌ای کلاس ۱ (مفتول)", "۱۲.۱ اهم بر کیلومتر", "مطابق دیتاشیت", "19.8 گرم بر متر", "0.7"),
    },
    {  # 11 - NYA colored wire 1mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۱", "تک‌رشته‌ای کلاس ۱ (مفتول)", "۱۸.۱ اهم بر کیلومتر", "مطابق دیتاشیت", "مقداری متناسب با کلاف", "0.6", voltage="۳۰۰/۵۰۰ ولت"),
    },
    {  # 12 - NYA colored wire 2.5mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2.5", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۲.۵", "تک‌رشته‌ای کلاس ۱ (مفتول)", "۷.۴۱ اهم بر کیلومتر", "3.35", "31 گرم بر متر", "0.8"),
    },
    {  # 13 - NYA colored wire 4mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۴", "تک‌رشته‌ای کلاس ۱ (مفتول)", "۴.۶۱ اهم بر کیلومتر", "3.85", "45.5 گرم بر متر", "0.8"),
    },
    {  # 14 - NYA colored wire 6mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "6", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۶", "تک‌رشته‌ای کلاس ۱ (مفتول)", "۳.۰۸ اهم بر کیلومتر", "4.34", "64.3 گرم بر متر", "0.8"),
    },
    {  # 15 - NYA colored wire 10mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "10", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۱۰", "تک‌رشته‌ای کلاس ۱ (مفتول) به قطر ۳.۵۲ میلی‌متر", "۱.۸۳ اهم بر کیلومتر", "5.52", "مقداری متناسب با کلاف", "1.0"),
    },
    {  # 16 - NYA colored wire 16mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "16", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۱۶", "نیمه‌افشان کلاس ۲ (۷ تار)", "۱.۱۵ اهم بر کیلومتر", "7.04", "167.5 گرم بر متر", "1.0"),
    },
    {  # 17 - NYA colored wire 25mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "25", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۲۵", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۱ میلی‌متر)", "۰.۷۲۷ اهم بر کیلومتر", "8.7", "263 گرم بر متر", "1.2"),
    },
    {  # 18 - NYA colored wire 35mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "35", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۳۵", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۴۷ میلی‌متر)", "۰.۵۲۴ اهم بر کیلومتر", "مطابق دیتاشیت", "344 گرم بر متر", "1.2"),
    },
    {  # 19 - NYA colored wire 95mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "95", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۹۵", "نیمه‌افشان کلاس ۲ (۱۹ تار)", "۰.۱۹۳ اهم بر کیلومتر", "15.55", "914 گرم بر متر", "1.6"),
    },
    {  # 20 - NYA colored wire 50mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "50", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۵۰", "نیمه‌افشان کلاس ۲ (۱۹ تار به قطر ۱.۷۵ میلی‌متر)", "۰.۳۸۷ اهم بر کیلومتر", "11.55", "480 گرم بر متر", "1.4"),
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
    with open(os.path.join(DATA_DIR, "batch24_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch24_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch24_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
