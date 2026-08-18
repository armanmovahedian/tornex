# -*- coding: utf-8 -*-
"""Batch 35: 20 products -- 15 Khorasan Afsharnejad NYY/NYYJ/NYYO
ground/solid cables (2/3/4-core), one NYYO Flexible 3.5-core afshan
power cable, and 4 NYYO 3.5-core ground/solid power cables."""
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


def zamini_content(cores_label, structure, size_mm2, conductor_desc, ins, filler, sheath, dia, weight,
                    sc_current, resistance, colors, voltage="600/1000 ولت", test_voltage="4 کیلوولت"):
    return f"""<p>کابل زمینی {cores_label} خراسان افشارنژاد ({structure}) از رشته‌های هم‌سطح‌مقطع {size_mm2} میلی‌متر مربع با هادی {conductor_desc} ساخته شده است. رنگ‌بندی رشته‌ها ({colors}) شناسایی و نصب دقیق را تسهیل می‌کند. عایق هر رشته از PVC به ضخامت {ins} میلی‌متر است و فیلر PVC به ضخامت {filler} میلی‌متر فضای میان رشته‌ها را پر کرده و شکل گرد کابل را حفظ می‌کند.</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی هر رشته در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی {voltage} و تست ولتاژ {test_voltage}، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و برای نصب ثابت زمینی مناسب است.</p>"""


def flex_35core_content(structure, phase_mm2, neutral_mm2, phase_tar, phase_dia, neutral_tar, neutral_dia,
                         phase_ins, neutral_ins, sheath, dia, weight, sc_current, res_phase, res_neutral):
    return f"""<p>کابل افشان سه‌ونیم‌رشته {phase_mm2}+{neutral_mm2} خراسان افشارنژاد ({structure}) از سه رشته فاز افشان کلاس ۵ با سطح مقطع {phase_mm2} میلی‌متر مربع ({phase_tar} تار به قطر {phase_dia} میلی‌متر) به رنگ‌های مشکی، زرد و قرمز و یک رشته نول با سطح مقطع {neutral_mm2} میلی‌متر مربع ({neutral_tar} تار به قطر {neutral_dia} میلی‌متر) به رنگ آبی ساخته شده است. عایق PVC فاز و نول به ترتیب {phase_ins} و {neutral_ins} میلی‌متر ضخامت دارد.</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی فاز {res_phase} و نول {res_neutral} در دمای ۲۰ درجه سانتی‌گراد است. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت و تست ولتاژ ۴ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای تامین برق کارخانجات، موتورهای الکتریکی سنگین و ماشین‌آلات صنعتی مناسب است.</p>"""


def zamini_35core_content(phase_mm2, neutral_mm2, phase_desc, neutral_desc, phase_ins, neutral_ins, sheath, dia,
                           weight, sc_current, res_phase, res_neutral, colors="فاز: مشکی، زرد، قرمز؛ نول: آبی"):
    return f"""<p>کابل زمینی سه‌ونیم‌رشته {phase_mm2}+{neutral_mm2} خراسان افشارنژاد (NYYO) از سه رشته فاز با سطح مقطع {phase_mm2} میلی‌متر مربع ({phase_desc}) و یک رشته نول با سطح مقطع {neutral_mm2} میلی‌متر مربع ({neutral_desc}) ساخته شده است. رنگ‌بندی رشته‌ها ({colors}) شناسایی و نصب دقیق را تسهیل می‌کند. عایق PVC فاز و نول به ترتیب {phase_ins} و {neutral_ins} میلی‌متر ضخامت دارد و یک نوار پلی‌استر (Pet-Tape) دور رشته‌ها پیچیده شده که در برابر ضربات و فشارهای مکانیکی محافظت می‌کند.</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی فاز {res_phase} و نول {res_neutral} در دمای ۲۰ درجه سانتی‌گراد است. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت و تست ولتاژ ۴ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و برای نصب ثابت زمینی مناسب است.</p>"""


PH3G = "فاز: مشکی، زرد، قرمز؛ نول: آبی؛ ارت: زرد/سبز"
PH2N = "فاز: مشکی و قهوه‌ای؛ نول: آبی"
PH3 = "فاز: مشکی، زرد، قرمز؛ نول: آبی"
PH2 = "فاز: مشکی؛ نول: آبی"

