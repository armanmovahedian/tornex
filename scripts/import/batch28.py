# -*- coding: utf-8 -*-
"""Batch 28: 20 products -- 6 more NYSLCY shielded cables (3x2.5,
3x1.5, 3x1, 2x2.5, 2x1.5, 2x1), 11 NYY Flexible single-core cables
(1x300 down to 1x16), 3 JY(st)Y telephone cables (10/6/4-pair 0.6mm),
all Khorasan Afsharnejad."""
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


def nyslcy_content(cores_label, size_mm2, tar_count, tar_dia, ins_thickness, sheath, dia, weight, resistance, sc_current, colors):
    return f"""<p>کابل شیلددار افشان {cores_label} خراسان افشارنژاد (NYSLCY) با سطح مقطع {size_mm2} میلی‌متر مربع برای هر رشته، از هادی مسی افشان کلاس ۵ ({tar_count} تار به قطر {tar_dia} میلی‌متر) با عایق PVC به ضخامت {ins_thickness} میلی‌متر ساخته شده است. رنگ‌بندی رشته‌ها ({colors}) شناسایی و نصب دقیق را تسهیل می‌کند. زیر روکش نهایی، شیلد مسی بافته‌شده همراه با نوار آلومینیوم و پلی‌استر هر یک به ضخامت ۰.۰۳۶ میلی‌متر، محافظت کاملی در برابر تداخل الکترومغناطیسی فراهم می‌کند.</p>
<p>روکش نهایی PVC طوسی به ضخامت {sheath} میلی‌متر است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با تست ولتاژ ۲ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای سیم‌کشی کنترل و فرمان در محیط‌های نویزی مناسب است.</p>"""


def nyy_flex_content(size_mm2, tar_count, tar_dia, ins_thickness, sheath, dia, weight, sc_current, resistance):
    return f"""<p>کابل افشان تک‌رشته {size_mm2} خراسان افشارنژاد (NYY Flexible) از هادی مسی آنیل‌شده افشان کلاس ۵ ({tar_count} تار به قطر {tar_dia} میلی‌متر) با عایق PVC به ضخامت {ins_thickness} میلی‌متر ساخته شده که انعطاف‌پذیری بالایی برای نصب در مسیرهای پیچیده و تجهیزات متحرک صنعتی دارد. روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است.</p>
<p>قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت و تست ولتاژ ۴ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای اتصال تجهیزات صنعتی سنگین و متحرک مناسب است.</p>"""


def telephone_content(pairs, resistance, weight, dia, colors):
    return f"""<p>کابل تلفن {pairs} زوج ۰.۶ خراسان افشارنژاد (ساختار JY(st)Y) از هادی مسی آنیل‌شده مفتولی کلاس ۱ به قطر ۰.۶ میلی‌متر ساخته شده و هر دو رشته به‌صورت زوج به‌هم‌تابیده‌اند تا نویز الکترومغناطیسی و تداخل بین زوج‌ها کاهش یابد. عایق هر رشته از PVC به ضخامت ۰.۲ میلی‌متر است و رنگ‌بندی زوج‌ها ({colors}) شناسایی مدارها را ساده می‌کند. دور کل رشته‌ها یک شیلد ترکیبی از فویل آلومینیوم، نوار پلی‌استر و سیم تخلیه قلع‌اندود قرار دارد که محافظت در برابر نویز را افزایش می‌دهد.</p>
<p>روکش نهایی PVC خاکستری به ضخامت ۱ میلی‌متر است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد حداکثر {resistance} است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. با حداکثر ولتاژ کاری ۳۰۰ ولت DC و تست ولتاژ ۲ کیلوولت، مطابق استانداردهای IEC 60189 و VDE 0815 تولید شده و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای سیم‌کشی تلفن ثابت و شبکه‌های مخابراتی داخلی ساختمان‌ها مناسب است.</p>"""


