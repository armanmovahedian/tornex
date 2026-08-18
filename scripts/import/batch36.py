# -*- coding: utf-8 -*-
"""Batch 36: 20 products -- 4 Khorasan Afsharnejad NYYO 3.5-core
ground cables, 11 NYY single-core ground cables, one NYY-J cooler
cable, and 4 Legrand Mosaic/Plexo accessories."""
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
SWITCH_PARENT = "سایر تجهیزات کابل"


def zamini_35core_content(phase_mm2, neutral_mm2, phase_desc, neutral_desc, phase_ins, neutral_ins, sheath, dia,
                           weight, sc_current, res_phase, res_neutral, colors="فاز: مشکی، زرد، قرمز؛ نول: آبی"):
    return f"""<p>کابل زمینی سه‌ونیم‌رشته {phase_mm2}+{neutral_mm2} خراسان افشارنژاد (NYYO) از سه رشته فاز با سطح مقطع {phase_mm2} میلی‌متر مربع ({phase_desc}) و یک رشته نول با سطح مقطع {neutral_mm2} میلی‌متر مربع ({neutral_desc}) ساخته شده است. رنگ‌بندی رشته‌ها ({colors}) شناسایی و نصب دقیق را تسهیل می‌کند. عایق PVC فاز و نول به ترتیب {phase_ins} و {neutral_ins} میلی‌متر ضخامت دارد و یک نوار پلی‌استر (Pet-Tape) دور رشته‌ها پیچیده شده که در برابر ضربات و فشارهای مکانیکی محافظت می‌کند.</p>
<p>روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی فاز {res_phase} و نول {res_neutral} در دمای ۲۰ درجه سانتی‌گراد است. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت و تست ولتاژ ۴ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و برای نصب ثابت زمینی مناسب است.</p>"""


def zamini_1core_content(size_mm2, tar_count, tar_dia, ins, sheath, dia, weight, sc_current, resistance):
    return f"""<p>کابل زمینی تک‌رشته {size_mm2} خراسان افشارنژاد (NYY) از هادی نیمه‌افشان کلاس ۲ ({tar_count} تار به قطر {tar_dia} میلی‌متر) با عایق PVC به ضخامت {ins} میلی‌متر ساخته شده است. روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است.</p>
<p>قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت و تست ولتاژ ۴ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و برای نصب ثابت در فضاهای بدون پیچ‌وخم مناسب است.</p>"""


def cooler_content(size_mm2, tar_dia, ins, sheath, dia, weight, sc_current, resistance):
    return f"""<p>کابل کولر آبی ۵×{size_mm2} خراسان افشارنژاد (NYY-J) از پنج رشته هم‌سطح‌مقطع {size_mm2} میلی‌متر مربع (فاز، نول و ارت) با هادی مفتولی به قطر {tar_dia} میلی‌متر در هر رشته ساخته شده و به رنگ‌های استاندارد قرمز، زرد، مشکی، آبی و زرد/سبز (ارت) تولید می‌شود. عایق هر رشته از PVC به ضخامت {ins} میلی‌متر است و مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است.</p>
<p>روکش نهایی PVC سفید به ضخامت {sheath} میلی‌متر در برابر اشعه UV و شرایط محیطی بیرونی مقاوم است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی ۳۰۰/۵۰۰ ولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای اتصال برق کولرهای آبی در پشت‌بام و فضاهای باز مناسب است.</p>"""


