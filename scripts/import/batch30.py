# -*- coding: utf-8 -*-
"""Batch 30: 20 products -- 5 more Legrand XS3 curve C single-pole
MCBs, 5 NA-DE emergency exit/lighting fixtures (title-only source
data), 2 EEC emergency lighting fixtures, and 8 Legrand Salbei
(Turkish economy line) switch/socket products."""
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

NETWORK_PARENT = "تجهیزات شبکه"
SWITCH_PARENT = "سایر تجهیزات کابل"

CURVE_DESC = {
    "B": "برای مدارهای حساس با جریان هجومی پایین مانند روشنایی و تجهیزات الکترونیکی ظریف",
    "C": "برای مدارهای عمومی و مصرف‌کننده‌های صنعتی با جریان هجومی متوسط",
}


def xs3_content(amp, curve):
    return f"""<p>کلید مینیاتوری تک پل {amp} آمپر کلاس {curve} لگراند از سری XS3 با ولتاژ عایقی ۴۰۰ ولت و ولتاژ ضربه‌ای ۴ کیلوولت، ظرفیت قطع ۴.۵ کیلوآمپر دارد. منحنی قطع {curve} این کلید {CURVE_DESC[curve]}.</p>
<p>ابعاد آن ارتفاع ۸۸.۸ میلی‌متر، عرض ۱۷.۸ میلی‌متر و عمق ۷۷.۳ میلی‌متر است و درجه حفاظت IP20 دارد. روی ریل استاندارد DIN نصب می‌شود و امکان اتصال با کابل مسی یا شینه توزیع را دارد. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


RECORDS = [
    {  # 1 - XS3 1P 25A C 403331
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از مدار کولر گازی و مصرف‌کننده‌های مشابه"},
        "content_html": xs3_content(25, "C"),
    },
    {  # 2 - XS3 1P 20A C 403330
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از مدارهای عمومی با بار متوسط"},
        "content_html": xs3_content(20, "C"),
    },
    {  # 3 - XS3 1P 6A C 403327
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از مدارهای حساس و کم‌مصرف خانگی و صنعت سبک"},
        "content_html": xs3_content(6, "C"),
    },
    {  # 4 - XS3 1P 10A C 403328
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از مدارهای روشنایی"},
        "content_html": xs3_content(10, "C"),
    },
    {  # 5 - XS3 1P 16A C 403329
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از پریزهای برق خانگی و اداری"},
        "content_html": xs3_content(16, "C"),
    },
    {  # 6 - NA-DE exit light 24LED
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "NA-DE", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نشانگر مسیر خروج اضطراری در ساختمان‌های عمومی و تجاری"},
        "content_html": """<p>چراغ خروج اضطراری NA-DE مدل 24LED یک تابلوی نشانگر مسیر خروج است که با ۲۴ عدد LED، علامت «خروج» را روشن نگه می‌دارد. این چراغ دارای باتری پشتیبان داخلی است که در زمان قطع برق شهر به‌طور خودکار وارد مدار شده و روشنایی نشانگر خروج را برای هدایت ایمن افراد به سمت درهای خروجی ساختمان تامین می‌کند.</p>
<p>این نوع تابلوی خروج اضطراری معمولاً بالای درهای خروج، در راهروها و پلکان‌های ساختمان‌های اداری، تجاری و عمومی نصب می‌شود تا در شرایط اضطراری مانند قطع برق یا آتش‌سوزی، مسیر تخلیه را به‌وضوح مشخص کند.</p>""",
    },
    {  # 7 - NA-DE emergency light 48LED
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "NA-DE", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "تامین روشنایی اضطراری فضاهای عمومی هنگام قطع برق"},
        "content_html": """<p>چراغ روشنایی اضطراری NA-DE مدل 48LED با ۴۸ عدد LED، روشنایی عمومی فضا را در زمان قطع برق تامین می‌کند. باتری پشتیبان داخلی این چراغ در حالت عادی شارژ می‌شود و به‌محض قطع برق شهر، به‌طور خودکار مدار روشنایی LED را فعال می‌کند.</p>
<p>این نوع چراغ روشنایی اضطراری در راهروها، پلکان‌ها و فضاهای عمومی ساختمان‌های اداری و تجاری نصب می‌شود تا در شرایط قطع برق، دید کافی برای تردد ایمن افراد فراهم شود.</p>""",
    },
    {  # 8 - NA-DE emergency light 24LED
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "NA-DE", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "تامین روشنایی اضطراری فضاهای عمومی هنگام قطع برق"},
        "content_html": """<p>چراغ روشنایی اضطراری NA-DE مدل 24LED با ۲۴ عدد LED، روشنایی عمومی فضا را در زمان قطع برق تامین می‌کند. باتری پشتیبان داخلی این چراغ در حالت عادی شارژ می‌شود و به‌محض قطع برق شهر، به‌طور خودکار مدار روشنایی LED را فعال می‌کند.</p>
