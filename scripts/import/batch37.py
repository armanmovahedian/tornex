# -*- coding: utf-8 -*-
"""Batch 37: 20 products -- 4 Legrand MCB distribution boxes, 2 Legrand
Plexo 3-phase IP44 sockets, a Legrand UPS socket lock, 2 Legrand
under-floor box base plates + 3 floor boxes, and 4 desktop pop-up box
base plates + 4 desktop pop-up boxes."""
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

SWITCH_PARENT = "سایر تجهیزات کابل"


def mcb_box_content(layout_desc):
    return f"""<p>جعبه مینیاتوری لگراند (تابلو برق انتهایی) برای نصب توکار در ورودی ساختمان یا واحدها طراحی شده تا هم از فیوزهای مینیاتوری محافظت کند و هم از نفوذ گردوغبار و مایعات به آن‌ها جلوگیری نماید. {layout_desc}</p>
<p>بدنه و درب آن از پلاستیک با درجه حفاظت IP40 در برابر گردوغبار و IK07 در برابر ضربه ساخته شده و خاصیت خودخاموش‌شوندگی تا دمای ۶۵۰ درجه سانتی‌گراد دارد. ساخت لگراند ترکیه است.</p>"""


def plexo_3phase_socket_content(extra_wire_desc):
    return f"""<p>پریز برق توکار سه‌فاز طوسی ضد آب پلکسو لگراند با استاندارد IP44 در برابر ورود گردوغبار و پاشش آب از هر جهت محافظت می‌کند و برای محیط‌های مرطوب و نیمه‌صنعتی مانند موتورخانه، آزمایشگاه و پالایشگاه مناسب است. {extra_wire_desc}</p>
<p>با ولتاژ نامی ۴۰۰ ولت و جریان نامی ۲۰ آمپر، طراحی ماژولار آن امکان تعویض تنها بخش آسیب‌دیده را بدون نیاز به تعویض کل مجموعه فراهم می‌کند و با نری هم‌شاخه لگراند یک اتصال کامل و ایمن می‌سازد. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def zire_floor_content(modules, code):
    return f"""<p>زیره کف خواب {modules} لگراند ({code}) پیش از نصب باکس کف خواب هم‌ماژول باید روی کف یا زمین نصب شود تا بستری استاندارد و مطمئن برای آن فراهم کند. از یک کادر پلاستیکی توخالی و یک قطعه یونولیت تشکیل شده که در زمان بتن‌ریزی مانع نفوذ بتن به داخل محفظه باکس می‌شود؛ پس از خشک شدن بتن، یونولیت از کادر خارج می‌گردد.</p>
<p>ارتفاع آن از ۷۵ تا ۱۰۵ میلی‌متر قابل تنظیم است تا با ضخامت کف و پوشش نهایی (فرش، پارکت یا سرامیک) تطبیق یابد و عمق مورد نیاز برای نصب آن ۶۵ میلی‌متر است. از جنس PVC سفید ساخته شده و مطابق استاندارد CEI 60670-23 تولید شده است.</p>"""


def floor_box_content(code, module_desc, extra=""):
    return f"""<p>باکس کف خواب لگراند ({code}) با ارتفاع کاهش‌یافته تا ۶۵ میلی‌متر، امکان نصب انواع پریز برق، سوکت شبکه، HDMI، USB و سایر مکانیزم‌های مورد نیاز را در کف زمین فراهم می‌کند. {module_desc} بدنه آن از پلاستیک مقاوم و درب آن از استیل ساخته شده که در برابر عبور افراد و اجسام سنگین آسیب نمی‌بیند.{extra}</p>
<p>درجه حفاظت آن IP30 در برابر اجسام جامد بزرگ‌تر از ۲.۵ میلی‌متر و IK07 در برابر ضربه با انرژی ۲ ژول است. برای نصب این محصول، زیره کف خواب هم‌ماژول لگراند نیز لازم است. مطابق استانداردهای EN 60670-1 و EN 50085-2-2 تولید شده است.</p>"""


def zire_desktop_content(code, material, dims, depth, extra=""):
    return f"""<p>زیره {material} باکس رومیزی لگراند ({code}) به‌طور اختصاصی برای نصب باکس رومیزی هم‌ماژول لگراند طراحی شده و فضایی منظم برای جمع‌آوری و مدیریت کابل‌های زیر میز فراهم می‌کند.{extra} با محل‌های مشخص برای پیچ، امکان اتصال محکم باکس رومیزی به آن وجود دارد و در صورت نیاز، امکان نصب باکس در کف زمین را نیز فراهم می‌کند.</p>