RECORDS = [
    {  # 1 - Ground 3.5-core 70+35 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x70+35", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب در مسیرهای مستقیم و زیرزمینی بدون نیاز به خمش"},
        "content_html": zamini_35core_content("70", "35", "نیمه‌افشان کلاس ۲ (۱۹ تار به قطر ۲.۱۶ میلی‌متر)", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۴۷ میلی‌متر)", "1.4", "1.2", "1.9", "30.5", "2.7 کیلوگرم بر متر", "مطابق دیتاشیت", "0.268 اهم بر کیلومتر", "0.524 اهم بر کیلومتر"),
    },
    {  # 2 - Ground 3.5-core 50+25 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x50+25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "تاسیسات برقی ساختمانی و صنعتی با نیاز به ساختار سکتوری"},
        "content_html": zamini_35core_content("50", "25", "نیمه‌افشان کلاس ۲ سکتوری (۱۹ تار به قطر ۱.۸ میلی‌متر)", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۱ میلی‌متر)", "1.4", "1.2", "1.9", "28.16", "2 کیلوگرم بر متر", "5.55 کیلوآمپر", "0.387 اهم بر کیلومتر", "0.727 اهم بر کیلومتر"),
    },
    {  # 3 - Ground 3.5-core 35+16 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x35+16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "برق‌کشی زیرزمینی و زمینی در مسافت‌های طولانی"},
        "content_html": zamini_35core_content("35", "16", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۴۷ میلی‌متر)", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۱.۶۸ میلی‌متر)", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.9", "28.3", "1.9 کیلوگرم بر متر", "مطابق دیتاشیت", "0.524 اهم بر کیلومتر", "1.15 اهم بر کیلومتر"),
    },
    {  # 4 - Ground 3.5-core 25+16 NYYO
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "3x25+16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های نصب ثابت با نیاز به رشته نول جداگانه"},
        "content_html": zamini_35core_content("25", "16", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۲.۱ میلی‌متر)", "نیمه‌افشان کلاس ۲ (۷ تار به قطر ۱.۶۸ میلی‌متر)", "1.2", "1.0", "1.8", "25.7", "1.5 کیلوگرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت"),
    },
    {  # 5 - Ground 1x300 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x300", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "پروژه‌های برقی وسیع با نیاز به جریان بسیار بالا"},
        "content_html": zamini_1core_content("300", "61", "2.47", "2.4", "2", "31.25", "3.3 کیلوگرم بر متر", "33.3 کیلوآمپر", "0.0601 اهم بر کیلومتر"),
    },
    {  # 6 - Ground 1x240 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x240", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "کابل‌کشی ساختمانی درون دیوار و سقف بدون نیاز به انعطاف"},
        "content_html": zamini_1core_content("240", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "26.6 کیلوآمپر", "0.0754 اهم بر کیلومتر"),
    },
    {  # 7 - Ground 1x185 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x185", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "توزیع برق فشار ضعیف در فضاهای ثابت"},
        "content_html": zamini_1core_content("185", "37", "مطابق دیتاشیت", "2", "1.8", "25.06", "2.1 کیلوگرم بر متر", "20.5 کیلوآمپر", "0.0991 اهم بر کیلومتر"),
    },
    {  # 8 - Ground 1x150 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x150", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271، IEC 60332-1-2", "application": "نصب ثابت با کمترین افت ولتاژ در حمل جریان بالا"},
        "content_html": zamini_1core_content("150", "37", "2.2", "1.8", "1.7", "22.55", "1.7 کیلوگرم بر متر", "مطابق دیتاشیت", "0.124 اهم بر کیلومتر"),
    },
    {  # 9 - Ground 1x120 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x120", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228", "application": "پروژه‌های سنگین با نیاز به انتقال جریان‌های قوی"},
        "content_html": zamini_1core_content("120", "37", "مطابق دیتاشیت", "1.6", "1.6", "20.54", "1.32 کیلوگرم بر متر", "13.3 کیلوآمپر", "0.153 اهم بر کیلومتر"),
    },
    {  # 10 - Ground 1x95 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x95", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های سنگین با نیاز به نصب در مسیرهای مستقیم"},
        "content_html": zamini_1core_content("95", "19", "2.47", "1.6", "مطابق دیتاشیت", "18.67", "1.1 کیلوگرم بر متر", "مطابق دیتاشیت", "0.193 اهم بر کیلومتر"),
    },
    {  # 11 - Ground 1x70 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x70", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های صنعتی با نیاز به تحمل بار سنگین و جریان بالا"},
        "content_html": zamini_1core_content("70", "19", "2.11", "1.4", "1.5", "16.35", "790 گرم بر متر", "7.77 کیلوآمپر", "0.268 اهم بر کیلومتر"),
    },
    {  # 12 - Ground 1x50 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x50", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت با عملکرد مطمئن در شرایط محیطی سخت"},
        "content_html": zamini_1core_content("50", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.4", "1.4", "14.5", "577 گرم بر متر", "5.55 کیلوآمپر", "0.387 اهم بر کیلومتر"),
    },
    {  # 13 - Ground 1x35 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x35", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب ثابت در فضاهای محدود"},
        "content_html": zamini_1core_content("35", "7", "2.47", "1.2", "1.4", "12.61", "425 گرم بر متر", "3.89 کیلوآمپر", "0.524 اهم بر کیلومتر"),
    },
    {  # 14 - Ground 1x25 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x25", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "پروژه‌های ساختمانی و تاسیسات برقی با ولتاژ فشار ضعیف"},
        "content_html": zamini_1core_content("25", "7", "2.1", "مطابق دیتاشیت", "1.4", "11.5", "325 گرم بر متر", "2.78 کیلوآمپر", "0.727 اهم بر کیلومتر"),
    },
    {  # 15 - Ground 1x16 NYY
        "category_name": "کابل زمینی", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x16", "conductor_material": "مس",
                   "standard": "IEC 60502-1، IEC 60228، INSO 3569-1، DIN VDE 0271", "application": "نصب‌های دائمی بدون نیاز به جابه‌جایی کابل"},
        "content_html": zamini_1core_content("16", "7", "1.68", "1.0", "1.4", "9.84", "225 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت"),
    },
    {  # 16 - Cooler cable 5x1.5 NYY-J
        "category_name": "کابل کولری", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x1.5", "conductor_material": "مس",
                   "standard": "IEC 60332-1-2", "application": "اتصال برق کولرهای آبی و سیستم‌های تهویه در فضای باز"},
        "content_html": cooler_content("1.5", "1.37", "0.7", "1.1", "مطابق دیتاشیت", "163 گرم بر متر", "100 آمپر", "12.1 اهم بر کیلومتر"),
    },
    {  # 17 - Legrand Mosaic hook support 080261
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60695-2-11", "application": "نصب بدون پیچ مکانیزم‌های دو ماژول موزائیک لگراند"},
        "content_html": """<p>ساپورت (حلقه) چنگکی موزائیک لگراند ۰۸۰۲۶۱ برای نصب سریع و بدون پیچ مکانیزم‌های ۲ ماژول موزائیک لگراند در دیوارهای گچی و سیمانی طراحی شده است. مکانیزم و کادر با کمک چنگک‌های جانبی این ساپورت به‌صورت محکم درون قوطی برق ثابت می‌شوند و با کادرها و مکانیزم‌های استاندارد موزائیک لگراند سازگار است.</p>
<p>بدنه آن از فولاد گالوانیزه با پوشش Galfan (ترکیب روی و آلومینیوم) ساخته شده که مقاومت بالایی در برابر زنگ‌زدگی و خوردگی دارد. ابعاد آن ۷۴×۴۰.۵ میلی‌متر است و مطابق استاندارد IEC 60695-2-11 خاصیت خودخاموش‌شوندگی در دمای ۶۵۰ درجه سانتی‌گراد به مدت ۳۰ ثانیه دارد. در بازه دمایی ۵- تا ۵۰+ درجه سانتی‌گراد کار می‌کند و برای منازل، ادارات، مراکز آموزشی و ایستگاه‌های مترو مناسب است.</p>""",
    },
    {  # 18 - Legrand Plexo surface box 069651
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NF C 61-314، IEC 60884-1", "application": "نصب روکار مکانیزم‌های پلکسو در محیط‌های مرطوب و صنعتی"},
        "content_html": """<p>باکس روکار طوسی ضد آب پلکسو لگراند ۰۶۹۶۵۱ با استاندارد IP55 در برابر نفوذ آب، گردوغبار و پاشش مستقیم آب محافظت می‌کند و برای نصب در فضای باز و شرایط جوی سخت مناسب است. از پلی‌پروپیلن تقویت‌شده ساخته شده که در برابر مواد شیمیایی مانند اسیدهای ملایم، روغن‌ها و مواد تمیزکننده صنعتی مقاوم است.</p>
<p>طراحی ماژولار آن امکان ترکیب با انواع مکانیزم‌های پلکسو یا موزائیک را فراهم می‌کند؛ برای مثال با مغزی پریز پلکسو کد ۰۶۹۵۷۱ یک پریز روکار کامل می‌سازد. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند و مطابق استانداردهای NF C 61-314 و IEC 60884-1 تولید شده است.</p>""",
    },
    {  # 19 - Legrand Plexo earthed socket mechanism 069571
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، IEC 60884-1", "application": "پریز برق ضد آب در استخر، حمام و آشپزخانه صنعتی"},
        "content_html": """<p>مغزی پریز برق ارت‌دار طوسی ضد آب پلکسو لگراند ۰۶۹۵۷۱ با بدنه پلی‌کربنات و پوشش ABS، درجه حفاظت IP55 دارد که در برابر ورود گردوغبار و فشار آب از همه جهات محافظت می‌کند. با ولتاژ ۲۲۰ تا ۲۵۰ ولت و جریان ۱۶ آمپر، دارای اتصال ارت برای ایمنی بالا در محیط‌های صنعتی و مرطوب است.</p>
<p>این مغزی پریز به‌صورت توکار با کادر لگراند کد ۰۶۹۶۸۱ یا به‌صورت روکار همراه با باکس روکار کد ۰۶۹۶۵۱ قابل نصب است. طراحی ماژولار آن امکان تعویض تنها قطعه معیوب را فراهم می‌کند و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند؛ برای استخرها، حمام‌ها، موتورخانه‌ها و آشپزخانه‌های صنعتی مناسب است.</p>""",
    },
    {  # 20 - Legrand 8-module MCB distribution box
        "category_name": "جعبه فیوز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب توکار در ورودی ساختمان یا واحد برای جای‌گیری فیوزهای مینیاتوری"},
        "content_html": """<p>جعبه مینیاتوری لگراند ۸ ماژول (تابلو برق انتهایی) یک ردیفه است و ۸ عدد فیوز مینیاتوری را در خود جای می‌دهد. این جعبه معمولاً در ورودی ساختمان‌ها یا هر واحد نصب می‌شود تا هم از فیوزهای مینیاتوری محافظت کند و هم از نفوذ مایعات به آن‌ها جلوگیری نماید.</p>
<p>بدنه آن از پلاستیک سفید ساخته شده و به‌صورت توکار نصب می‌شود. مدل بزرگ‌تر همین خانواده، جعبه فیوز مینیاتوری ۱۲ ماژول لگراند است که ظرفیت بیشتری برای پروژه‌های با تعداد مدار بالاتر فراهم می‌کند.</p>""",
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
    with open(os.path.join(DATA_DIR, "batch36_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch36_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch36_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
