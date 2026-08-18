# -*- coding: utf-8 -*-
"""Batch 32: 20 products -- 2 more NYAF flexible colored wires, a
Leoni Studer fire alarm cable, 6 NYY Flexible 3.5-core cables, 6
NYY/NYMHY 5-core cables, and 3 NYY 4-core cables, all Khorasan
Afsharnejad except the Leoni cable."""
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


def nyaf_content(size, tar_count, tar_dia, resistance, insulation, dia, weight, voltage="450/750 ولت"):
    return f"""<p>سیم برق افشان رنگی {size} خراسان افشارنژاد (NYAF) از هادی مسی آنیل‌شده افشان کلاس ۵ ({tar_count} تار به قطر {tar_dia} میلی‌متر) با عایق PVC به ضخامت {insulation} میلی‌متر ساخته شده و در رنگ‌های قرمز، آبی، مشکی، قهوه‌ای، زرد، سبز، ارت یا رنگ سفارشی مشتری تولید می‌شود. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است. با ولتاژ نامی {voltage} و تست ولتاژ ۲.۵ کیلوولت، عایق آن در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد دوام می‌آورد و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def flex_35core_content(structure, phase_mm2, neutral_mm2, phase_tar, phase_dia, neutral_tar, neutral_dia,
                         phase_ins, neutral_ins, filler, sheath, dia, weight, sc_current, res_phase, res_neutral):
    return f"""<p>کابل افشان سه‌ونیم‌رشته {phase_mm2}+{neutral_mm2} خراسان افشارنژاد ({structure}) از سه رشته فاز افشان کلاس ۵ با سطح مقطع {phase_mm2} میلی‌متر مربع ({phase_tar} تار به قطر {phase_dia} میلی‌متر) به رنگ‌های مشکی، زرد و قرمز و یک رشته نول با سطح مقطع {neutral_mm2} میلی‌متر مربع ({neutral_tar} تار به قطر {neutral_dia} میلی‌متر) به رنگ آبی ساخته شده است. عایق PVC فاز و نول به ترتیب {phase_ins} و {neutral_ins} میلی‌متر ضخامت دارد و فیلر PVC به ضخامت {filler} میلی‌متر فضای میان رشته‌ها را پر می‌کند.</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی فاز {res_phase} و نول {res_neutral} در دمای ۲۰ درجه سانتی‌گراد است. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت و تست ولتاژ ۴ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def flex_5core_content(structure, size_mm2, tar_count, tar_dia, ins, sheath, dia, weight, sc_current, resistance,
                        voltage="600/1000 ولت", test_voltage="4 کیلوولت",
                        colors="مشکی، قهوه‌ای، قرمز (فاز)؛ آبی (نول)؛ زرد/سبز (ارت)"):
    return f"""<p>کابل افشان پنج‌رشته {size_mm2} خراسان افشارنژاد ({structure}) از پنج رشته هم‌سطح‌مقطع {size_mm2} میلی‌متر مربع (سه فاز، یک نول و یک ارت) با هادی افشان کلاس ۵ ({tar_count} تار به قطر {tar_dia} میلی‌متر در هر رشته) ساخته شده است. رنگ‌بندی رشته‌ها ({colors}) شناسایی و نصب دقیق را تسهیل می‌کند. عایق هر رشته از PVC به ضخامت {ins} میلی‌متر است.</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی هر رشته در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی {voltage} و تست ولتاژ {test_voltage}، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای تغذیه تجهیزات سه‌فاز و مدارهای کنترل مناسب است.</p>"""