<p>این نوع چراغ روشنایی اضطراری در راهروها، پلکان‌ها و فضاهای عمومی ساختمان‌های اداری و تجاری نصب می‌شود تا در شرایط قطع برق، دید کافی برای تردد ایمن افراد فراهم شود.</p>""",
    },
    {  # 9 - NA-DE exit light 305mm
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "NA-DE", "size_diameter": "305mm", "conductor_material": "",
                   "standard": "", "application": "نشانگر مسیر خروج اضطراری در ساختمان‌های عمومی و تجاری"},
        "content_html": """<p>چراغ خروج اضطراری NA-DE با عرض تابلوی ۳۰۵ میلی‌متر، یک نشانگر مسیر خروج با باتری پشتیبان داخلی است. در زمان قطع برق شهر، باتری داخلی به‌طور خودکار وارد مدار شده و علامت «خروج» را روشن نگه می‌دارد تا مسیر تخلیه ساختمان برای افراد قابل تشخیص باشد.</p>
<p>این تابلوی خروج اضطراری معمولاً بالای درهای خروج، در راهروها و پلکان‌های ساختمان‌های اداری، تجاری و عمومی نصب می‌شود.</p>""",
    },
    {  # 10 - NA-DE exit light 265mm
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "NA-DE", "size_diameter": "265mm", "conductor_material": "",
                   "standard": "", "application": "نشانگر مسیر خروج اضطراری در ساختمان‌های عمومی و تجاری"},
        "content_html": """<p>چراغ خروج اضطراری NA-DE با عرض تابلوی ۲۶۵ میلی‌متر، یک نشانگر مسیر خروج با باتری پشتیبان داخلی است. در زمان قطع برق شهر، باتری داخلی به‌طور خودکار وارد مدار شده و علامت «خروج» را روشن نگه می‌دارد تا مسیر تخلیه ساختمان برای افراد قابل تشخیص باشد.</p>
<p>این تابلوی خروج اضطراری معمولاً بالای درهای خروج، در راهروها و پلکان‌های ساختمان‌های اداری، تجاری و عمومی نصب می‌شود.</p>""",
    },
    {  # 11 - EEC PFL series exit light
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "ای ای سی", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 60598-2-22، تاییدیه TUV",
                   "application": "نشانگر مسیر خروج در ساختمان‌های عمومی، تجاری و صنعتی"},
        "content_html": """<p>چراغ خروج اضطراری سری پروفیلایت (PFL) شرکت EEC ترکیه به سه صورت زنجیری (آویز)، دیواری و سقفی روکار یا توکار قابل نصب است. بدنه آن از ABS ساخته شده و با ۱۰ عدد LED، علامت مسیر خروج (Exit) را روشن می‌کند تا افراد را در شرایط اضطراری به سمت درهای خروجی هدایت کند.</p>
<p>این محصول دارای درجه حفاظت IP33، توان مصرفی ۴ وات، باتری نیکل کادمیوم با ۳ ساعت پشتیبانی پس از قطع برق و کلاس عایقی ۲ است. در دو حالت Maintained (روشن دائم) و Non-Maintained (فقط هنگام قطع برق) قابل استفاده است و با ولتاژ ۲۲۰ تا ۲۵۰ ولت کار می‌کند. مطابق استاندارد EN 60598-2-22 تولید شده و دارای تاییدیه TUV است.</p>""",
    },
    {  # 12 - EEC ERL series emergency light
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "ای ای سی", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 60598-2-22، تاییدیه TUV",
                   "application": "روشنایی اضطراری راهرو و فضاهای عمومی هنگام قطع برق"},
        "content_html": """<p>چراغ روشنایی اضطراری سری ERL شرکت ترکیه‌ای EEC، در حالت کاری Non-Maintained عمل می‌کند؛ یعنی تا زمانی که به برق شهر متصل است، LED آن خاموش باقی می‌ماند و تنها با قطع برق، باتری نیکل کادمیوم داخلی وارد مدار شده و چراغ LED روشن می‌شود. نور تولیدی آن ۱۳۵ لومن به‌صورت خطی و بیضی‌شکل (Asymmetric) پخش می‌شود که برای روشن کردن مسیر عبور مناسب است.</p>
