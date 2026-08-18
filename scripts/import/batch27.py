# -*- coding: utf-8 -*-
"""Batch 27: 20 products -- 3 Legrand LCS3 patch panels (Cat8/Cat6A/Cat6
SFTP), 2 Legrand Plexo IP55 waterproof switch/socket, Fluke DSX 8000
cable tester, Cat6 UTP Khorasan Afsharnejad network cable, 4 NYRY
armored cables, 2 KNX cables (Simia, Hedayat), 2 Hedayat solar
photovoltaic cables, 5 NYSLCY shielded control cables."""
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
NETWORK_PARENT = "تجهیزات شبکه"
SWITCH_PARENT = "سایر تجهیزات کابل"


def nyry_armored_content(size_mm2, tar_count, tar_dia, sheath, dia, weight, resistance):
    return f"""<p>کابل آرموردار تک‌رشته {size_mm2} خراسان افشارنژاد (NYRY) از هادی مسی نیمه‌افشان کلاس ۲ ({tar_count} تار به قطر {tar_dia} میلی‌متر) با عایق و بدینگ PVC ساخته شده و زره سیم آلومینیومی (AWA) در برابر ضربه، فشار مکانیکی و آسیب جوندگان از آن محافظت می‌کند. روکش نهایی PVC مشکی به ضخامت {sheath} میلی‌متر مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است.</p>
<p>قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت و تست ولتاژ ۴ کیلوولت، در اتصال کوتاه تا ۱۶۰ درجه سانتی‌گراد را به‌صورت لحظه‌ای تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای نصب زیرزمینی، تونل‌های مترو و مسیرهایی با خطر آسیب مکانیکی مناسب است.</p>"""


def solar_content(size_mm2, weight):
    return f"""<p>کابل سولار فتوولتاییک تک‌رشته {size_mm2} هدایت (هدسان) از هادی مسی قلع‌اندود رشته‌ای کلاس ۵ (مطابق IEC 60228) ساخته شده که انعطاف‌پذیری و رسانایی بالایی دارد. عایق آن از XLPO کراس‌لینک‌شده و بدون هالوژن و روکش آن از HFFR (بدون هالوژن و کندسوز) است که در برابر اشعه UV (مطابق ISO 4892-2)، ازون و گسترش شعله (مطابق EN 60332-1-2) مقاوم است و با تمامی کانکتورهای رایج بازار سازگار است.</p>
<p>با ولتاژ نامی ۱۵۰۰ ولت DC (۱۰۰۰ ولت AC) و تست ولتاژ لحظه‌ای ۶۵۰۰ ولت AC، مطابق استانداردهای IEC 62930 و EN 50618 تولید شده است. وزن تقریبی آن {weight} است و در بازه دمایی ۴۰- تا ۱۲۰+ درجه سانتی‌گراد کار می‌کند و شعاع خمش مجاز آن ۶ برابر قطر کابل است. برای پروژه‌های خورشیدی مسکونی، تجاری، صنعتی و نیروگاه‌های خورشیدی روی پشت‌بام مناسب است.</p>"""


def nyslcy_content(cores_label, size_mm2, tar_count, tar_dia, ins_thickness, sheath, dia, weight, resistance, sc_current, colors):
    return f"""<p>کابل شیلددار افشان {cores_label} خراسان افشارنژاد (NYSLCY) با سطح مقطع {size_mm2} میلی‌متر مربع برای هر رشته، از هادی مسی افشان کلاس ۵ ({tar_count} تار به قطر {tar_dia} میلی‌متر) با عایق PVC به ضخامت {ins_thickness} میلی‌متر ساخته شده است. رنگ‌بندی رشته‌ها ({colors}) شناسایی و نصب دقیق را تسهیل می‌کند. زیر روکش نهایی، شیلد مسی بافته‌شده (۲۴ دسته، هر دسته ۶ تار به قطر ۰.۱۲ میلی‌متر) همراه با نوار آلومینیوم و پلی‌استر هر یک به ضخامت ۰.۰۳۶ میلی‌متر، محافظت کاملی در برابر تداخل الکترومغناطیسی فراهم می‌کند.</p>
<p>روکش نهایی PVC طوسی به ضخامت {sheath} میلی‌متر است. قطر کلی کابل حدود {dia} میلی‌متر و وزن آن حدود {weight} است. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است. با تست ولتاژ ۲ کیلوولت، جریان اتصال کوتاه لحظه‌ای تا {sc_current} را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای سیم‌کشی کنترل و فرمان در محیط‌های نویزی مناسب است.</p>"""


