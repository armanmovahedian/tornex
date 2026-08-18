# -*- coding: utf-8 -*-
"""Batch 34: 20 products -- 6 more Khorasan Afsharnejad NYMHY 2-core
flexible cables, 8 NYYJ/NYY 5-core ground/solid cables, and 6
NYYO/NYY 4-core ground/solid cables."""
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


def zamini_content(cores_label, structure, size_mm2, conductor_desc, ins, filler, sheath, dia, weight,
                    sc_current, resistance, colors, voltage="600/1000 ولت", test_voltage="4 کیلوولت"):
    return f"""<p>کابل زمینی {cores_label} خراسان افشارنژاد ({structure}) از رشته‌های هم‌سطح‌مقطع {size_mm2} میلی‌متر مربع با هادی {conductor_desc} ساخته شده است. رنگ‌بندی رشته‌ها ({colors}) شناسایی و نصب دقیق را تسهیل می‌کند. عایق هر رشته از PVC به ضخامت {ins} میلی‌متر است و فیلر PVC به ضخامت {filler} میلی‌متر فضای میان رشته‌ها را پر کرده و شکل گرد کابل را حفظ می‌کند.</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی هر رشته در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی {voltage} و تست ولتاژ {test_voltage}، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و برای نصب ثابت زمینی مناسب است.</p>"""


PH3G = "فاز: مشکی، زرد، قرمز؛ نول: آبی؛ ارت: زرد/سبز"
PH3 = "فاز: مشکی، زرد، قرمز؛ نول: آبی"
PH2 = "فاز: مشکی؛ نول: آبی"

