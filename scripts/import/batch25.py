# -*- coding: utf-8 -*-
"""Batch 25: 20 products -- Khorasan Afsharnejad NYA general-purpose
colored wires (70-300mm2) and NA2XY aluminum cables (3.5-core and
single-core)."""
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
GENERAL_WIRE_APP = "سیم‌کشی ثابت عمومی در تاسیسات ساختمانی، تابلوهای برق و پست‌های توزیع"
AL_STD = "IEC 60502-1، ISIRI 3569-1، ISIRI 3084"
AL_MULTI_APP = "شبکه‌های توزیع برق فشار ضعیف سه‌فاز با نیاز به رسانای سبک‌تر و اقتصادی‌تر از مس"
AL_SINGLE_APP = "خطوط تغذیه اصلی و کابل‌کشی زمینی با جریان بالا، به‌عنوان جایگزین اقتصادی کابل مسی"


def nya_general_content(size, conductor_desc, resistance, dia, weight, insulation, voltage="450/750 ولت"):
    return f"""<p>سیم مفتول رنگی {size} خراسان افشارنژاد (NYA) از هادی مسی {conductor_desc} با عایق PVC به ضخامت {insulation} میلی‌متر ساخته شده و در رنگ‌های آبی، زرد، قرمز، سبز، قهوه‌ای، مشکی، طوسی یا رنگ سفارشی مشتری تولید می‌شود. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است. با ولتاژ نامی {voltage} و تست ولتاژ ۲.۵ کیلوولت، عایق آن در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد دوام می‌آورد و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای سیم‌کشی ثابت عمومی در تاسیسات ساختمانی، تابلوهای برق و پست‌های توزیع مناسب است.</p>"""


