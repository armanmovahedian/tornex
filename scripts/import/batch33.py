# -*- coding: utf-8 -*-
"""Batch 33: 20 products -- Khorasan Afsharnejad NYMHY/NYY/NYY-O
Flexible cables: 6 four-core, 8 three-core, and 2 two-core cables,
plus 4 more (rounding out the 3-core NYMHY family)."""
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


def flex_ncore_content(cores_label, structure, size_mm2, tar_count, tar_dia, ins, sheath, dia, weight,
                        sc_current, resistance, voltage, test_voltage, colors, filler=None):
    filler_sentence = f" فیلر PVC به ضخامت {filler} میلی‌متر فضای میان رشته‌ها را پر می‌کند." if filler else ""
    return f"""<p>کابل افشان {cores_label} خراسان افشارنژاد ({structure}) از رشته‌های هم‌سطح‌مقطع {size_mm2} میلی‌متر مربع با هادی افشان کلاس ۵ ({tar_count} تار به قطر {tar_dia} میلی‌متر در هر رشته) ساخته شده است. رنگ‌بندی رشته‌ها ({colors}) شناسایی و نصب دقیق را تسهیل می‌کند. عایق هر رشته از PVC به ضخامت {ins} میلی‌متر است.{filler_sentence}</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی هر رشته در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی {voltage} و تست ولتاژ {test_voltage}، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


PH3 = "فاز: مشکی، زرد، قرمز؛ نول: آبی"
PH3G = "فاز: مشکی؛ نول: آبی؛ ارت: زرد/سبز"
PH2N = "فاز: مشکی و قهوه‌ای؛ نول: آبی"
PH2 = "فاز: مشکی؛ نول: آبی"

RECORDS = [
    {  # 1 - 4x6 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x6", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-6", "application": "تامین برق تجهیزات مختلف با مصرف متوسط"},
        "content_html": flex_ncore_content("۴×۶", "NYMHY", "6", "84", "0.29", "0.8", "1.4", "مطابق دیتاشیت", "مطابق دیتاشیت", "666 آمپر", "3.3 اهم بر کیلومتر", "450/750 ولت", "2 کیلوولت", PH3),
    },
    {  # 2 - 4x4 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x4", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "انتقال توان به دستگاه‌های پرمصرف در شبکه‌های فشار ضعیف"},
        "content_html": flex_ncore_content("۴×۴", "NYMHY", "4", "56", "0.29", "0.8", "1.4", "12.8", "287 گرم بر متر", "444 آمپر", "4.95 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH3),
    },
    {  # 3 - 4x2.5 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x2.5", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "صنایع ساختمانی، خودروسازی و کشاورزی"},
        "content_html": flex_ncore_content("۴×۲.۵", "NYMHY", "2.5", "50", "0.24", "0.8", "1.1", "10.8", "197 گرم بر متر", "278 آمپر", "7.98 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH3),
    },
    {  # 4 - 4x1.5 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x1.5", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "اتصالات برق سیار و تغذیه دستگاه‌های متحرک الکتریکی"},
        "content_html": flex_ncore_content("۴×۱.۵", "NYMHY", "1.5", "30", "0.24", "0.7", "1.0", "9.04", "133 گرم بر متر", "مطابق دیتاشیت", "13.3 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH3),
    },
    {  # 5 - 3x35 NYY-O Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x35", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های ساختمانی و صنعتی با نیاز به کابل قابل خمش"},
        "content_html": flex_ncore_content("سه‌رشته ۳۵", "NYY-O Flexible", "35", "266", "0.39", "1.2", "1.9", "28.2", "1.7 کیلوگرم بر متر", "3.89 کیلوآمپر", "0.554 اهم بر کیلومتر", "600/1000 ولت", "4 کیلوولت", "مطابق دیتاشیت", filler="1.0"),
    },
    {  # 6 - 4x1 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x1", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "تغذیه دستگاه‌های سه‌فاز به همراه نول در شبکه ولتاژ پایین"},
        "content_html": flex_ncore_content("۴×۱ (بدون ارت)", "NYMHY", "1", "32", "0.19", "0.6", "0.9", "7.7", "96 گرم بر متر", "مطابق دیتاشیت", "19.5 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", "فاز: قرمز، مشکی، قهوه‌ای؛ نول: آبی"),
    },
    {  # 7 - 4x0.75 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x0.75", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "اتصال دستگاه‌های کم‌مصرف سه‌فاز با نول"},
        "content_html": flex_ncore_content("۴×۰.۷۵", "NYMHY", "0.75", "24", "0.2", "مطابق دیتاشیت", "مطابق دیتاشیت", "7.24", "79.85 گرم بر متر", "مطابق دیتاشیت", "26 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH3),
    },
    {  # 8 - 3x70 NYY-O Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x70", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "انرژی‌رسانی به ماشین‌آلات و تجهیزات بزرگ صنعتی"},
        "content_html": flex_ncore_content("سه‌رشته ۷۰ (دو فاز و یک نول)", "NYY-O Flexible", "70", "350", "0.49", "1.4", "2.2", "37.8", "3.2 کیلوگرم بر متر", "7.77 کیلوآمپر", "0.272 اهم بر کیلومتر", "600/1000 ولت", "4 کیلوولت", PH2N, filler="1.2"),
    },
    {  # 9 - 3x50 NYY-O Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x50", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های صنعتی و ساختمانی با نیاز به جریان بالا"},
        "content_html": flex_ncore_content("سه‌رشته ۵۰ (دو فاز و یک نول)", "NYY-O Flexible", "50", "384", "0.39", "1.4", "مطابق دیتاشیت", "33.1", "2.4 کیلوگرم بر متر", "5.55 کیلوآمپر", "0.386 اهم بر کیلومتر", "600/1000 ولت", "4 کیلوولت", PH2N),
    },
    {  # 10 - 3x25 NYY-O Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "برق‌کشی ساختمانی و صنعتی با نیاز به خمش کابل"},
        "content_html": flex_ncore_content("سه‌رشته ۲۵ (دو فاز و یک نول)", "NYY-O Flexible", "25", "189", "0.39", "1.2", "مطابق دیتاشیت", "25.4", "1.3 کیلوگرم بر متر", "2.78 کیلوآمپر", "0.78 اهم بر کیلومتر", "600/1000 ولت", "4 کیلوولت", PH2N, filler="1.0"),
    },
    {  # 11 - 3x16 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "تامین برق وسایل و ابزارآلات پرمصرف"},
        "content_html": flex_ncore_content("سه‌رشته ۱۶", "NYY Flexible", "16", "126", "0.39", "1.0", "مطابق دیتاشیت", "19.37", "710 گرم بر متر", "1.78 کیلوآمپر", "1.21 اهم بر کیلومتر", "600/1000 ولت", "4 کیلوولت", PH3G),
    },
    {  # 12 - 3x10 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x10", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "تامین برق وسایل پرتابل و ابزارآلات صنعتی"},
        "content_html": flex_ncore_content("سه‌رشته ۱۰", "NYY Flexible", "10", "80", "0.39", "1.0", "1.8", "16.72", "545 گرم بر متر", "1.11 کیلوآمپر", "1.91 اهم بر کیلومتر", "600/1000 ولت", "4 کیلوولت", PH3G),
    },
    {  # 13 - 3x6 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x6", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-6", "application": "اتصال کنتور برق اصلی و سیستم‌های توزیع برق"},
        "content_html": flex_ncore_content("سه‌رشته ۶", "NYMHY", "6", "84", "0.29", "0.8", "1.4", "12.93", "308 گرم بر متر", "666 آمپر", "مطابق دیتاشیت", "450/750 ولت", "2 کیلوولت", PH3G),
    },
    {  # 14 - 3x4 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x4", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "تغذیه کولرهای گازی و سیستم‌های گرمایش برقی"},
        "content_html": flex_ncore_content("سه‌رشته ۴", "NYMHY", "4", "56", "0.29", "0.8", "1.3", "11.5", "230 گرم بر متر", "444 آمپر", "4.95 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH3G),
    },
    {  # 15 - 3x2.5 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x2.5", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "سیم‌کشی مسیرهای پیچیده با نیاز به خمش"},
        "content_html": flex_ncore_content("سه‌رشته ۲.۵", "NYMHY", "2.5", "50", "مطابق دیتاشیت", "0.8", "1.1", "9.9", "162 گرم بر متر", "مطابق دیتاشیت", "7.98 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH3G),
    },
    {  # 16 - 3x1.5 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x1.5", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "سیم‌کشی دستگاه‌های قابل حمل کم‌مصرف"},
        "content_html": flex_ncore_content("سه‌رشته ۱.۵", "NYMHY", "1.5", "30", "0.24", "0.7", "0.9", "8.1", "106 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", "300/500 ولت", "2 کیلوولت", PH3G),
    },
    {  # 17 - 3x1 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x1", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "اتصال ایمن لوازم برقی کوچک"},
        "content_html": flex_ncore_content("سه‌رشته ۱", "NYMHY", "1", "32", "0.19", "0.6", "مطابق دیتاشیت", "6.89", "77 گرم بر متر", "111 آمپر", "19.5 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH3G),
    },
    {  # 18 - 3x0.75 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x0.75", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "اتصال دستگاه‌های برقی کوچک با نیاز به سیم ارت"},
        "content_html": flex_ncore_content("سه‌رشته ۰.۷۵", "NYMHY", "0.75", "24", "0.2", "مطابق دیتاشیت", "0.8", "6.63", "67 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", "300/500 ولت", "2 کیلوولت", PH3G),
    },
    {  # 19 - 2x16 NYY-O Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "کابل رابط برای تجهیزات پرمصرف"},
        "content_html": flex_ncore_content("دورشته ۱۶", "NYY-O Flexible", "16", "126", "0.39", "1.0", "1.8", "18.26", "545 گرم بر متر", "مطابق دیتاشیت", "1.21 اهم بر کیلومتر", "600/1000 ولت", "4 کیلوولت", PH2),
    },
    {  # 20 - 2x10 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x10", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "اتصالات متحرک و تجهیزات با نیاز به انعطاف بالا"},
        "content_html": flex_ncore_content("دورشته ۱۰", "NYY Flexible", "10", "80", "0.39", "1.0", "1.8", "15.8", "432 گرم بر متر", "1.11 کیلوآمپر", "1.91 اهم بر کیلومتر", "600/1000 ولت", "4 کیلوولت", PH2),
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
    with open(os.path.join(DATA_DIR, "batch33_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch33_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch33_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