RECORDS = [
    {  # 1 - Legrand Cat8 SFTP patch panel LCS3 033782
        "category_name": "پچ پنل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "دیتاسنترها و شبکه‌های با نیاز به پهنای باند بسیار بالا و حداقل نویز"},
        "content_html": """<p>پچ پنل اصلی Cat8 SFTP لگراند از سری LCS3 (مدل ۰۳۳۷۸۲)، ۲۴ پورت RJ45 با محافظ SFTP دارد و از بدنه فولاد گالوانیزه DC01 مقاوم در برابر ضربه و خوردگی ساخته شده است. با پشتیبانی از سرعت انتقال داده تا ۴۰ گیگابیت بر ثانیه و پهنای باند ۱۶۰۰ تا ۲۰۰۰ مگاهرتز، بالاترین استاندارد کابل شبکه فعلی را پوشش می‌دهد.</p>
<p>نصب آن با فناوری Soluclip بدون نیاز به پیچ انجام می‌شود و ۴ کاست ۶ پورتی آن به‌سادگی با فشردن یک دکمه قابل تعویض هستند. به همراه ۲۴ کیستون، برچسب رنگی و دفترچه راهنما عرضه می‌شود و در بازه دمایی ۴۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای بهره‌مندی کامل از سرعت Cat8، کابل شبکه و کیستون‌های متصل به آن نیز باید هم‌رده Cat8 باشند.</p>""",
    },
    {  # 2 - Legrand Cat6A SFTP patch panel LCS3 033772
        "category_name": "پچ پنل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "دیتاسنترها و شبکه‌های سازمانی با نیاز به سرعت بالا و پشتیبانی PoE"},
        "content_html": """<p>پچ پنل اصلی Cat6A SFTP لگراند از سری LCS3 (مدل ۰۳۳۷۷۲)، ۲۴ پورت RJ45 با روکش پلاستیکی زرد و محافظ فویلی S/FTP دارد که در برابر تداخل الکترومغناطیسی (EMI) و نویز محافظت می‌کند. سرعت انتقال داده آن ۱۰ گیگابیت بر ثانیه و پهنای باند آن ۵۰۰ مگاهرتز است و برای ارتباط بین رک‌ها در طبقات مختلف مناسب است.</p>
<p>بدنه ریل آن از ورق گالوانیزه ضدزنگ با سیستم اتصال خودکار به زمین ساخته شده و ۴ یونیت ۶ پورتی به همراه نظم‌دهنده کابل پشتی دارد. بدون نیاز به پیچ و مهره، با قفل‌های طرفین روی رک ۱۹ اینچی نصب می‌شود و از فناوری Power over Ethernet تا ۹۰ وات پشتیبانی می‌کند؛ مناسب برای دوربین‌های امنیتی و تلفن‌های VoIP. در بازه دمایی ۲۵- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و به همراه ریل، برچسب، ۲۴ کیستون و دفترچه راهنما عرضه می‌شود.</p>""",
    },
    {  # 3 - Legrand Cat6 SFTP patch panel LCS3 033762
        "category_name": "پچ پنل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "دیتاسنترها و شبکه‌های سازمانی با نیاز به محافظت در برابر نویز"},
        "content_html": """<p>پچ پنل اصلی Cat6 SFTP لگراند از سری LCS3 (مدل ۰۳۳۷۶۲)، ۲۴ پورت با کیستون‌های شیلددار و فویل مسی دارد که در قالب ۴ یونیت ۶ پورتی سازمان‌دهی شده است. ساختار فلزی گالوانیزه آن نویز را به زمین منتقل می‌کند و سیستم اتصال خودکار به زمین (grounding) پایداری شبکه را تضمین می‌کند. سرعت انتقال داده آن ۱ گیگابیت بر ثانیه و پهنای باند آن ۲۵۰ مگاهرتز است.</p>
<p>نصب آن بدون پیچ روی رک‌های استاندارد ۱۹ اینچی انجام می‌شود و نظم‌دهنده کابل در پشت پنل، کابل‌ها را در حین تعمیر و نگهداری منظم نگه می‌دارد. برچسب‌های رنگی برای شناسایی آسان کابل‌ها و پورت‌ها تعبیه شده و در بازه دمایی ۲۵- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. به همراه ریل، برچسب، کیستون، ۴ یونیت ۶ پورتی و دفترچه راهنما عرضه می‌شود؛ برای بهترین عملکرد، کابل شبکه و کیستون متصل نیز باید از نوع Cat6 SFTP باشند.</p>""",
    },
    {  # 4 - Legrand Plexo IP55 earthed socket grey 069833
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، IEC 60884-1", "application": "نصب توکار در محیط‌های مرطوب و صنعتی مانند آشپزخانه‌های صنعتی و کارگاه‌ها"},
        "content_html": """<p>پریز برق ارت‌دار توکار طوسی ضد آب پلکسو لگراند ۰۶۹۸۳۳ با استاندارد IP55 برای نصب توکار طراحی شده و در برابر نفوذ گردوغبار و پاشش آب از تمامی جهات محافظت می‌کند. درب محافظ آن با مکانیزم ساده از ورود آب به داخل پریز جلوگیری می‌کند و واشرهای سیلیکونی و درپوش‌های آن آب‌بندی کامل مکانیزم را تضمین می‌کنند.</p>
<p>با ولتاژ ۲۵۰ ولت و جریان ۱۶ آمپر، برای فضاهای صنعتی، مسکونی و اداری مرطوب مانند آشپزخانه‌های صنعتی و کارگاه‌ها مناسب است. بدنه آن با مواد مقاوم در برابر حرارت و مواد شیمیایی و شوینده‌های قوی ساخته شده و طراحی ماژولار آن امکان تعویض قطعات آسیب‌دیده را بدون تعویض کل مکانیزم فراهم می‌کند. در صورت نبود قوطی پیچ‌دار، با ساپورت چنگکی مخصوص پلکسو نیز قابل نصب است و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 5 - Legrand Plexo IP55 2-pole switch grey 069815
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، NF EN 60669-1، NBN EN 60669-1، CEI 60669-1",
                   "application": "نصب توکار در محیط‌های مرطوب مانند حمام، استخر و موتورخانه"},
        "content_html": """<p>کلید دو پل توکار طوسی ضد آب پلکسو لگراند ۰۶۹۸۱۵ از ترکیب کادر توکار طوسی پلکسو ۰۶۹۶۸۱ و مغزی کلید دو پل طوسی پلکسو ۰۶۹۵۲۵ تشکیل شده است. واشرهای سیلیکونی و لاستیکی آن از نفوذ آب و گردوغبار به مکانیزم جلوگیری می‌کنند و استاندارد IP55 آن تضمین می‌کند در برابر پاشش آب از هر جهت و ورود ذرات گردوغبار مقاوم است.</p>
<p>با ولتاژ ۲۵۰ ولت و جریان ۱۰ آمپر، برای محیط‌های صنعتی، آزمایشگاه‌ها، اتاق‌های تمیز و فضاهای مرطوب مانند حمام، استخر و موتورخانه مناسب است. بدنه آن از پلی‌پروپیلن تقویت‌شده با مقاومت بالا در برابر ضربه و شرایط محیطی ساخته شده و برای نصب توکار طراحی شده است. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 6 - Fluke DSX 8000 cable tester
        "category_name": "تجهیزات تست شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "فلوک", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "صدور گواهی و عیب‌یابی کابل‌کشی ساختار یافته شبکه تا رده Cat8.2"},
        "content_html": """<p>دستگاه تست فلوک DSX 8000 از خانواده جدید Versiv شرکت فلوک نتورکس آمریکا است که قابلیت تست و صدور گواهی کلیه کابل‌های شبکه مسی تا رده Cat8.2 را دارد. نسبت به مدل‌های پیشین این خانواده، زمان تست کابل کاهش یافته و تست یک کابل Cat6A تنها در حدود ۸ ثانیه انجام می‌شود که سرعت پروژه‌های صدور گواهی شبکه را به‌طور محسوسی افزایش می‌دهد.</p>
<p>نسخه به‌روزشده این محصول با نام فلوک DSX2 8000 نیز در بازار عرضه شده که همان پلتفرم را با بهبودهایی ادامه می‌دهد. این دستگاه برای تکنسین‌ها و پیمانکاران شبکه که نیاز به تایید استاندارد و عیب‌یابی سریع زیرساخت کابل‌کشی ساختار یافته دارند طراحی شده است.</p>""",
    },
    {  # 7 - Cat6 UTP Khorasan Afsharnejad network cable
        "category_name": "کابل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "شبکه‌های محلی (LAN) خانگی و تجاری با نیاز به هزینه اقتصادی"},
        "content_html": """<p>کابل شبکه Cat6 UTP خراسان افشارنژاد از چهار زوج سیم مسی تابیده بدون شیلد و فویل تشکیل شده و امکان انتقال داده با سرعت ۱ گیگابیت بر ثانیه و پهنای باند ۲۵۰ مگاهرتز را فراهم می‌کند. در تست فلوک این کابل هدروم بالای ۵ دسی‌بل در حالت پرمننت لینک ثبت شده است.</p>
<p>عدم استفاده از شیلد، وزن کمتر و انعطاف‌پذیری بیشتری نسبت به کابل‌های FTP به آن می‌دهد و هزینه آن نسبت به کابل‌های شیلددار پایین‌تر است؛ به همین دلیل برای پروژه‌های خانگی و تجاری با محدودیت بودجه مناسب است. عایق داخلی و روکش نهایی آن از جنس PVC آبی‌رنگ است، در قرقره‌های ۳۰۵ متری عرضه می‌شود و در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 8 - NYRY armored 1x240
        "category_name": "کابل زره‌دار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "240", "conductor_material": "مس",
                   "standard": "IEC 60502-1، ISIRI 3569-1، ISIRI 3084", "application": "زیرزمین، تونل‌های مترو و سیستم‌های توزیع برق کارخانه‌ها"},
        "content_html": nyry_armored_content("240", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت"),
    },
    {  # 9 - NYRY armored 1x185
        "category_name": "کابل زره‌دار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "185", "conductor_material": "مس",
                   "standard": "IEC 60502-1، DIN VDE 0271، ISIRI 3569-1", "application": "شبکه‌های توزیع شهری، تابلوهای صنعتی و نصب‌های دفن‌شده"},
        "content_html": nyry_armored_content("185", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "2.5 کیلوگرم بر متر", "مطابق دیتاشیت"),
    },
    {  # 10 - NYRY armored 1x150
        "category_name": "کابل زره‌دار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "150", "conductor_material": "مس",
                   "standard": "IEC 60502-1، ISIRI 3084، ISIRI 3569-1", "application": "تامین توان اصلی در کارخانجات، تاسیسات صنعتی و شبکه‌های توزیع شهری"},
        "content_html": nyry_armored_content("150", "37", "2.2", "1.9", "28.8", "2000 کیلوگرم بر کیلومتر", "0.124 اهم بر کیلومتر"),
    },
    {  # 11 - NYRY armored 1x300
        "category_name": "کابل زره‌دار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "300", "conductor_material": "مس",
                   "standard": "IEC 60502-1، ISIRI 3569-1، ISIRI 3084", "application": "تاسیسات صنعتی، کارخانه‌ها و نصب زیرزمینی با نیاز به جریان بالا"},
        "content_html": nyry_armored_content("300", "61", "2.47", "2.2", "38", "3950 کیلوگرم بر کیلومتر", "0.0601 اهم بر کیلومتر"),
    },
    {  # 12 - KNX cable Simia
        "category_name": "کابل KNX", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "سیمیا", "size_diameter": "2x2x0.8", "conductor_material": "مس",
                   "standard": "IEC 60332-1", "application": "سیم‌کشی سیستم‌های کنترل و مدیریت هوشمند ساختمان مانند نورپردازی، گرمایش و تهویه"},
        "content_html": """<p>کابل هوشمندسازی KNX سیمیا با کد شناسایی J-Y(St)Yh، از دو زوج (۴ رشته) هادی مسی مفتولی کلاس ۱ به قطر ۰.۸ میلی‌متر با رنگ‌بندی مشکی-قرمز و سفید-زرد تشکیل شده است. برای حفظ یکپارچگی سیگنال، هر زوج با یک نوار آلومینیوم/پلی‌استر و کل چهار رشته نیز با یک شیلد کلی مشابه پوشانده شده که در کنار هم محافظت دوگانه در برابر تداخل الکترومغناطیسی (EMI) ایجاد می‌کنند. سه سیم تخلیه قلع‌اندود به قطر ۰.۴ میلی‌متر (دو عدد برای زوج‌ها و یک عدد کلی) برای اتصال به زمین و دفع نویز تعبیه شده است.</p>
<p>مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد حداکثر ۳۷.۵ اهم بر کیلومتر است. روکش نهایی PVC سبز رنگ آن مطابق IEC 60332-1 در برابر گسترش شعله مقاوم است. وزن آن حدود ۷.۲ کیلوگرم بر کلاف ۱۰۰ متری و قطر کلی آن ۷.۶ میلی‌متر است. در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند (حداقل دمای نصب ۵- درجه) و برای سیم‌کشی شبکه کنترل و اتوماسیون داخلی ساختمان مناسب است.</p>""",
    },
    {  # 13 - KNX cable Hedayat
        "category_name": "کابل KNX", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "هدسان", "size_diameter": "0.8", "conductor_material": "مس",
                   "standard": "", "application": "ارتباط با تجهیزات مدیریت ساختمان هوشمند شامل روشنایی، تهویه و سیستم صوتی"},
        "content_html": """<p>کابل KNX هدایت از چهار رشته سیم مفتول مسی به‌صورت دو زوج به‌هم‌تابیده با سطح مقطع ۰.۸ میلی‌متر تشکیل شده که هر زوج جداگانه با فویل آلومینیومی پوشانده شده است. علاوه بر آن، روی کل مجموعه زوج‌ها نیز یک لایه فویل آلومینیومی و روکش پلی‌استر قرار گرفته که محافظت مضاعفی در برابر نویز ایجاد می‌کند. زوج اول به رنگ قرمز/مشکی، اصلی‌ترین زوج برای انتقال برق و دیتای پروتکل KNX است؛ زوج دوم به رنگ زرد/سفید معمولاً بلااستفاده است، اما در برخی سیستم‌ها برای انتقال توان کمکی به کار می‌رود.</p>
<p>روکش نهایی این کابل از PVC سبز رنگ ساخته شده است. سرعت انتقال اطلاعات استاندارد پروتکل KNX روی این کابل ۹۶۰۰ بیت بر ثانیه است. برای سیم‌کشی سیستم‌های مدیریت ساختمان هوشمند از جمله کنترل روشنایی، تهویه مطبوع و سیستم‌های صوتی مناسب است.</p>""",
    },
    {  # 14 - Solar cable 1x4 Hedayat
        "category_name": "کابل سولار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "هدسان", "size_diameter": "1x4", "conductor_material": "مس",
                   "standard": "IEC 62930، ISIRI 15613، IEC 60228، EN 50618، EN 60332-1-2، ISO 4892-2، IEC 60811-506",
                   "application": "پروژه‌های خورشیدی مسکونی، تجاری، صنعتی و نیروگاه‌های خورشیدی روی پشت‌بام"},
        "content_html": solar_content("۱×۴", "60 گرم بر متر"),
    },
    {  # 15 - Solar cable 1x6 Hedayat
        "category_name": "کابل سولار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "هدسان", "size_diameter": "1x6", "conductor_material": "مس",
                   "standard": "IEC 62930، ISIRI 15613، IEC 60228، EN 50618، EN 60332-1-2، ISO 4892-2، IEC 60811-506، IEC 60216-1,2",
                   "application": "پروژه‌های خورشیدی مسکونی، تجاری، صنعتی و نیروگاه‌های خورشیدی روی پشت‌بام"},
        "content_html": solar_content("۱×۶", "مطابق دیتاشیت"),
    },
    {  # 16 - NYSLCY shielded 5x1.5
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x1.5", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "سیم‌کشی کنترل و فرمان سه‌فاز به همراه نول و ارت در محیط‌های نویزی"},
        "content_html": nyslcy_content("۵×۱.۵", "1.5", "30", "0.24", "0.7", "1.2", "10.74", "173 گرم بر متر", "13.3 اهم بر کیلومتر", "0.2 کیلوآمپر", "فاز: مشکی، قرمز، زرد؛ نول: آبی؛ ارت: سبز/زرد"),
    },
    {  # 17 - NYSLCY shielded 5x1
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x1", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "سیم‌کشی کنترل و فرمان سه‌فاز به همراه نول و ارت در محیط‌های نویزی"},
        "content_html": nyslcy_content("۵×۱", "1", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.1", "9.3", "131 گرم بر متر", "19.50 اهم بر کیلومتر", "مطابق دیتاشیت", "فاز: آبی، قرمز، قهوه‌ای؛ نول: مشکی؛ ارت: سبز/زرد"),
    },
    {  # 18 - NYSLCY shielded 4x2.5
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x2.5", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "سیم‌کشی کنترل و فرمان در پروژه‌های ساختمانی و صنعتی بدون نیاز به ارت"},
        "content_html": nyslcy_content("۴×۲.۵", "2.5", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت", "1.2", "11.44", "198 گرم بر متر", "مطابق دیتاشیت", "مطابق دیتاشیت", "فاز: مشکی، قرمز، زرد؛ نول: آبی"),
    },
    {  # 19 - NYSLCY shielded 4x1.5
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x1.5", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "سیم‌کشی کنترل و فرمان در ساختمان‌های بدون چاه ارت"},
        "content_html": nyslcy_content("۴×۱.۵", "1.5", "30", "0.24", "مطابق دیتاشیت", "1.1", "9.7", "139 گرم بر متر", "13.3 اهم بر کیلومتر", "0.2 کیلوآمپر", "فاز: مشکی، زرد، قرمز؛ نول: آبی"),
    },
    {  # 20 - NYSLCY shielded 4x1
        "category_name": "کابل شیلددار", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4x1", "conductor_material": "مس",
                   "standard": "IEC 60227-7، DIN VDE 0245", "application": "سیم‌کشی کنترل و فرمان در پروژه‌های ساختمانی و صنعتی بدون نیاز به ارت"},
        "content_html": nyslcy_content("۴×۱", "1", "32", "0.19", "0.6", "1", "8.35", "مطابق دیتاشیت", "19.50 اهم بر کیلومتر", "0.2 کیلوآمپر", "زرد، آبی، قرمز و مشکی"),
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
    with open(os.path.join(DATA_DIR, "batch27_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch27_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch27_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