RECORDS = [
    {  # 1 - Ground 4x1.5 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x1.5", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت در تاسیسات توزیع برق سه‌فاز و نول"},
        "content_html": zamini_content("چهاررشته ۱.۵", "NYYO", "1.5", "مفتولی تک‌رشته کلاس ۱ (قطر ۱.۳۷ میلی‌متر)", "0.8", "1.0", "1.8", "مطابق دیتاشیت", "مطابق دیتاشیت", "167 آمپر", "12.1 اهم بر کیلومتر", PH3),
    },
    {  # 2 - Ground 3x35 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x35", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت در پروژه‌های کوچک و بزرگ بدون نیاز به رشته ارت"},
        "content_html": zamini_content("سه‌رشته ۳۵ (دو فاز و یک نول)", "NYY", "35", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۴۷ میلی‌متر)", "1.2", "1.0", "1.8", "27.01", "1.7 کیلوگرم بر متر", "3.89 کیلوآمپر", "مطابق دیتاشیت", PH2N),
    },
    {  # 3 - Ground 3x25 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب در لوله‌ها، داکت‌ها، ترانکینگ‌ها و روی دیوار در شبکه فشار ضعیف"},
        "content_html": zamini_content("سه‌رشته ۲۵ (دو فاز و یک نول)", "NYY", "25", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۱ میلی‌متر)", "1.2", "مطابق دیتاشیت", "1.8", "24.31", "1.3 کیلوگرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", PH2N),
    },
    {  # 4 - Ground 3x16 NYYJ
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های صنعتی و ساختمانی با نیاز به رشته ارت"},
        "content_html": zamini_content("سه‌رشته ۱۶", "NYYJ", "16", "نیمه‌افشان کلاس ۲ (۷ مفتول به قطر ۱.۶۸ میلی‌متر)", "1.0", "1.0", "1.8", "20.9", "895 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", PH3G),
    },
    {  # 5 - Ground 3x10 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x10", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1", "application": "نصب ثابت در ساختمان‌های مسکونی، تجاری و صنعتی"},
        "content_html": zamini_content("سه‌رشته ۱۰", "NYY", "10", "مفتولی تک‌رشته کلاس ۱ (قطر ۳.۵۲ میلی‌متر)", "1.0", "مطابق دیتاشیت", "1.8", "17.5", "599 گرم بر متر", "1.11 کیلوآمپر", "مطابق دیتاشیت", PH3G),
    },
    {  # 6 - Ground 3x6 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x6", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت در تاسیسات توزیع برق با نیاز به رشته ارت"},
        "content_html": zamini_content("سه‌رشته ۶", "NYY", "6", "مفتولی تک‌رشته کلاس ۱ (قطر ۲.۷۲ میلی‌متر)", "1.0", "1.0", "مطابق دیتاشیت", "15.8", "445 گرم بر متر", "666 آمپر", "مطابق دیتاشیت", "فاز: مشکی؛ نول: آبی؛ ارت: زرد/سبز"),
    },
    {  # 7 - Ground 3x4 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x4", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت در تاسیسات توزیع برق با نیاز به رشته ارت"},
        "content_html": zamini_content("سه‌رشته ۴", "NYY", "4", "مفتولی تک‌رشته کلاس ۱ (قطر ۲.۲۲ میلی‌متر)", "1.0", "1.0", "1.8", "14.74", "362 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", PH3G),
    },
    {  # 8 - Ground 3x2.5 NYY-J
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x2.5", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "برق‌رسانی اصلی ساختمان‌ها، موتورها و روشنایی محوطه"},
        "content_html": zamini_content("سه‌رشته ۲.۵", "NYY-J", "2.5", "مفتولی تک‌رشته کلاس ۱", "مطابق دیتاشیت", "1.0", "1.8", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "7.4 اهم بر کیلومتر", PH3G),
    },
    {  # 9 - Ground 3x1.5 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x1.5", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1", "application": "نصب ثابت در مدارهای نیازمند سیم ارت"},
        "content_html": zamini_content("سه‌رشته ۱.۵", "NYY", "1.5", "مفتولی تک‌رشته کلاس ۱", "0.8", "1.0", "1.8", "12", "215 گرم بر متر", "مطابق دیتاشیت", "12.1 اهم بر کیلومتر", PH3G),
    },
    {  # 10 - Ground 2x16 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت زمینی با نیاز به استحکام مکانیکی بالا"},
        "content_html": zamini_content("دورشته ۱۶", "NYY", "16", "نیمه‌افشان کلاس ۲ (۷ مفتول به قطر ۱.۶۸ میلی‌متر)", "1.0", "1.0", "1.8", "19.8", "720 گرم بر متر", "1.78 کیلوآمپر", "1.15 اهم بر کیلومتر", PH2),
    },
    {  # 11 - Ground 2x10 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x10", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت با نیاز به استحکام مکانیکی بالا"},
        "content_html": zamini_content("دورشته ۱۰", "NYY", "10", "مفتولی تک‌رشته کلاس ۱ (قطر ۳.۵۲ میلی‌متر)", "1.0", "1.0", "1.8", "16.74", "505 گرم بر متر", "مطابق دیتاشیت", "1.83 اهم بر کیلومتر", PH2),
    },
    {  # 12 - Ground 2x6 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x6", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت برای تغذیه بارهای سنگین"},
        "content_html": zamini_content("دورشته ۶", "NYY", "6", "مفتولی تک‌رشته کلاس ۱ (قطر ۲.۷۲ میلی‌متر)", "1.0", "1.0", "1.8", "15.05", "379 گرم بر متر", "666 آمپر", "مطابق دیتاشیت", PH2),
    },
    {  # 13 - Ground 2x4 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x4", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت زیرزمینی، روی دیوار و در کانال‌ها"},
        "content_html": zamini_content("دورشته ۴", "NYY", "4", "مفتولی تک‌رشته کلاس ۱ (قطر ۲.۲۲ میلی‌متر)", "1.0", "مطابق دیتاشیت", "1.8", "14.05", "311 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", PH2),
    },
    {  # 14 - Ground 2x2.5 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x2.5", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت و زمینی بدون نیاز به خمش کابل"},
        "content_html": zamini_content("دورشته ۲.۵", "NYY", "2.5", "مفتولی تک‌رشته کلاس ۱ (قطر ۱.۷۵ میلی‌متر)", "1.0", "مطابق دیتاشیت", "1.8", "12.3", "230 گرم بر متر", "278 آمپر", "مطابق دیتاشیت", PH2),
    },
    {  # 15 - Ground 2x1.5 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x1.5", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت بدون نیاز به خمش کابل"},
        "content_html": zamini_content("دورشته ۱.۵", "NYY", "1.5", "مفتولی تک‌رشته کلاس ۱ (قطر ۱.۳۷ میلی‌متر)", "0.8", "1.0", "1.8", "11.54", "191 گرم بر متر", "مطابق دیتاشیت", "12.1 اهم بر کیلومتر", PH2),
    },
    {  # 16 - Flexible 3.5-core 240+120 NYYO Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x240+120", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "تامین برق کارخانجات، موتورهای سنگین و شبکه‌های توزیع برق"},
        "content_html": flex_35core_content("NYYO Flexible", "240", "120", "مطابق دیتاشیت", "0.49", "مطابق دیتاشیت", "0.49", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "71.01", "11 کیلوگرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت"),
    },
    {  # 17 - Ground 3.5-core 185+95 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x185+95", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "کابل اصلی سیستم‌های برق صنعتی"},
        "content_html": zamini_35core_content("185", "95", "نیمه‌افشان کلاس ۲، ۳۷ تار به قطر ۲.۵۴ میلی‌متر", "نیمه‌افشان کلاس ۲، ۱۹ تار به قطر ۲.۵۴ میلی‌متر", "مطابق دیتاشیت", "مطابق دیتاشیت", "2.5", "47.7", "7 کیلوگرم بر متر", "20.5 کیلوآمپر", "0.0991 اهم بر کیلومتر", "0.193 اهم بر کیلومتر"),
    },
    {  # 18 - Ground 3.5-core 150+70 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x150+70", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "پروژه‌های زیرزمینی و صنعتی با بار الکتریکی بالا"},
        "content_html": zamini_35core_content("150", "70", "نیمه‌افشان کلاس ۲ (۳۷ مفتول به قطر ۲.۲۴ میلی‌متر)", "نیمه‌افشان کلاس ۲", "1.8", "مطابق دیتاشیت", "2.3", "42.6", "5.53 کیلوگرم بر متر", "16.7 کیلوآمپر", "0.124 اهم بر کیلومتر", "0.268 اهم بر کیلومتر"),
    },
    {  # 19 - Ground 3.5-core 120+70 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x120+70", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "انتقال برق و تامین انرژی در نیروگاه‌ها و ساختمان‌های صنعتی"},
        "content_html": zamini_35core_content("120", "70", "نیمه‌افشان کلاس ۲", "نیمه‌افشان کلاس ۲", "1.6", "1.4", "مطابق دیتاشیت", "39.6", "4.7 کیلوگرم بر متر", "مطابق دیتاشیت", "0.153 اهم بر کیلومتر", "0.268 اهم بر کیلومتر"),
    },
    {  # 20 - Ground 3.5-core 95+50 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x95+50", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "شبکه‌های ولتاژ پایین با نیاز به هادی سکتوری فشرده"},
        "content_html": zamini_35core_content("95", "50", "نیمه‌افشان کلاس ۲ سکتوری، ۱۹ تار به قطر ۲.۵۴ میلی‌متر", "نیمه‌افشان کلاس ۲ سکتوری، ۱۹ تار به قطر ۱.۷۸ میلی‌متر", "1.6", "1.4", "2.1", "36.4", "مطابق دیتاشیت", "مطابق دیتاشیت", "0.193 اهم بر کیلومتر", "0.387 اهم بر کیلومتر"),
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
    with open(os.path.join(DATA_DIR, "batch35_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch35_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch35_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