def flex_4core_content(structure, size_mm2, tar_count, tar_dia, ins, filler, sheath, dia, weight, sc_current, resistance):
    return f"""<p>کابل افشان چهاررشته {size_mm2} خراسان افشارنژاد ({structure}) از چهار رشته هم‌سطح‌مقطع {size_mm2} میلی‌متر مربع (سه فاز به رنگ‌های مشکی، زرد و قرمز و یک نول به رنگ آبی) با هادی افشان کلاس ۵ ({tar_count} تار به قطر {tar_dia} میلی‌متر در هر رشته) ساخته شده است. عایق هر رشته از PVC به ضخامت {ins} میلی‌متر و فیلر PVC به ضخامت {filler} میلی‌متر فضای میان رشته‌ها را پر می‌کند.</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی هر رشته در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت و تست ولتاژ ۴ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


RECORDS = [
    {  # 1 - NYAF 70mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "70", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "اتصال دستگاه‌های جوشکاری و سایر تجهیزات صنعتی پرجریان"},
        "content_html": nyaf_content("۷۰", "مطابق دیتاشیت", "مطابق دیتاشیت", "۰.۲۷۲ اهم بر کیلومتر", "1.4", "14.4", "685 گرم بر متر"),
    },
    {  # 2 - NYAF 1mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0271، IEC 60228", "application": "سیم‌کشی مدارهای فشار ضعیف با جریان کم"},
        "content_html": nyaf_content("۱", "32", "0.19", "۱۹.۴۸ اهم بر کیلومتر", "0.6", "مطابق دیتاشیت", "مطابق دیتاشیت", voltage="300/500 ولت"),
    },
    {  # 3 - Leoni Studer fire alarm cable 2x1.5
        "category_name": "کابل اعلام حریق", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "لئونی", "size_diameter": "2x1.5", "conductor_material": "مس",
                   "standard": "BS6387 C.W.Z، FR-SIR-F90", "application": "اتصال دتکتور، آژیر و پنل کنترل در سیستم‌های اعلام حریق ثابت"},
        "content_html": """<p>کابل اعلام حریق اشتودر (Studer) لئونی ۲×۱.۵ با کد ۳۰۵۲۰۸، از هادی مسی افشان کلاس ۵ با عایق XLPE و شیلد مسی (SC) زیر روکش نهایی LSHF (کم‌دود، بدون هالوژن) قرمزرنگ ساخته شده است. مطابق استاندارد BS6387 با رده C.W.Z تولید شده که نشان‌دهنده مقاومت آن در برابر آتش در دمای بالا (C)، مقاومت در برابر ضربه (W) و مقاومت در برابر پاشش آب (Z) است؛ این کابل می‌تواند تا ۳ ساعت در دمای ۹۵۰ درجه سانتی‌گراد به عملکرد خود ادامه دهد.</p>
