# -*- coding: utf-8 -*-
"""Batch 20: 20 products -- mixed: 3 Schneider Multi9 1P MCBs, 1 Acti9
1P MCB, 2 Legrand Cat6 FTP keystones, 6 Yaghout silicone heat/fire
resistant cables, 6 Cat6/Cat6A network bulk cables (Afsharnejad,
Legrand, Kerpen Datacom)."""
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

MULTI9_STD = "EN 60947-2، IEC 60947-2، IEC 60898"
ACTI9_STD = "EN 60898-1، EN 60947-2، IEC 60947-2، IEC 60898-1"
POLE1_APP = "حفاظت از مدارهای تک‌فاز روشنایی و پریز در ساختمان‌های مسکونی و تجاری"
CURVE_DESC = {
    "C": "برای مدارهایی با جریان هجومی راه‌اندازی متوسط مانند موتورها و تجهیزات القایی",
    "B": "برای مدارهای عمومی روشنایی و پریز با جریان راه‌اندازی پایین",
}

HEAT_CABLE_APP = "کوره‌ها، تجهیزات حرارتی، تابلو برق و صنایع سنگین با نیاز به مقاومت حرارتی بالا"
HEAT_CABLE_STD = "IEC 60245-1، IEC 60228، IEC 60754-1/2، IEC 61034-2، IEC 60332-1-2"
SHIELD_STD = "IEC 60245-1، IEC 60228، IEC 60754-1/2، IEC 61034-2، IEC 60332-1-2"
SHIELD_APP = "صنایع فولاد، پتروشیمی، کوره‌ها و تجهیزات حرارتی با نیاز به محافظت در برابر نویز"
FIRE_STD = "BS 7629-1، BS 50200، IEC 60228، IEC 60754-1/2، IEC 61034-2، IEC 60332-1-2"
FIRE_APP = "مدارهای اضطراری، سیستم‌های اعلام حریق، آسانسور و تخلیه دود در ساختمان‌های بلند، بیمارستان‌ها و مراکز کنترل"


def multi9_content(amp, curve):
    curve_desc = CURVE_DESC[curve]
    return f"""<p>کلید مینیاتوری تک پل {amp} آمپر کلاس {curve} اشنایدر از سری Multi9 (خانواده C60N) با تکنولوژی تریپ حرارتی-مغناطیسی، در برابر اضافه‌بار طولانی‌مدت و اتصال کوتاه ناگهانی محافظت می‌کند. ظرفیت قطع آن ۶ کیلوآمپر است و منحنی قطع {curve} این کلید {curve_desc}.</p>
<p>نصب آن روی ریل استاندارد DIN (۳۵ میلی‌متری) ساده است. ابعاد آن ارتفاع ۸۱ میلی‌متر، عرض ۱۸ میلی‌متر و عمق ۷۳ میلی‌متر با وزن ۱۲۰ گرم است و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد (نگهداری تا ۴۰- تا ۷۰+ درجه) کار می‌کند.</p>"""


def acti9_content(amp, curve):
    curve_desc = CURVE_DESC[curve]
    return f"""<p>کلید مینیاتوری تک پل {amp} آمپر کلاس {curve} اشنایدر از سری Acti9 با ولتاژ عایقی ۵۰۰ ولت و ولتاژ ضربه‌ای ۶ کیلوولت، ظرفیت قطع ۶ کیلوآمپر دارد و برای شبکه‌های AC و DC تا ۴۰۰ ولت مناسب است. منحنی قطع {curve} این کلید {curve_desc}.</p>
<p>این کلید با درجه حفاظت IP20، دوام مکانیکی ۲۰۰۰۰ سیکل و دوام الکتریکی ۱۰۰۰۰ سیکل تولید شده و در دمای کاری ۳۵- تا ۷۰+ درجه سانتی‌گراد (و نگهداری تا ۸۵+ درجه) کار می‌کند. ابعاد آن ارتفاع ۸۵ میلی‌متر، عرض ۱۸ میلی‌متر و عمق ۷۸.۵ میلی‌متر با وزن ۲۱۵ گرم است. روی ریل DIN نصب می‌شود و ترمینال‌های آن سیم‌های مفتولی تا ۲۵ میلی‌متر مربع و سیم‌های نرم تا ۱۶ میلی‌متر مربع را می‌پذیرند.</p>"""