<p>ابعاد آن {dims} میلی‌متر و عمق مورد نیاز برای نصب آن {depth} میلی‌متر است. ساخت شرکت لگراند فرانسه است و مطابق استانداردهای NFC 61-314 و EN 60670-1/23 تولید شده است.</p>"""


def desktop_box_content(code, dims, depth, layout_desc):
    return f"""<p>باکس رومیزی پاپ‌آپ لگراند ({code}) با درب تاشو و دکمه Push and Move، دسترسی سریع به پریزهای برق، شبکه، HDMI و USB روی میز را فراهم می‌کند و در حالت بسته ظاهری یکپارچه با سطح میز ایجاد می‌کند. برای باز کردن درب باید دکمه را فشرد و به سمت خود کشید که از باز شدن ناخواسته درب جلوگیری می‌کند. {layout_desc}</p>
<p>بدنه آن از آلومینیوم با مقاومت ضربه IK07 ساخته شده و رنگ آن نقره‌ای است (رنگ‌های دیگر سفارشی). ابعاد آن {dims} میلی‌متر و عمق مورد نیاز برای نصب آن {depth} میلی‌متر است. برای نصب زمینی این باکس، زیره فلزی هم‌ماژول لگراند لازم است. ساخت شرکت لگراند فرانسه است و مطابق استانداردهای NFC 61-314 و EN 60670-1/23 تولید شده است.</p>"""


RECORDS = [
    {  # 1 - MCB box 36-module
        "category_name": "جعبه فیوز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب توکار در ورودی ساختمان یا واحد برای پروژه‌های با تعداد مدار بالا"},
        "content_html": mcb_box_content("این جعبه فیوز سه‌ردیفه است و در هر ردیف امکان نصب ۱۲ عدد فیوز مینیاتوری وجود دارد؛ در مجموع ظرفیت ۳۶ فیوز مینیاتوری تک‌فاز دارد."),
    },
    {  # 2 - MCB box 24-module
        "category_name": "جعبه فیوز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب توکار در ورودی ساختمان یا واحد"},
        "content_html": mcb_box_content("این جعبه فیوز دو ردیف ۱۲ ماژولی دارد و می‌تواند تا ۲۴ فیوز مینیاتوری تک‌فاز را در خود جای دهد. این محصول پیش‌تر در ایران توسط شرکت صنایع الکتریکی البرز (لگراند) تولید می‌شد که پس از توقف تولید داخلی، اکنون در ترکیه ساخته و وارد می‌شود."),
    },
    {  # 3 - MCB box 12-module
        "category_name": "جعبه فیوز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب توکار در ورودی ساختمان یا واحد"},
        "content_html": mcb_box_content("این جعبه یک‌ردیفه است و امکان نصب ۱۲ عدد فیوز مینیاتوری استاندارد را روی خود فراهم می‌کند. شامل یک قوطی پشتی برای نصب داخل دیوار است که ریل نصب فیوزها درون آن قرار دارد."),
    },
    {  # 4 - MCB box 6-module
        "category_name": "جعبه فیوز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب توکار برای پروژه‌های کوچک با تعداد مدار محدود"},
        "content_html": mcb_box_content("این جعبه یک‌ردیفه است و امکان نصب ۶ عدد فیوز مینیاتوری را روی خود فراهم می‌کند. این خانواده محصول در مدل‌های ۶ تا ۳۶ ماژولی تولید می‌شود؛ مدل‌های ۶، ۸ و ۱۲ ماژول یک‌ردیفه، مدل ۲۴ ماژول دو ردیف ۱۲تایی و مدل ۳۶ ماژول سه ردیف ۱۲تایی است."),
    },
    {  # 5 - Plexo 3-phase 5-pin socket 055708
        "category_name": "پریز صنعتی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، IEC 60884-1", "application": "اتصال برق سه‌فاز کامل با نول و ارت در محیط‌های مرطوب"},
        "content_html": plexo_3phase_socket_content("این پریز قابلیت اتصال سه سیم فاز، یک نول و یک ارت را دارد و برای مدارهای کامل سه‌فاز با نول و ارت مناسب است؛ با نری سه‌فاز پنج شاخ لگراند یک اتصال کامل می‌سازد."),
    },
    {  # 6 - Plexo 3-phase 4-pin socket 055706
        "category_name": "پریز صنعتی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، IEC 60884-1", "application": "اتصال برق سه‌فاز با نول در محیط‌های مرطوب"},
        "content_html": plexo_3phase_socket_content("این پریز قابلیت اتصال سه سیم فاز و یک سیم نول را دارد و با نری سه‌فاز چهار شاخ لگراند کد ۰۵۵۱۵۵ سازگار است."),
    },
    {  # 7 - UPS socket lock 050299
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "جلوگیری از دسترسی غیرمجاز به پریزهای UPS در ادارات، هتل‌ها و مترو"},
        "content_html": """<p>ضامن پریز UPS قرمز لگراند ۰۵۰۲۹۹ به‌طور خاص برای پریز برق آنتی‌باکتریال ارت‌دار قرمز موزائیک لگراند ۰۷۷۲۱۴ طراحی شده است. در حالت عادی، قطعات پلاستیکی داخل دهانه‌های فاز و نول پریز مانع ورود دوشاخه می‌شوند و تنها با استفاده از این ضامن می‌توان این مسیر را باز کرد؛ به این ترتیب فقط افراد مجاز می‌توانند از پریز UPS استفاده کنند.</p>