<p>با ولتاژ نامی ۳۰۰/۵۰۰ ولت و تست ولتاژ ۲ کیلوولت، در اتصال کوتاه تا ۲۵۰ درجه سانتی‌گراد را تحمل می‌کند و در بازه دمایی کاری تا ۹۰ درجه سانتی‌گراد کار می‌کند. برای اتصال دتکتورها، آژیرها و پنل‌های کنترل در سیستم‌های اعلام حریق ساختمان‌های مسکونی، تجاری، بیمارستان‌ها و مدارس مناسب است.</p>""",
    },
    {  # 4 - Flexible 5x35 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x35", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "توزیع برق سه‌فاز سنگین در پروژه‌های صنعتی و ساختمانی"},
        "content_html": flex_5core_content("NYY Flexible", "35", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "2.1", "34.7", "2.6 کیلوگرم بر متر", "مطابق دیتاشیت", "0.554 اهم بر کیلومتر"),
    },
    {  # 5 - Flexible 5x25 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "توزیع برق در تاسیسات صنعتی بزرگ"},
        "content_html": flex_5core_content("NYY Flexible", "25", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.2", "مطابق دیتاشیت", "31.3", "1.98 کیلوگرم بر متر", "2.78 کیلوآمپر", "0.78 اهم بر کیلومتر"),
    },
    {  # 6 - Flexible 3.5-core 120+70 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x120+70", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "شبکه‌های ولتاژ پایین با نیاز به جریان بالا"},
        "content_html": flex_35core_content("NYY Flexible", "120", "70", "570", "0.49", "350", "0.49", "1.6", "1.4", "1.4", "2.5", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "0.161 اهم بر کیلومتر", "0.272 اهم بر کیلومتر"),
    },
    {  # 7 - Flexible 3.5-core 95+50 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x95+50", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های صنعتی بزرگ با نیاز به جریان بالا"},
        "content_html": flex_35core_content("NYY Flexible", "95", "50", "456", "0.49", "384", "0.39", "1.6", "1.4", "1.4", "2.4", "مطابق دیتاشیت", "مطابق دیتاشیت", "10.5 کیلوآمپر", "0.206 اهم بر کیلومتر", "0.386 اهم بر کیلومتر"),
    },
    {  # 8 - Flexible 3.5-core 70+35 NYY-O Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x70+35", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "سیستم‌های برقی ساختمانی با نیاز به نصب در فضاهای محدود"},
        "content_html": flex_35core_content("NYY-O Flexible", "70", "35", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.4", "1.2", "1.2", "2.2", "39.1", "3.5 کیلوگرم بر متر", "7.77 کیلوآمپر", "0.272 اهم بر کیلومتر", "0.554 اهم بر کیلومتر"),
    },
    {  # 9 - Flexible 3.5-core 50+25 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x50+25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "توزیع برق در تاسیسات ساختمانی و صنعتی"},
        "content_html": flex_35core_content("NYY Flexible", "50", "25", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.4", "1.2", "1.2", "2.1", "مطابق دیتاشیت", "مطابق دیتاشیت", "5.55 کیلوآمپر", "0.386 اهم بر کیلومتر", "0.78 اهم بر کیلومتر"),
    },
    {  # 10 - Flexible 3.5-core 35+16 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x35+16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC60332-1-2", "application": "خطوط اصلی شبکه فشار ضعیف و اتصال سیستم‌های سه‌فاز"},
        "content_html": flex_35core_content("NYY Flexible", "35", "16", "268", "مطابق دیتاشیت", "126", "مطابق دیتاشیت", "1.2", "1.0", "1.0", "1.9", "29", "1.8 کیلوگرم بر متر", "3.89 کیلوآمپر", "0.554 اهم بر کیلومتر", "1.21 اهم بر کیلومتر"),
    },
    {  # 11 - Flexible 3.5-core 25+16 NYY-O Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x25+16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "شبکه‌های توزیع فشار ضعیف"},
        "content_html": flex_35core_content("NYY-O Flexible", "25", "16", "192", "مطابق دیتاشیت", "126", "مطابق دیتاشیت", "1.2", "1.0", "مطابق دیتاشیت", "مطابق دیتاشیت", "26.7", "1.5 کیلوگرم بر متر", "2.78 کیلوآمپر", "0.78 اهم بر کیلومتر", "1.21 اهم بر کیلومتر"),
    },
    {  # 12 - Flexible 5x16 NYYJ Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "تامین برق تاسیسات سه‌فاز سنگین"},
        "content_html": flex_5core_content("NYYJ Flexible", "16", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.0", "1.8", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.21 اهم بر کیلومتر"),
    },
    {  # 13 - Flexible 5x10 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x10", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "کابل اصلی توزیع برق در تاسیسات صنعتی و ساختمانی"},
        "content_html": flex_5core_content("NYY Flexible", "10", "80", "مطابق دیتاشیت", "1", "1.8", "20.1", "821 گرم بر متر", "1.11 کیلوآمپر", "1.91 اهم بر کیلومتر"),
    },
    {  # 14 - Flexible 5x6 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x6", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "تغذیه تجهیزات پرقدرت سه‌فاز"},
        "content_html": flex_5core_content("NYMHY", "6", "84", "مطابق دیتاشیت", "0.8", "1.5", "15.71", "مطابق دیتاشیت", "666 آمپر", "3.3 اهم بر کیلومتر", voltage="450/750 ولت", test_voltage="2 کیلوولت"),
    },
    {  # 15 - Flexible 5x4 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x4", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "تغذیه تجهیزات الکتریکی در تاسیسات فشار ضعیف صنعتی و ساختمانی"},
        "content_html": flex_5core_content("NYMHY", "4", "56", "0.29", "0.8", "1.4", "مطابق دیتاشیت", "مطابق دیتاشیت", "444 آمپر", "4.95 اهم بر کیلومتر", voltage="300/500 ولت", test_voltage="2 کیلوولت"),
    },
    {  # 16 - Flexible 5x2.5 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x2.5", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5، IEC 60332-1-2", "application": "اتصال تجهیزات برقی سه‌فاز همراه با نول و ارت"},
        "content_html": flex_5core_content("NYMHY", "2.5", "50", "0.24", "0.8", "مطابق دیتاشیت", "12.04", "247 گرم بر متر", "278 آمپر", "7.98 اهم بر کیلومتر", voltage="300/500 ولت", test_voltage="2 کیلوولت"),
    },
    {  # 17 - Flexible 5x1.5 NYMHY
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x1.5", "conductor_material": "مس",
                   "standard": "IEC 60227، IEC 60228، ISIRI 607-5", "application": "اتصال ایمن لوازم برقی در شبکه‌های سه‌فاز و مدارهای کنترل"},
        "content_html": flex_5core_content("NYMHY", "1.5", "30", "0.24", "مطابق دیتاشیت", "مطابق دیتاشیت", "10.1", "166 گرم بر متر", "167 آمپر", "13.3 اهم بر کیلومتر", voltage="300/500 ولت", test_voltage="2 کیلوولت"),
    },
    {  # 18 - Flexible 4x25 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "هدایت جریان الکتریکی از منبع برق تا مصرف‌کننده در تاسیسات و تجهیزات برقی"},
        "content_html": flex_4core_content("NYY Flexible", "25", "189", "0.39", "1.2", "1", "1.8", "27.8", "1.6 کیلوگرم بر متر", "2.78 کیلوآمپر", "0.78 اهم بر کیلومتر"),
    },
    {  # 19 - Flexible 4x16 NYY Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "شبکه‌های فشار ضعیف با نیاز به کابل قابل خمش"},
        "content_html": flex_4core_content("NYY Flexible", "16", "126", "0.39", "1.0", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.78 کیلوآمپر", "1.21 اهم بر کیلومتر"),
    },
    {  # 20 - Flexible 4x10 NYY-O Flexible
        "category_name": "کابل افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x10", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "سیم‌کشی داخل ساختمان‌ها، مدارهای کنترل و محیط‌های صنعتی سبک"},
        "content_html": flex_4core_content("NYY-O Flexible", "10", "80", "0.39", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "18.3", "670 گرم بر متر", "1.11 کیلوآمپر", "1.91 اهم بر کیلومتر"),
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
    with open(os.path.join(DATA_DIR, "batch32_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch32_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch32_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