RECORDS = [
    {  # 1 - 2x6 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x6", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "شبکه‌های فشار ضعیف با نیاز به تغذیه وسایل پرقدرت در فواصل کوتاه"},
        "content_html": flex_ncore_content("۲×۶", "NYMHY", "6", "84", "0.29", "0.8", "1.3", "12.02", "250 گرم بر متر", "666 آمپر", "3.3 اهم بر کیلومتر", "450/750 ولت", "2 کیلوولت", PH2),
    },
    {  # 2 - 2x4 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x4", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "برق‌رسانی به تجهیزات پرتوان آشپزخانه و کارگاه"},
        "content_html": flex_ncore_content("۲×۴", "NYMHY", "4", "56", "0.29", "0.8", "1.3", "10.9", "190 گرم بر متر", "مطابق دیتاشیت", "4.95 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH2),
    },
    {  # 3 - 2x2.5 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x2.5", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228", "application": "تغذیه تجهیزات برقی منزل و کارگاه با توان متوسط"},
        "content_html": flex_ncore_content("۲×۲.۵", "NYMHY", "2.5", "50", "0.24", "0.8", "1.0", "9.14", "131 گرم بر متر", "278 آمپر", "7.98 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH2),
    },
    {  # 4 - 2x1.5 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x1.5", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "برق‌رسانی لوازم برقی قابل حمل منزل"},
        "content_html": flex_ncore_content("۲×۱.۵", "NYMHY", "1.5", "30", "مطابق دیتاشیت", "0.7", "0.8", "7.44", "84.76 گرم بر متر", "167 آمپر", "13.3 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH2),
    },
    {  # 5 - 2x1 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x1", "conductor_material": "مس",
                   "standard": "IEC 60227", "application": "اتصال لوازم برقی منزل و اداری"},
        "content_html": flex_ncore_content("۲×۱", "NYMHY", "1", "32", "مطابق دیتاشیت", "مطابق دیتاشیت", "0.8", "6.52", "64.15 گرم بر متر", "111 آمپر", "19.5 اهم بر کیلومتر", "300/500 ولت", "2 کیلوولت", PH2),
    },
    {  # 6 - 2x0.75 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x0.75", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "اتصال وسایل برقی کوچک و روشنایی"},
        "content_html": flex_ncore_content("۲×۰.۷۵", "NYMHY", "0.75", "24", "0.2", "0.6", "0.8", "6.28", "56.25 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", "300/500 ولت", "2 کیلوولت", PH2),
    },
    {  # 7 - Ground 5x35 NYYJ
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x35", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "انتقال نیرو در پروژه‌های زیرساختی بزرگ"},
        "content_html": zamini_content("پنج‌رشته ۳۵", "NYYJ", "35", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۴۷ میلی‌متر)", "1.2", "مطابق دیتاشیت", "2", "32.9", "2.6 کیلوگرم بر متر", "3.89 کیلوآمپر", "0.524 اهم بر کیلومتر", PH3G),
    },
    {  # 8 - Ground 5x25 NYYJ
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "اتصال الکتروموتورهای صنعتی و برق‌رسانی به مجتمع‌ها و سوله‌ها"},
        "content_html": zamini_content("پنج‌رشته ۲۵", "NYYJ", "25", "نیمه‌افشان کلاس ۲", "1.2", "1.0", "1.9", "29.3", "2 کیلوگرم بر متر", "مطابق دیتاشیت", "0.727 اهم بر کیلومتر", PH3G),
    },
    {  # 9 - Ground 5x16 NYYJ
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "انتقال برق قدرت فشار ضعیف در هوا و زیرزمین"},
        "content_html": zamini_content("پنج‌رشته ۱۶", "NYYJ", "16", "نیمه‌افشان کلاس ۲", "1.0", "1.0", "1.8", "24.6", "1.3 کیلوگرم بر متر", "مطابق دیتاشیت", "1.5 اهم بر کیلومتر", "فاز: زرد، قرمز، مشکی؛ نول: آبی؛ ارت: زرد/سبز"),
    },
    {  # 10 - Ground 5x10 NYYJ
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x10", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های صنعتی، تجاری و ساختمانی با نیاز به حمل جریان سنگین"},
        "content_html": zamini_content("پنج‌رشته ۱۰", "NYYJ", "10", "مفتولی تک‌رشته کلاس ۱", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.8", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.11 کیلوآمپر", "مطابق دیتاشیت", PH3G),
    },
    {  # 11 - Ground 5x6 NYYJ
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x6", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت زمینی در فضاهای محدود"},
        "content_html": zamini_content("پنج‌رشته ۶", "NYYJ", "6", "مفتولی تک‌رشته کلاس ۱", "1.0", "1.0", "1.8", "18.35", "633 گرم بر متر", "666 آمپر", "3.1 اهم بر کیلومتر", PH3G),
    },
    {  # 12 - Ground 5x4 NYYJ
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x4", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "مدارهای تغذیه قدرت، توزیع برق و سیستم‌های روشنایی"},
        "content_html": zamini_content("پنج‌رشته ۴", "NYYJ", "4", "مفتولی تک‌رشته کلاس ۱", "1.0", "1.0", "1.8", "17.1", "503 گرم بر متر", "444 آمپر", "مطابق دیتاشیت", PH3G),
    },
    {  # 13 - Ground 5x2.5 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x2.5", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت در تاسیسات ساختمانی و صنعتی"},
        "content_html": zamini_content("پنج‌رشته ۲.۵", "NYY", "2.5", "مفتولی تک‌رشته کلاس ۱ (قطر ۱.۷۵ میلی‌متر)", "مطابق دیتاشیت", "1.0", "1.8", "14.65", "353 گرم بر متر", "278 آمپر", "مطابق دیتاشیت", PH3G),
    },
    {  # 14 - Ground 5x1.5 NYYJ
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x1.5", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت زمینی با نیاز به رشته ارت"},
        "content_html": zamini_content("پنج‌رشته ۱.۵", "NYYJ", "1.5", "مفتولی تک‌رشته کلاس ۱", "0.8", "1.0", "1.8", "13.6", "283 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", PH3G),
    },
    {  # 15 - Ground 4x25 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "کاربردهای صنعتی و ساختمانی با نیاز به انتقال پایدار انرژی"},
        "content_html": zamini_content("چهاررشته ۲۵", "NYYO", "25", "نیمه‌افشان کلاس ۲", "مطابق دیتاشیت", "1.0", "1.8", "26.6", "1.6 کیلوگرم بر متر", "مطابق دیتاشیت", "0.727 اهم بر کیلومتر", PH3),
    },
    {  # 16 - Ground 4x16 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت در تونل‌ها، زیرزمین و مسیرهای صنعتی طولانی"},
        "content_html": zamini_content("چهاررشته ۱۶", "NYYO", "16", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۱.۶۸ میلی‌متر)", "1.0", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.1 کیلوگرم بر متر", "1.78 کیلوآمپر", "1.15 اهم بر کیلومتر", PH3),
    },
    {  # 17 - Ground 4x10 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x10", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "توزیع نیروی برق در نصب ثابت تاسیسات"},
        "content_html": zamini_content("چهاررشته ۱۰", "NYYO", "10", "مفتولی تک‌رشته کلاس ۱ (قطر ۳.۵۲ میلی‌متر)", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "18.9", "728 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", PH3),
    },
    {  # 18 - Ground 4x6 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x6", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت در شبکه‌های توزیع سه‌فاز و نول"},
        "content_html": zamini_content("چهاررشته ۶", "NYY-O", "6", "مفتولی تک‌رشته کلاس ۱", "1.0", "1.0", "1.8", "17", "532 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", PH3),
    },
    {  # 19 - Ground 4x4 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x4", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های کابل‌کشی زمینی مسکونی و صنعتی"},
        "content_html": zamini_content("چهاررشته ۴", "NYYO", "4", "مفتولی تک‌رشته کلاس ۱ (قطر ۲.۲۲ میلی‌متر)", "1.0", "مطابق دیتاشیت", "1.8", "15.84", "425 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", PH3),
    },
    {  # 20 - Ground 4x2.5 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x2.5", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت در شبکه‌های توزیع سه‌فاز و نول"},
        "content_html": zamini_content("چهاررشته ۲.۵", "NYY", "2.5", "مفتولی تک‌رشته کلاس ۱ (قطر ۱.۷۵ میلی‌متر)", "1.0", "1.0", "1.8", "13.7", "305 گرم بر متر", "278 آمپر", "مطابق دیتاشیت", PH3),
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
    with open(os.path.join(DATA_DIR, "batch34_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch34_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch34_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