def al_multi_content(phase_mm2, neutral_mm2, phase_tar, phase_dia, neutral_tar, neutral_dia,
                      phase_ins, neutral_ins, sheath, dia, weight, sc_current, res_phase, res_neutral):
    return f"""<p>کابل آلومینیوم زمینی ۳×{phase_mm2}+{neutral_mm2} خراسان افشارنژاد (NA2XY) از سه رشته فاز با سطح مقطع {phase_mm2} میلی‌متر مربع ({phase_tar} تار به قطر {phase_dia} میلی‌متر) و یک رشته نول با سطح مقطع {neutral_mm2} میلی‌متر مربع ({neutral_tar} تار به قطر {neutral_dia} میلی‌متر) ساخته شده است. عایق XLPE فاز و نول به ترتیب {phase_ins} و {neutral_ins} میلی‌متر ضخامت دارد و نوار پلی‌استر (Pet-tape) شکل کابل را حفظ می‌کند.</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی فاز {res_phase} و نول {res_neutral} در دمای ۲۰ درجه سانتی‌گراد است. با ولتاژ نامی ۰.۶/۱ کیلوولت و تست ولتاژ ۴ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۵- تا ۹۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def al_single_content(size_mm2, tar_count, tar_dia, insulation, sheath, dia, weight, sc_current, resistance):
    return f"""<p>کابل آلومینیوم تک‌رشته {size_mm2} خراسان افشارنژاد (NA2XY) از هادی نیمه‌افشان کلاس ۲ گرد ({tar_count} تار به قطر {tar_dia} میلی‌متر) با عایق XLPE به ضخامت {insulation} میلی‌متر ساخته شده است. روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی ۰.۶/۱ کیلوولت و تست ولتاژ ۴ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۵- تا ۹۰+ درجه سانتی‌گراد کار می‌کند. برای خطوط تغذیه اصلی و کابل‌کشی زمینی با جریان بالا، به‌عنوان جایگزین اقتصادی کابل مسی مناسب است.</p>"""


RECORDS = [
    {  # 1 - NYA colored wire 70mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "70", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۷۰", "نیمه‌افشان کلاس ۲ (۱۹ تار به قطر ۲.۱۱ میلی‌متر)", "۰.۲۶۸ اهم بر کیلومتر", "مطابق دیتاشیت", "663 گرم بر متر", "1.4"),
    },
    {  # 2 - NYA colored wire 120mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "120", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۱۲۰", "نیمه‌افشان کلاس ۲ (۳۷ تار به قطر ۲ میلی‌متر)", "۰.۱۵۳ اهم بر کیلومتر", "17.2", "1175 گرم بر متر", "1.6"),
    },
    {  # 3 - NYA colored wire 300mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "300", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۳۰۰", "نیمه‌افشان کلاس ۲ (۶۱ تار به قطر ۲.۴۷ میلی‌متر)", "۰.۰۶۰۱ اهم بر کیلومتر", "27.25", "2916 گرم بر متر", "2.4"),
    },
    {  # 4 - NYA colored wire 240mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "240", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۲۴۰", "نیمه‌افشان کلاس ۲ (۶۱ تار به قطر ۲.۲ میلی‌متر)", "۰.۰۷۵۴ اهم بر کیلومتر", "24.2", "2.3 کیلوگرم بر متر", "2.2"),
    },
    {  # 5 - NYA colored wire 185mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "185", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۱۸۵", "نیمه‌افشان کلاس ۲ (۳۷ تار به قطر ۲.۴۷ میلی‌متر)", "۰.۰۹۹۱ اهم بر کیلومتر", "21.3", "1804 گرم بر متر", "2.0"),
    },
    {  # 6 - NYA colored wire 150mm2
        "category_name": "سیم مفتول رنگی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "150", "conductor_material": "مس",
                   "standard": GROUND_WIRE_STD, "application": GENERAL_WIRE_APP},
        "content_html": nya_general_content("۱۵۰", "نیمه‌افشان کلاس ۲ (۳۷ تار به قطر ۲.۲ میلی‌متر)", "۰.۱۲۴ اهم بر کیلومتر", "19", "1436 گرم بر متر", "1.8"),
    },
    {  # 7 - Aluminum 3x240+120
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x240+120", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_MULTI_APP},
        "content_html": al_multi_content("240", "120", "61", "2.23", "37", "2.02", "مطابق دیتاشیت", "مطابق دیتاشیت", "2.6", "51.4", "3332 کیلوگرم بر کیلومتر", "10 کیلوآمپر", "0.125 اهم بر کیلومتر", "0.253 اهم بر کیلومتر"),
    },
    {  # 8 - Aluminum 3x185+95
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x185+95", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_MULTI_APP},
        "content_html": al_multi_content("185", "95", "37", "2.52", "19", "2.52", "1.6", "1.1", "2.5", "45.2", "2626 کیلوگرم بر کیلومتر", "7.6 کیلوآمپر", "مطابق دیتاشیت", "مطابق دیتاشیت"),
    },
    {  # 9 - Aluminum 3x150+70
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x150+70", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_MULTI_APP},
        "content_html": al_multi_content("150", "70", "37", "2.23", "19", "2.14", "1.4", "1.1", "مطابق دیتاشیت", "مطابق دیتاشیت", "2100 کیلوگرم بر کیلومتر", "6.3 کیلوآمپر", "مطابق دیتاشیت", "مطابق دیتاشیت"),
    },
    {  # 10 - Aluminum 3x120+70
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x120+70", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_MULTI_APP},
        "content_html": al_multi_content("120", "70", "37", "2.02", "19", "2.14", "مطابق دیتاشیت", "مطابق دیتاشیت", "2.2", "37.2", "1762 کیلوگرم بر کیلومتر", "5 کیلوآمپر", "مطابق دیتاشیت", "مطابق دیتاشیت"),
    },
    {  # 11 - Aluminum 3x95+50
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x95+50", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_MULTI_APP},
        "content_html": al_multi_content("95", "50", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.1", "1.0", "2.1", "33.8", "1403 کیلوگرم بر کیلومتر", "3.9 کیلوآمپر", "0.320 اهم بر کیلومتر", "0.641 اهم بر کیلومتر"),
    },
    {  # 12 - Aluminum 3x70+35
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x70+35", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_MULTI_APP},
        "content_html": al_multi_content("70", "35", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.1", "0.9", "1.9", "مطابق دیتاشیت", "1.063 کیلوگرم بر متر", "2.9 کیلوآمپر", "مطابق دیتاشیت", "مطابق دیتاشیت"),
    },
    {  # 13 - Aluminum 3x35+16
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x35+16", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_MULTI_APP},
        "content_html": al_multi_content("35", "16", "7", "2.45", "7", "1.66", "0.9", "0.7", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.45 کیلوآمپر", "0.868 اهم بر کیلومتر", "1.91 اهم بر کیلومتر"),
    },
    {  # 14 - Aluminum 3x25+16
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x25+16", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_MULTI_APP},
        "content_html": al_multi_content("25", "16", "7", "2.09", "7", "1.66", "0.9", "0.7", "1.8", "مطابق دیتاشیت", "مطابق دیتاشیت", "1 کیلوآمپر", "1.2 اهم بر کیلومتر", "1.91 اهم بر کیلومتر"),
    },
    {  # 15 - Aluminum 1x500
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x500", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_SINGLE_APP},
        "content_html": al_single_content("500", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "36.75", "1.835 کیلوگرم بر متر", "21 کیلوآمپر", "0.0605 اهم بر کیلومتر"),
    },
    {  # 16 - Aluminum 1x400
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x400", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_SINGLE_APP},
        "content_html": al_single_content("400", "61", "2.78", "2.0", "1.9", "32.9", "1455 کیلوگرم بر کیلومتر", "16 کیلوآمپر", "0.0778 اهم بر کیلومتر"),
    },
    {  # 17 - Aluminum 1x240
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x240", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_SINGLE_APP},
        "content_html": al_single_content("240", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.7", "مطابق دیتاشیت", "26.5", "939 کیلوگرم بر کیلومتر", "9.9 کیلوآمپر", "مطابق دیتاشیت"),
    },
    {  # 18 - Aluminum 1x300
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x300", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_SINGLE_APP},
        "content_html": al_single_content("300", "61", "2.45", "مطابق دیتاشیت", "1.8", "29.3", "1150 کیلوگرم بر کیلومتر", "12.2 کیلوآمپر", "0.1 اهم بر کیلومتر"),
    },
    {  # 19 - Aluminum 1x185
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x185", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_SINGLE_APP},
        "content_html": al_single_content("185", "37", "2.45", "1.6", "1.6", "23.6", "737 کیلوگرم بر کیلومتر", "7.1 کیلوآمپر", "0.164 اهم بر کیلومتر"),
    },
    {  # 20 - Aluminum 1x150
        "category_name": "کابل آلومینیوم", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x150", "conductor_material": "آلومینیوم",
                   "standard": AL_STD, "application": AL_SINGLE_APP},
        "content_html": al_single_content("150", "37", "2.19", "1.4", "1.6", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "0.206 اهم بر کیلومتر"),
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
    with open(os.path.join(DATA_DIR, "batch25_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch25_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch25_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