<p>بدنه این چراغ از ترموپلاستیک ساخته شده و فقط به‌صورت روکار قابل نصب است؛ محل‌های نصب روکار در پشت آن تعبیه شده‌اند. توان مصرفی آن ۳ وات، پشتیبانی باتری ۱ تا ۳ ساعت و ولتاژ کاری ۲۲۰ تا ۲۵۰ ولت است. مطابق استاندارد EN 60598-2-22 تولید شده و دارای تاییدیه کیفی TUV و CE است.</p>""",
    },
    {  # 13 - Legrand Salbei TV/SAT terminal socket 767128
        "category_name": "پریز آنتن", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60695-2-11", "application": "نقطه پایانی سیستم توزیع آنتن و ماهواره مرکزی"},
        "content_html": """<p>پریز انتهایی آنتن و ماهواره سالبی لگراند ۷۶۷۱۲۸ (ساخت ترکیه) یک پریز «پایان‌دهنده» (Sonlu) است که در نقطه انتهایی خطوط کابل‌کشی سیستم آنتن مرکزی نصب می‌شود و با مسدود کردن مسیر سیگنال، از بازگشت و انعکاس امواج جلوگیری می‌کند. این ویژگی کیفیت سیگنال دریافتی را بهبود داده و نویز تصویر و صدا را کاهش می‌دهد.</p>
<p>این پریز به‌صورت توکار با ظرفیت ۲ ماژول نصب می‌شود و بدنه سفید آن از مواد مقاوم در برابر رطوبت، گردوغبار و تغییرات دما ساخته شده است. برای منازل مسکونی، آپارتمان‌ها، ساختمان‌های اداری، هتل‌ها و مراکز آموزشی مناسب است.</p>""",
    },
    {  # 14 - Legrand Salbei antenna socket 767123
        "category_name": "پریز آنتن", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60695-2-11", "application": "توزیع سریالی سیگنال آنتن در ساختمان‌های چندواحدی"},
        "content_html": """<p>پریز آنتن سالبی لگراند ۷۶۷۱۲۳ (ساخت ترکیه) با ساختار حلقه‌ای (Loop-through)، امکان توزیع سیگنال آنتن به‌صورت سریالی از یک پریز به پریز بعدی را فراهم می‌کند که در ساختمان‌های چندواحدی هزینه سیم‌کشی را کاهش می‌دهد. تضعیف سیگنال آن ۱۵ دسی‌بل است که افت کیفیت تصویر و صدا را به حداقل می‌رساند.</p>
<p>این پریز به‌صورت توکار با ظرفیت ۲ ماژول نصب می‌شود و برای منازل مسکونی، آپارتمان‌ها، هتل‌ها، بیمارستان‌ها، مدارس و دفاتر اداری مناسب است.</p>""",
    },
    {  # 15 - Legrand Salbei network socket 767139
        "category_name": "پریز شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IP20، IEC 60695-2-11", "application": "اتصال شبکه محلی با کابل Cat6 STP"},
        "content_html": """<p>پریز شبکه تک پورت سالبی لگراند ۷۶۷۱۳۹ (ساخت ترکیه) از استاندارد Cat6 STP پشتیبانی می‌کند و انتقال داده تا سرعت ۱ گیگابیت بر ثانیه را با محافظت شیلد در برابر تداخل الکترومغناطیسی فراهم می‌کند. این پریز به‌صورت توکار نصب شده و پس از نصب کاملاً هم‌سطح دیوار قرار می‌گیرد.</p>
<p>بدنه آن از ترموپلاستیک باکیفیت با مقاومت مکانیکی بالا ساخته شده و درجه حفاظت آن IP20 است. با کابل شبکه Cat6 UTP یا سایر کابل‌های رده Cat6 سازگار است و برای شبکه‌های محلی خانگی و اداری مناسب است.</p>""",
    },
    {  # 16 - Legrand Salbei telephone socket 767129
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IP20، IEC 60884-1", "application": "اتصال خطوط تلفن ثابت آنالوگ"},
        "content_html": """<p>پریز تلفن سالبی لگراند ۷۶۷۱۲۹ (ساخت ترکیه) از نوع RJ11 با شش پین است که استاندارد رایج اتصال تلفن‌های ثابت آنالوگ به خطوط مخابراتی است. این پریز به‌صورت توکار نصب می‌شود و عمق مورد نیاز برای نصب آن تنها ۱۴.۵ میلی‌متر است.</p>