<p>از پلاستیک مرغوب ساخته شده و دارای چسب دوطرفه زرد رنگ است که نشانه اصالت کالاست؛ ضامن‌های سفیدرنگ موجود در بازار غیراصل هستند. این محصول برای دفاتر اداری، هتل‌ها، فرودگاه‌ها، مترو و مراکز تجاری که نیاز به کنترل دسترسی به پریزهای UPS دارند مناسب است.</p>""",
    },
    {  # 8 - Under-floor box base plate 18-module 089631
        "category_name": "باکس زمینی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60670-23", "application": "بستر نصب باکس کف خواب ۱۸ ماژول قبل از بتن‌ریزی"},
        "content_html": zire_floor_content("۱۸ ماژول", "۰۸۹۶۳۱"),
    },
    {  # 9 - Under-floor box base plate 10/12-module 089630
        "category_name": "باکس زمینی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60670-23", "application": "بستر نصب باکس کف خواب ۱۰ یا ۱۲ ماژول قبل از بتن‌ریزی"},
        "content_html": zire_floor_content("۱۰ و ۱۲ ماژول", "۰۸۹۶۳۰"),
    },
    {  # 10 - Floor box 12-module 089605
        "category_name": "باکس زمینی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 60-670، EN 60670-1، CEI 60670-23، EN 50085-1، EN 50085-2-2", "application": "تامین برق و دیتا از کف در ایستگاه‌های کاری"},
        "content_html": floor_box_content("۰۸۹۶۰۵، ۱۲ ماژول", "این باکس قابلیت نصب ۱۲ مکانیزم باریک (۱ ماژول) یا ۶ مکانیزم پهن (۲ ماژول) را دارد."),
    },
    {  # 11 - Floor box 18-module 089610
        "category_name": "باکس زمینی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 60-670، EN 60670-1، CEI 60670-23، EN 50085-1، EN 50085-2-2", "application": "محیط‌هایی با نیاز به تعداد زیادی پریز و سوکت در کف"},
        "content_html": floor_box_content("۰۸۹۶۱۰، ۱۸ ماژول", "این باکس قابلیت نصب ۱۸ مکانیزم باریک (۱ ماژول) را دارد.", extra=" دستگیره مخفی و دکمه بازکننده درب استفاده از آن را ساده می‌کند، درب در حالت باز نیز ثابت می‌ماند و ارتفاع نصب پریزها برای ایجاد شیب دلخواه قابل تنظیم است."),
    },
    {  # 12 - Floor box 10-module 089620
        "category_name": "باکس زمینی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 60-670، EN 50085-2-2", "application": "فضاهای اداری، سالن کنفرانس و مراکز تجاری با نیاز به مدیریت کابل"},
        "content_html": floor_box_content("۰۸۹۶۲۰، ۱۰ ماژول", "این باکس امکان نصب ماژول‌های موزائیک لگراند را برای پریز برق، شبکه و تلفن فراهم می‌کند و مجهز به محفظه‌های جداکننده کابل است."),
    },
    {  # 13 - Desktop box metal base 8-module 054003
        "category_name": "باکس رومیزی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NFC 61-314، EN 60 670-1، EN 60 670-23", "application": "میزهای کنفرانس بزرگ با نیاز به اتصالات فراوان"},
        "content_html": zire_desktop_content("۰۵۴۰۰۳، ۸ ماژول", "فلزی", "۲۵۵ در ۱۰۰", "۶۱.۲", extra=" در دور تا دور آن محل‌هایی برای اتصال لوله خرطومی برق (قطر ۲۰ و ۲۵ میلی‌متر) و ورودی کابل تعبیه شده و آرایش داخلی آن به‌صورت ۲ در ۴ ماژول است."),
    },
    {  # 14 - Desktop box metal base 6-module 054002
        "category_name": "باکس رومیزی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NFC 61-314، EN 60 670-1، EN 60 670-23", "application": "میزهای کنفرانس و کار گروهی با نیاز به مدیریت کابل"},
        "content_html": zire_desktop_content("۰۵۴۰۰۲، ۶ ماژول", "فلزی", "۲۱۰ در ۱۰۰", "۶۱.۲"),
    },
    {  # 15 - Desktop box metal base 3-module 054000
        "category_name": "باکس رومیزی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NFC 61-314، EN 60 670-1، EN 60 670-23", "application": "میزهای اداری و کنفرانسی کوچک"},
        "content_html": zire_desktop_content("۰۵۴۰۰۰، ۳ ماژول", "فلزی", "۱۰۰ در ۱۰۰", "۶۱.۲", extra=" با دو محل پیچ، اتصال ایمن باکس رومیزی ۳ ماژول را فراهم می‌کند."),
    },
    {  # 16 - Desktop box plastic base 3-module 650390
        "category_name": "باکس رومیزی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NFC 61-314، EN 60 670-1، EN 60 670-23", "application": "میزهای اداری و کنفرانسی کوچک"},
        "content_html": zire_desktop_content("۶۵۰۳۹۰، ۳ ماژول", "پلاستیکی", "۱۰۰ در ۱۰۰", "۵۸"),
    },
    {  # 17 - Desktop pop-up box 8-module 054013
        "category_name": "باکس رومیزی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NFC 61-314، EN 60 670-1، EN 60 670-23", "application": "میزهای کنفرانس بزرگ و سالن‌های جلسات با تعداد کاربر بالا"},
        "content_html": desktop_box_content("۰۵۴۰۱۳، ۸ ماژول", "۱۲۰ در ۲۷۵", "۵۷", "ظرفیت آن ۸ مکانیزم یک‌ماژولی یا ترکیبی از مکانیزم‌های یک و دو ماژول (تا ۴ مکانیزم دو ماژول) است."),
    },
    {  # 18 - Desktop pop-up box 6-module 054012
        "category_name": "باکس رومیزی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NFC 61-314، EN 60 670-1، EN 60 670-23", "application": "میزهای کنفرانس و محیط‌های آموزشی با اتصالات متعدد"},
        "content_html": desktop_box_content("۰۵۴۰۱۲، ۶ ماژول", "۱۲۰ در ۲۳۰", "۶۵", "آرایش داخلی آن به‌صورت ۱+۲+۲+۱ است؛ یعنی دو مکانیزم دو ماژول و دو مکانیزم یک ماژول هم‌زمان قابل نصب هستند."),
    },
    {  # 19 - Desktop pop-up box 4-module 054011
        "category_name": "باکس رومیزی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NFC 61-314، EN 60 670-1، EN 60 670-23", "application": "محیط‌های اداری و تجاری با نیاز متوسط به اتصالات میز"},
        "content_html": desktop_box_content("۰۵۴۰۱۱، ۴ ماژول", "۱۲۰ در ۱۴۲.۵", "۵۷", "ظرفیت آن دو مکانیزم پهن (۲ ماژول) یا چهار مکانیزم باریک (۱ ماژول) از سری موزائیک لگراند است."),
    },
    {  # 20 - Desktop pop-up box 3-module 054010
        "category_name": "باکس رومیزی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NFC 61-314، EN 60 670-1، EN 60 670-23", "application": "میزهای اداری کوچک با نیاز محدود به اتصالات"},
        "content_html": desktop_box_content("۰۵۴۰۱۰، ۳ ماژول", "۱۲۰ در ۱۲۰", "۵۷", "بدنه آن با مواد باکیفیت مانند آلومینیوم مات، برنج برس‌خورده یا استیل ضدزنگ نیز قابل سفارش است."),
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
    with open(os.path.join(DATA_DIR, "batch37_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch37_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch37_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