RECORDS = [
    {  # 1 - NYSLCY 3x2.5
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x2.5", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "اتوماسیون صنعتی، تابلوهای فرمان و ماشین‌آلات در محیط‌های دارای میدان مغناطیسی"},
        "content_html": nyslcy_content("۳×۲.۵", "2.5", "مطابق دیتاشیت", "مطابق دیتاشیت", "0.8", "1.1", "10.34", "مطابق دیتاشیت", "مطابق دیتاشیت", "0.2 کیلوآمپر", "فاز: مشکی؛ نول: آبی؛ ارت: زرد/سبز"),
    },
    {  # 2 - NYSLCY 3x1.5
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x1.5", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "سیم‌کشی کنترل و فرمان در محیط‌های نویزی"},
        "content_html": nyslcy_content("۳×۱.۵", "1.5", "30", "0.24", "0.7", "1.1", "8.72", "108 گرم بر متر", "13.30 اهم بر کیلومتر", "0.2 کیلوآمپر", "فاز: مشکی؛ نول: آبی"),
    },
    {  # 3 - NYSLCY 3x1
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x1", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "کنترل ابزار دقیق در محیط‌های صنعتی با نویز"},
        "content_html": nyslcy_content("۳×۱", "1", "32", "0.19", "0.6", "1", "7.74", "85 گرم بر متر", "19.5 اهم بر کیلومتر", "0.2 کیلوآمپر", "فاز: مشکی؛ نول: آبی؛ ارت: زرد/سبز"),
    },
    {  # 4 - NYSLCY 2x2.5
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x2.5", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "سیم‌کشی کنترل و فرمان تک‌فاز در محیط‌های نویزی"},
        "content_html": nyslcy_content("۲×۲.۵", "2.5", "50", "0.24", "0.8", "1", "9.6", "117 گرم بر متر", "7.98 اهم بر کیلومتر", "مطابق دیتاشیت", "فاز و نول (رنگ‌بندی استاندارد طوسی)"),
    },
    {  # 5 - NYSLCY 2x1.5
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x1.5", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "سیم‌کشی کنترل و فرمان تک‌فاز در محیط‌های نویزی"},
        "content_html": nyslcy_content("۲×۱.۵", "1.5", "30", "0.24", "0.7", "1", "8.3", "85 گرم بر متر", "13.3 اهم بر کیلومتر", "0.2 کیلوآمپر", "فاز و نول (رنگ‌بندی استاندارد طوسی)"),
    },
    {  # 6 - NYSLCY 2x1
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x1", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "سیم‌کشی کنترل و فرمان تک‌فاز در محیط‌های نویزی"},
        "content_html": nyslcy_content("۲×۱", "1", "32", "0.19", "0.6", "1", "7.35", "70 گرم بر متر", "19.5 اهم بر کیلومتر", "مطابق دیتاشیت", "فاز و نول (رنگ‌بندی استاندارد طوسی)"),
    },
    {  # 7 - NYY Flexible 1x300
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x300", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "تغذیه برق پرقدرت ماشین‌آلات صنعتی سنگین و متحرک"},
        "content_html": nyy_flex_content("۱×۳۰۰", "1480", "0.49", "2.4", "2", "مطابق دیتاشیت", "3.1 کیلوگرم بر متر", "33.3 کیلوآمپر", "0.0641 اهم بر کیلومتر"),
    },
    {  # 8 - NYY Flexible 1x240
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x240", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "تغذیه برق پرقدرت ماشین‌آلات صنعتی سنگین و متحرک"},
        "content_html": nyy_flex_content("۱×۲۴۰", "1170", "مطابق دیتاشیت", "2.2", "2.2", "29.2", "2.51 کیلوگرم بر متر", "26.6 کیلوآمپر", "0.0801 اهم بر کیلومتر"),
    },
    {  # 9 - NYY Flexible 1x185
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x185", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "ورودی تابلوهای برق بزرگ، اتصال به ژنراتور و ترانسفورماتور"},
        "content_html": nyy_flex_content("۱×۱۸۵", "875", "0.49", "2.0", "1.8", "مطابق دیتاشیت", "مطابق دیتاشیت", "20.5 کیلوآمپر", "0.106 اهم بر کیلومتر"),
    },
    {  # 10 - NYY Flexible 1x150
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x150", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "تامین برق تجهیزات صنعتی سنگین دارای تحرک"},
        "content_html": nyy_flex_content("۱×۱۵۰", "722", "0.49", "1.8", "1.7", "23.5", "1.6 کیلوگرم بر متر", "16.7 کیلوآمپر", "مطابق دیتاشیت"),
    },
    {  # 11 - NYY Flexible 1x120
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x120", "conductor_material": "مس",
                   "standard": "IEC 60502-1، INSO 3569-1، IEC 60228، DIN VDE 0271", "application": "تامین برق اصلی ماشین‌آلات پرمصرف متحرک صنعتی"},
        "content_html": nyy_flex_content("۱×۱۲۰", "570", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.7", "21.3", "1.3 کیلوگرم بر متر", "13.30 کیلوآمپر", "0.161 اهم بر کیلومتر"),
    },
    {  # 12 - NYY Flexible 1x95
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x95", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "تامین برق تجهیزات متحرک صنعتی با توان بالا"},
        "content_html": nyy_flex_content("۱×۹۵", "456", "مطابق دیتاشیت", "1.6", "1.6", "19.9", "1.1 کیلوگرم بر متر", "10.5 کیلوآمپر", "0.206 اهم بر کیلومتر"),
    },
    {  # 13 - NYY Flexible 1x70
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x70", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "کابل تغذیه ماشین‌آلات سنگین صنعتی"},
        "content_html": nyy_flex_content("۱×۷۰", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.4", "1.5", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "0.272 اهم بر کیلومتر"),
    },
    {  # 14 - NYY Flexible 1x50
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x50", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "برق‌کشی سیستم‌های مختلف صنعتی و ساختمانی"},
        "content_html": nyy_flex_content("۱×۵۰", "384", "0.39", "1.4", "1.4", "15.2", "590 گرم بر متر", "5.55 کیلوآمپر", "0.386 اهم بر کیلومتر"),
    },
    {  # 15 - NYY Flexible 1x35
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x35", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "کابل‌کشی صنعتی و تجهیزات متحرک"},
        "content_html": nyy_flex_content("۱×۳۵", "266", "مطابق دیتاشیت", "1.2", "1.4", "مطابق دیتاشیت", "428 گرم بر متر", "3.89 کیلوآمپر", "0.554 اهم بر کیلومتر"),
    },
    {  # 16 - NYY Flexible 1x25
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، INSO 3569-1، IEC 60228، DIN VDE 0271", "application": "برق‌کشی داخلی ساختمان‌ها و تاسیسات کارگاهی"},
        "content_html": nyy_flex_content("۱×۲۵", "189", "0.39", "1.2", "1.4", "12", "326 گرم بر متر", "2.78 کیلوآمپر", "مطابق دیتاشیت"),
    },
    {  # 17 - NYY Flexible 1x16
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های ساخت‌وساز پیچیده با نیاز به خمش کابل"},
        "content_html": nyy_flex_content("۱×۱۶", "126", "0.39", "1", "1.4", "10.1", "227 گرم بر متر", "1.78 کیلوآمپر", "مطابق دیتاشیت"),
    },
    {  # 18 - Telephone cable 10-pair
        "category_name": "کابل تلفن", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "10 زوج", "conductor_material": "مس",
                   "standard": "IEC 60189، VDE 0815، TCI", "application": "سیم‌کشی تلفن و شبکه‌های مخابراتی داخلی مجتمع‌های بزرگ"},
        "content_html": telephone_content("۱۰", "65 اهم بر کیلومتر", "10.3 کیلوگرم بر کلاف ۱۰۰ متری", "8.31", "رنگ‌بندی متنوع برای شناسایی هر زوج"),
    },
    {  # 19 - Telephone cable 6-pair
        "category_name": "کابل تلفن", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "6 زوج", "conductor_material": "مس",
                   "standard": "IEC 60189، VDE 0815، TCI", "application": "سیم‌کشی تلفن ثابت و آیفون تصویری آنالوگ"},
        "content_html": telephone_content("۶", "65 اهم بر کیلومتر", "7 کیلوگرم بر کلاف ۱۰۰ متری", "6.98", "قرمز-سفید، آبی-سفید، نارنجی-سفید، سبز-سفید، قهوه‌ای-سفید، طوسی-سفید"),
    },
    {  # 20 - Telephone cable 4-pair
        "category_name": "کابل تلفن", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4 زوج", "conductor_material": "مس",
                   "standard": "IEC 60189، VDE 0815، TCI", "application": "اتصال تلفن‌های ثابت و پنل آیفون به مراکز سانترال داخلی"},
        "content_html": telephone_content("۴", "65 اهم بر کیلومتر", "5.2 کیلوگرم بر کلاف ۱۰۰ متری", "6.14", "سفید-نارنجی، سفید-آبی، سفید-سبز، سفید-قهوه‌ای"),
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
    with open(os.path.join(DATA_DIR, "batch28_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch28_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch28_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