<p>بدنه آن از ترموپلاستیک ساخته شده که وزن سبک و مقاومت مناسب در برابر ضربه و حرارت دارد و به‌عنوان عایق الکتریکی نیز عمل می‌کند. درجه حفاظت آن IP20 است و برای فضاهای داخلی مسکونی و اداری مناسب است.</p>""",
    },
    {  # 17 - Legrand Salbei earthed socket 767114
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IP20، IEC 60884-1", "application": "پریز برق خانگی و اداری با اتصال ارت"},
        "content_html": """<p>پریز برق ارت‌دار سالبی لگراند ۷۶۷۱۱۴ (ساخت ترکیه) با سیستم ارت، ایمنی مدار و کاربر را در برابر برق‌گرفتگی افزایش می‌دهد. با ولتاژ نامی ۲۵۰ ولت و جریان نامی ۱۶ آمپر، توان تا ۳۶۸۰ وات را پشتیبانی می‌کند و برای وسایل خانگی و اداری مناسب است.</p>
<p>بدنه آن از آکریلونیتریل استایرن اکریلات (ASA) و پلی‌کربنات (PC) با مقاومت بالا در برابر حرارت، ضربه و اشعه UV ساخته شده است. ابعاد آن ۷۱×۷۱×۴۴.۶ میلی‌متر و وزن آن ۸۱ گرم است؛ درجه حفاظت آن IP20 و نصب آن توکار است.</p>""",
    },
    {  # 18 - Legrand Salbei 2-pole switch 767106
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IP20، IEC 60669-1", "application": "قطع و وصل هم‌زمان دو مدار روشنایی"},
        "content_html": """<p>کلید دو پل سالبی لگراند ۷۶۷۱۰۶ (ساخت ترکیه) امکان قطع و وصل هم‌زمان دو مدار را فراهم می‌کند. با ولتاژ ۲۵۰ ولت و جریان ۱۰ آمپر، توانایی کنترل مدارهای روشنایی با توان تا ۲۳۰۰ وات را دارد. ابعاد آن ۷۱×۷۱×۴۲ میلی‌متر و وزن آن ۷۰.۵ گرم است.</p>
<p>بدنه آن از ترموپلاستیک با مقاومت بالا در برابر ضربه، حرارت و رطوبت ساخته شده است و به‌صورت توکار نصب می‌شود. درجه حفاظت آن IP20 است و برای منازل، ادارات، هتل‌ها و مراکز تجاری مناسب است.</p>""",
    },
    {  # 19 - Legrand Salbei 1-pole two-way switch 767101
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IP20، IEC 60669-1", "application": "کنترل روشنایی از دو نقطه (کلید راه‌پله)"},
        "content_html": """<p>کلید یک پل تبدیل سالبی لگراند ۷۶۷۱۰۱ (ساخت ترکیه)، معروف به «کلید راه‌پله»، برای کنترل روشنایی از دو نقطه مانند راهروهای طولانی، پلکان‌های چندطبقه و پارکینگ‌های وسیع طراحی شده است. با ولتاژ ۲۵۰ ولت و جریان ۱۰ آمپر، توان تا ۲۳۰۰ وات را پشتیبانی می‌کند.</p>
<p>ابعاد آن ۷۱×۷۱×۴۲ میلی‌متر و وزن آن ۷۴ گرم است. بدنه از ترموپلاستیک باکیفیت با مقاومت در برابر ضربه، حرارت و رطوبت ساخته شده و به‌صورت توکار با درجه حفاظت IP20 نصب می‌شود.</p>""",
    },
    {  # 20 - Legrand Salbei 1-pole switch 767100
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IP20، IEC 60669-1", "application": "کنترل مدار روشنایی از یک نقطه"},
        "content_html": """<p>کلید تک پل سالبی لگراند ۷۶۷۱۰۰ (ساخت ترکیه) از دو بخش کادر و مکانیزم تشکیل شده که با اتصال به یکدیگر کلید کامل را می‌سازند و به‌صورت توکار روی دیوار نصب می‌شوند. با ولتاژ ۲۵۰ ولت و جریان ۱۰ آمپر، توان تا ۲۳۰۰ وات را پشتیبانی می‌کند.</p>
<p>ابعاد آن ۷۱×۷۱×۴۲ میلی‌متر و وزن آن ۷۰.۵ گرم است. بدنه از ترموپلاستیک با دوام بالا و مقاومت در برابر حرارت ساخته شده و درجه حفاظت آن IP20 است؛ برای منازل، ادارات، هتل‌ها، مدارس و مراکز درمانی مناسب است.</p>""",
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
    with open(os.path.join(DATA_DIR, "batch30_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch30_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch30_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