RECORDS = [
    {  # 1 - Multi9 1P 10A C
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "",
                   "standard": MULTI9_STD, "application": POLE1_APP},
        "content_html": multi9_content(10, "C"),
    },
    {  # 2 - Multi9 1P 6A C
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "",
                   "standard": MULTI9_STD, "application": POLE1_APP},
        "content_html": multi9_content(6, "C"),
    },
    {  # 3 - Multi9 1P 2A C
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "",
                   "standard": MULTI9_STD, "application": POLE1_APP},
        "content_html": multi9_content(2, "C"),
    },
    {  # 4 - keystone Cat6 FTP 2-module Legrand 076565
        "category_name": "پریز شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "ISO/IEC 11801، ANSI/TIA-568، EN 50173، IEC 60603-7",
                   "application": "پریزهای اطلاعاتی شبکه در پچ‌پنل و باکس‌های دیواری برای اتصال کابل Cat6"},
        "content_html": """<p>کیستون شبکه Cat6 FTP دو ماژول (پهن) لگراند با کد ۰۷۶۵۶۵ از جنس پلی‌کربنات با عرض و طول ۴۵ میلی‌متر ساخته شده و برای انتقال داده تا سرعت ۱ گیگابیت بر ثانیه و پهنای باند ۲۵۰ مگاهرتز مناسب است. کد رنگی دوگانه T568A و T568B اتصال و کابل‌کشی را ساده می‌کند و مکانیزم قفل داخلی نیازی به ابزار خاص برای نصب ندارد.</p>
<p>نصب این کیستون به‌صورت توکار یا روکار (روی ترانک، میز یا دیوار) با جعبه‌ای به عمق حداقل ۴۰ میلی‌متر انجام می‌شود و برای پچ‌پنل‌ها و باکس‌های دیواری شبکه مناسب است.</p>""",
    },
    {  # 5 - keystone Cat6 FTP 1-module Legrand 076562
        "category_name": "پریز شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "ISO/IEC 11801، ANSI/TIA-568، EN 50173، IEC 60603-7",
                   "application": "پریزهای اطلاعاتی شبکه در پچ‌پنل و باکس‌های دیواری برای اتصال کابل Cat6"},
        "content_html": """<p>کیستون شبکه Cat6 FTP یک ماژول (باریک) لگراند با کد ۰۷۶۵۶۲ دارای ساختار فویل‌دار (FTP) است که در برابر تداخل الکترومغناطیسی مقاوم است و برای انتقال داده تا سرعت ۱ گیگابیت بر ثانیه و پهنای باند ۲۵۰ مگاهرتز مناسب است. این کیستون درجه حفاظت IP20 و مقاومت ضربه‌ای IK04 دارد و به اتصال‌دهنده RJ45 مجهز است.</p>
<p>کد رنگی دوگانه T568A و T568B نصب را برای انواع استانداردهای کابل‌کشی ساده می‌کند. نصب آن به‌صورت توکار یا روکار با جعبه‌ای به عمق حدود ۴۰ میلی‌متر و بدون نیاز به ابزار خاص انجام می‌شود.</p>""",
    },
    {  # 6 - Acti9 1P 6A B
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "",
                   "standard": ACTI9_STD, "application": POLE1_APP},
        "content_html": acti9_content(6, "B"),
    },
    {  # 7 - heat-resistant shielded afshan 3x1.5 (SIHCSI)
        "category_name": "کابل شیلددار", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "یاقوت", "size_diameter": "3x1.5", "conductor_material": "مس قلع‌اندود",
                   "standard": SHIELD_STD, "application": SHIELD_APP},
        "content_html": """<p>کابل افشان شیلددار سیلیکونی ۳×۱.۵ یاقوت (SIHCSI) از سه رشته با هادی مس قلع‌اندود افشان (کلاس ۵) ساخته شده که با فویل پلی‌استر آلومینیومی و شیلد بافته‌شده از مس قلع‌اندود محافظت می‌شود. این ساختار دوگانه در برابر نویز و تداخل الکترومغناطیسی (EMI/RFI) مقاوم است. عایق سیلیکونی به ضخامت ۰.۷ میلی‌متر و روکش نهایی به ضخامت ۰.۹ میلی‌متر به رنگ قرمز اخرایی دارد.</p>
<p>با ولتاژ نامی ۳۰۰/۵۰۰ ولت، در بازه دمایی ۶۰- تا ۲۰۰+ درجه سانتی‌گراد کار می‌کند. رشته فاز، نول و ارت با سطح مقطع ۱.۵ میلی‌متر مربع دارد، قطر آن حدود ۸.۱ میلی‌متر و وزن آن حدود ۱۰۰ گرم بر متر است. برای اتصال موتورها و پمپ‌های محیط‌های گرم و مدارهای حساس به نویز مناسب است.</p>""",
    },
    {  # 8 - fire-resistant nim-afshan class2 3x1.5+1.5 (SILTS3)
        "category_name": "کابل ضد حریق", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "یاقوت", "size_diameter": "3x1.5+1.5", "conductor_material": "مس",
                   "standard": FIRE_STD, "application": FIRE_APP},
        "content_html": """<p>کابل ضد حریق نیمه افشان ۳×۱.۵+۱.۵ یاقوت (SILTS3) از سه هادی مسی کلاس ۲ به همراه یک رشته درین وایر (CPC) تشکیل شده است. عایق آن از سیلیکون سرامیکی مقاوم در برابر آتش است که طبق دیتاشیت تا دمای ۸۳۰ درجه سانتی‌گراد به مدت ۱۲۰ دقیقه بدون قطع مدار کار می‌کند. دو لایه شیلد (نوار پلی‌استر و نوار فلزی لمینیت) نویز الکترومغناطیسی را کاهش می‌دهد و روکش نهایی LTS3 کم‌دود و بدون هالوژن است.</p>
<p>قطر این کابل حدود ۹.۲ میلی‌متر و وزن آن حدود ۱۳۰ گرم بر متر است. با ولتاژ نامی ۳۰۰/۵۰۰ ولت، برای تداوم برق‌رسانی به سیستم‌های اعلام و اطفای حریق، روشنایی و تهویه اضطراری در مسیرهای فرار مناسب است.</p>""",
    },
    {  # 9 - fire-resistant nim-afshan class2 2x1.5+1.5 (SILTS3)
        "category_name": "کابل ضد حریق", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "یاقوت", "size_diameter": "2x1.5+1.5", "conductor_material": "مس",
                   "standard": FIRE_STD, "application": FIRE_APP},
        "content_html": """<p>کابل ضد حریق نیمه افشان ۲×۱.۵+۱.۵ یاقوت (SILTS3) از هادی مسی کلاس ۲ مطابق IEC 60228 با ۷ تار به قطر ۰.۵۱۶ میلی‌متر در هر رشته ساخته شده است. عایق سیلیکون سرامیکی آن تا دمای ۸۳۰ درجه سانتی‌گراد به مدت ۱۲۰ دقیقه پایداری خود را حفظ می‌کند و روکش LSFOH آن کم‌دود و بدون هالوژن‌های سمی است.</p>
<p>قطر این کابل حدود ۸.۱ میلی‌متر و وزن آن حدود ۱۰۹ گرم بر متر است. با ولتاژ نامی ۳۰۰/۵۰۰ ولت، برای شبکه‌های فشار ضعیف و تامین برق مسیرهای تخلیه اضطراری مناسب است.</p>""",
    },
    {  # 10 - heat-resistant unshielded afshan 3x1.5 (SIHSI)
        "category_name": "کابل مقاوم در برابر حرارت", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "یاقوت", "size_diameter": "3x1.5", "conductor_material": "مس قلع‌اندود",
                   "standard": HEAT_CABLE_STD, "application": HEAT_CABLE_APP},
        "content_html": """<p>کابل سیلیکونی افشان ۳×۱.۵ یاقوت (SIHSI) از سه هادی مس قلع‌اندود افشان (۳۲ تار به قطر ۰.۲۲۷ میلی‌متر در هر رشته) با رنگ‌بندی آبی، قهوه‌ای و ارت ساخته شده است. عایق سیلیکونی و روکش نهایی سیلیکون رابر آن مقاومت حرارتی بالایی دارد و در دمای ۶۰- تا ۲۰۰+ درجه سانتی‌گراد کار می‌کند.</p>
<p>با ولتاژ نامی ۳۰۰/۵۰۰ ولت، قطر حدود ۸ میلی‌متر و مطابق استانداردهای IEC 60245-1 و IEC 60332-1-2، برای صنایع پتروشیمی، فولاد، خودروسازی و سایر محیط‌های صنعتی با دمای بالا مناسب است.</p>""",
    },
    {  # 11 - heat-resistant shielded afshan 2x1.5 (SIHCSI)
        "category_name": "کابل شیلددار", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "یاقوت", "size_diameter": "2x1.5", "conductor_material": "مس قلع‌اندود",
                   "standard": SHIELD_STD, "application": SHIELD_APP},
        "content_html": """<p>کابل افشان شیلددار سیلیکونی ۲×۱.۵ یاقوت (SIHCSI) از دو رشته هادی مس قلع‌اندود افشان (۳۲ تار به قطر ۰.۲۲۷ میلی‌متر) با فویل پلی‌استر آلومینیومی و شیلد مسی قلع‌اندود محافظت می‌شود که در برابر نویز و تداخل الکترومغناطیسی (EMI/RFI) مقاوم است. عایق سیلیکونی به ضخامت ۰.۷ میلی‌متر و روکش نهایی به ضخامت ۰.۹ میلی‌متر به رنگ قرمز اخرایی دارد.</p>
<p>با ولتاژ نامی ۳۰۰/۵۰۰ ولت، در بازه دمایی ۶۰- تا ۲۰۰+ درجه سانتی‌گراد کار می‌کند. قطر آن حدود ۷.۱۷ میلی‌متر است و برای مدارهای تک‌فاز و کنترل و ابزار دقیق در محیط‌های حرارتی مناسب است.</p>""",
    },
    {  # 12 - fire-resistant maftool class1 3x1.5+1.5 (SILTS3)
        "category_name": "کابل ضد حریق", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "یاقوت", "size_diameter": "3x1.5+1.5", "conductor_material": "مس",
                   "standard": FIRE_STD, "application": FIRE_APP},
        "content_html": """<p>کابل ضد حریق مفتول ۳×۱.۵+۱.۵ یاقوت (SILTS3) از سه هادی مسی مفتولی کلاس ۱ به همراه یک رشته درین وایر ساخته شده است. عایق سیلیکون سرامیکی آن در برابر حرارت و شعله مقاوم است و طبق دیتاشیت تا دمای ۸۳۰ درجه سانتی‌گراد به مدت ۱۲۰ دقیقه بدون قطع مدار کار می‌کند. دو لایه نوار فلزی و پلی‌استری محافظ (شیلد) نویز الکترومغناطیسی را کاهش می‌دهد و روکش LTS3 کم‌دود و بدون هالوژن است.</p>
<p>قطر این کابل حدود ۹.۲ میلی‌متر است و مطابق استاندارد BS 7629-1 تایید آتش‌نشانی دارد. با ولتاژ نامی ۳۰۰/۵۰۰ ولت، برای سیستم‌های برق اضطراری و اعلام حریق در ساختمان‌های تجاری، اداری، بیمارستان‌ها و مراکز صنعتی مناسب است.</p>""",
    },
    {  # 13 - fire-resistant maftool class1 2x1.5+1.5 (SILTS3)
        "category_name": "کابل ضد حریق", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "یاقوت", "size_diameter": "2x1.5+1.5", "conductor_material": "مس",
                   "standard": FIRE_STD, "application": FIRE_APP},
        "content_html": """<p>کابل ضد حریق مفتول ۲×۱.۵+۱.۵ یاقوت (SILTS3) از هادی مسی مفتولی کلاس ۱ به قطر ۱.۳۸ میلی‌متر با عایق سیلیکون سرامیکی به ضخامت ۰.۷ میلی‌متر ساخته شده و می‌تواند در دمای ۶۰- تا ۲۰۰+ درجه سانتی‌گراد کار کند. روکش خارجی آن به ضخامت ۰.۹ میلی‌متر و از نوع LSFOH (کم‌دود، بدون هالوژن) است.</p>
<p>عایق سیلیکونی این کابل سختی ۷۰ Shore A و تحمل کششی تا ۱۵۰ درصد دارد. سیم درین وایر آن نیز از مس قلع‌اندود با سطح مقطع ۱.۵ میلی‌متر مربع است. با ولتاژ نامی ۳۰۰/۵۰۰ ولت، برای تامین برق مطمئن در ساختمان‌های حساس و مهم در زمان بحران مناسب است.</p>""",
    },
    {  # 14 - heat-resistant unshielded afshan 2x1.5 (SIHSI)
        "category_name": "کابل مقاوم در برابر حرارت", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "یاقوت", "size_diameter": "2x1.5", "conductor_material": "مس قلع‌اندود",
                   "standard": HEAT_CABLE_STD, "application": HEAT_CABLE_APP},
        "content_html": """<p>کابل سیلیکونی افشان ۲×۱.۵ یاقوت (SIHSI) از دو رشته هادی مس قلع‌اندود افشان (۳۲ تار به قطر ۰.۲۲۷ میلی‌متر در هر رشته) با رنگ‌بندی آبی و قهوه‌ای ساخته شده است. عایق سیلیکونی به ضخامت ۰.۷ میلی‌متر و روکش نهایی به ضخامت ۰.۹ میلی‌متر مقاومت حرارتی بالایی دارد و در دمای ۶۰- تا ۲۰۰+ درجه سانتی‌گراد کار می‌کند.</p>
<p>با ولتاژ نامی ۳۰۰/۵۰۰ ولت و مطابق استانداردهای IEC 60245-1 و IEC 60332-1-2، این کابل برای اتصال تجهیزات حرارتی صنعتی و محیط‌های داغ مانند کوره‌ها مناسب است.</p>""",
    },
    {  # 15 - Cat6 SFTP Afsharnejad LSZH
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "افشارنژاد", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ISO/IEC 11801، ANSI/TIA-568، EN 50173",
                   "application": "شبکه‌های داخلی حساس به ایمنی حریق مانند بیمارستان‌ها و دیتاسنترها"},
        "content_html": """<p>کابل شبکه Cat6 S/FTP خراسان افشارنژاد با روکش LSZH (کم‌دود، بدون هالوژن) از چهار زوج به‌هم‌تابیده تشکیل شده که هر زوج با فویل آلومینیومی و یک شیلد نهایی محافظت می‌شود و در برابر تداخل الکترومغناطیسی مقاوم است. پهنای باند آن ۲۵۰ مگاهرتز و سرعت انتقال داده آن تا ۱ گیگابیت بر ثانیه است و در تست فلوک هدروم بالای ۵ دسی‌بل در حالت پرمننت لینک دارد.</p>
<p>روکش LSZH آن هنگام آتش‌سوزی دود و گازهای سمی کمی تولید می‌کند، به همین دلیل برای بیمارستان‌ها، دیتاسنترها و ساختمان‌های عمومی مناسب است. در قرقره‌های ۵۰۰ متری عرضه می‌شود و در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 16 - Cat6 SFTP Afsharnejad PVC
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "افشارنژاد", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ISO/IEC 11801، ANSI/TIA-568، EN 50173",
                   "application": "شبکه‌های داخلی ساختمان با نیاز به شیلدینگ در برابر نویز"},
        "content_html": """<p>کابل شبکه Cat6 S/FTP خراسان افشارنژاد با روکش PVC از چهار زوج به‌هم‌تابیده با ساختار شیلد و فویل تشکیل شده که در برابر تداخل الکترومغناطیسی مقاوم است و نسبت به کابل‌های UTP دوام بیشتری دارد. پهنای باند آن ۲۵۰ مگاهرتز و سرعت انتقال داده آن تا ۱ گیگابیت بر ثانیه است و در تست فلوک هدروم بالای ۵ دسی‌بل در حالت پرمننت لینک دارد.</p>
<p>عایق داخلی آن از جنس پلی‌اتیلن و روکش نهایی PVC است که مقاومت خوبی در برابر شرایط محیطی دارد. در قرقره‌های ۵۰۰ متری عرضه می‌شود و در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 17 - Cat6 UTP Legrand LSZH
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568.2-D، EN 50173-1، ISO/IEC 11801، EN 50399، IEC 60332-1-2",
                   "application": "شبکه‌های محلی با نیاز به ایمنی حریق و پشتیبانی PoE++"},
        "content_html": """<p>کابل شبکه Cat6 UTP لگراند با روکش LSZH (کم‌دود، بدون هالوژن) توانایی انتقال داده تا فرکانس ۲۵۰ مگاهرتز را دارد و برای شبکه‌های گیگابیتی و کاربردهای PoE++ مناسب است. قطر متوسط آن ۵.۸ میلی‌متر و وزن آن ۳۷ تا ۴۳ گرم بر متر است و حداقل شعاع خمش مجاز آن ۲۵ میلی‌متر است.</p>
<p>اتصال آن با استانداردهای T568A و T568B انجام می‌شود. مطابق EN 50399 و IEC 60332-1-2 در برابر گسترش شعله مقاوم است و در کارتن‌های ۳۰۵ متری عرضه می‌شود.</p>""",
    },
    {  # 18 - Cat5e UTP Legrand
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801",
                   "application": "شبکه‌های محلی (LAN)، سیستم‌های تلفنی و دوربین‌های مداربسته"},
        "content_html": """<p>کابل شبکه Cat5e UTP لگراند از چهار زوج سیم مسی تابیده بدون شیلد (UTP) با قطر هادی ۰.۵۱ میلی‌متر (AWG 24) تشکیل شده و قطر کلی آن ۴.۹ میلی‌متر است. این کابل توانایی انتقال داده تا فاصله ۱۰۰ متر بدون افت قابل‌توجه کیفیت را دارد و برای شبکه‌های محلی، سیستم‌های تلفنی و دوربین‌های مداربسته مناسب است.</p>
<p>روکش بیرونی آن از جنس PVC است و در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند. سرعت انتقال داده آن تا ۱۰۰ مگابیت بر ثانیه و پهنای باند آن ۱۰۰ مگاهرتز است. در کارتن‌های ۳۰۵ متری عرضه می‌شود.</p>""",
    },
    {  # 19 - Cat6A UFTP Kerpen Datacom
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "کرپن دیتاکام", "size_diameter": "", "conductor_material": "مس",
                   "standard": "EN 50575، EN 50399، IEC 60332-3-24، IEC 60754-1/2، IEC 61034-2",
                   "application": "دیتاسنترها و شبکه‌های سازمانی با نیاز به سرعت بالا و ایمنی حریق"},
        "content_html": """<p>کابل شبکه Cat6A U/FTP کرپن دیتاکام دارای ساختار محافظ U/FTP است که در آن هر یک از چهار زوج سیم با یک فویل آلومینیومی جداگانه پوشانده شده و نویز الکترومغناطیسی را کاهش می‌دهد. هادی آن از مس با قطر ۰.۵۵ میلی‌متر و عایق پلی‌اتیلن ۱.۴۰ میلی‌متری ساخته شده است. قطر خارجی کابل حدود ۶.۵ میلی‌متر و وزن آن ۴۲ گرم بر متر (شامل ۲۳.۵ گرم مس خالص) است.</p>
<p>روکش زرد رنگ آن از نوع LSOH (کم‌دود، بدون هالوژن) است و مطابق EN 50575 و EN 50399 در برابر گسترش شعله مقاوم است. در قرقره‌های ۵۰۰ متری عرضه می‌شود و در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 20 - Cat6A SFTP Kerpen Datacom
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "کرپن دیتاکام", "size_diameter": "", "conductor_material": "مس",
                   "standard": "EN 50575، EN 50399، IEC 60332-3-24، IEC 60754-1/2، IEC 61034-2",
                   "application": "دیتاسنترها و شبکه‌های سازمانی با نیاز به سرعت بالا و ایمنی حریق"},
        "content_html": """<p>کابل شبکه Cat6A S/FTP کرپن دیتاکام (ساخت آلمان) از چهار زوج به‌هم‌تابیده تشکیل شده که هر زوج با نوار آلومینیومی و یک شیلد نهایی دور همه زوج‌ها محافظت می‌شود و تداخل الکترومغناطیسی را کاهش می‌دهد. هادی آن از مس خالص با قطر ۰.۵۵ میلی‌متر ساخته شده، قطر کلی کابل ۶.۷ میلی‌متر و وزن آن ۴۹ گرم بر متر است.</p>
<p>روکش زرد رنگ آن از نوع LSOH (کم‌دود، بدون هالوژن) است و مطابق EN 50575 و EN 50399 در برابر گسترش شعله مقاوم است. برای دیتاسنترها و شبکه‌های سازمانی با نیاز به سرعت بالا مناسب است و در قرقره‌های ۱۰۰۰ متری عرضه می‌شود.</p>""",
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
    with open(os.path.join(DATA_DIR, "batch20_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch20_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch20_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
