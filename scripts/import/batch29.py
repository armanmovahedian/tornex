# -*- coding: utf-8 -*-
"""Batch 29: 20 products -- Legrand Cat5e patch panel, Mosaic motion
sensor, Mosaic dimmer, Mosaic surface box, two 3-phase industrial
plugs, 13 Legrand XS3 single-pole MCBs (curve B 6-63A, curve C
32-63A), and a 2-pair Khorasan Afsharnejad telephone cable."""
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

CURVE_DESC = {
    "B": "برای مدارهای حساس با جریان هجومی پایین مانند روشنایی و تجهیزات الکترونیکی ظریف",
    "C": "برای مدارهای عمومی و مصرف‌کننده‌های صنعتی با جریان هجومی متوسط",
}


def xs3_content(amp, curve):
    return f"""<p>کلید مینیاتوری تک پل {amp} آمپر کلاس {curve} لگراند از سری XS3 با ولتاژ عایقی ۴۰۰ ولت و ولتاژ ضربه‌ای ۴ کیلوولت، ظرفیت قطع ۴.۵ کیلوآمپر دارد. منحنی قطع {curve} این کلید {CURVE_DESC[curve]}.</p>
<p>ابعاد آن ارتفاع ۸۸.۸ میلی‌متر، عرض ۱۷.۸ میلی‌متر و عمق ۷۷.۳ میلی‌متر است و درجه حفاظت IP20 دارد. روی ریل استاندارد DIN نصب می‌شود و امکان اتصال با کابل مسی یا شینه توزیع را دارد. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


RECORDS = [
    {  # 1 - Legrand Cat5e UTP patch panel LCS2 033551
        "category_name": "پچ پنل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "شبکه‌های محلی با حجم انتقال متوسط و بودجه اقتصادی"},
        "content_html": """<p>پچ پنل اصلی Cat5e UTP لگراند از سری LCS2 (مدل ۰۳۳۵۵۱)، ۲۴ پورت RJ45 از نوع بدون شیلد (UTP) دارد و برای شبکه‌هایی که نیازی به محافظت در برابر نویز الکترومغناطیسی ندارند مناسب است. بدنه آن از فولاد گالوانیزه DC01 مقاوم در برابر ضربه و خوردگی و کانکتورهای آن از پلی‌کربنات با کیفیت ساخته شده‌اند که مقاومت تماسی پایین و دوام بالا را تضمین می‌کنند.</p>
<p>سرعت انتقال داده آن ۱۰۰ مگابیت بر ثانیه و پهنای باند آن ۱۰۰ مگاهرتز است. هر کانکتور به‌صورت مجزا روی پنل نصب می‌شود و نیازی به نگهدارنده کابل جداگانه ندارد که نصب را سریع‌تر می‌کند. به همراه ریل و دفترچه راهنما عرضه می‌شود و در بازه دمایی ۴۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 2 - Legrand Mosaic motion sensor 078450
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP40، EN 60669-1، IEC 60695-2-11", "application": "کنترل خودکار روشنایی در راهرو، پارکینگ و فضاهای عمومی پرتردد"},
        "content_html": """<p>سنسور توکار لگراند ۰۷۸۴۵۰ با درجه حفاظت IP40 در برابر گردوغبار و اجسام جامد و مقاومت ضربه IK04 محافظت می‌کند و در جعبه‌های برق با عمق حداقل ۴۰ میلی‌متر نصب می‌شود. با سیستم تشخیص مادون‌قرمز، به‌محض تشخیص حرکت و افت نور طبیعی، مدار روشنایی را به‌صورت خودکار فعال می‌کند. زاویه تشخیص آن ۱۲۰ درجه و برد آن ۸ متر است و مدت‌زمان قطع جریان از ۰ تا ۱۰ دقیقه قابل تنظیم است.</p>
<p>بدنه آن از ABS سفید (RAL 9003) بدون هالوژن و مقاوم در برابر UV ساخته شده است. با ولتاژ ۱۰۰ تا ۲۴۰ ولت و فرکانس ۵۰-۶۰ هرتز کار می‌کند و توان مصرفی آن در حالت استندبای تنها ۰.۰۳۵ وات است. برای فضاهایی مانند سالن کنفرانس، اداره، هتل، مدرسه و پارکینگ که صرفه‌جویی در مصرف انرژی اهمیت دارد مناسب است.</p>""",
    },
    {  # 3 - Telephone cable 2-pair Khorasan Afsharnejad
        "category_name": "کابل تلفن", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2 زوج", "conductor_material": "مس",
                   "standard": "IEC 60189، VDE 0815، TCI", "application": "سیم‌کشی داخلی تلفن ثابت و فکس"},
        "content_html": """<p>کابل تلفن ۲ زوج ۰.۶ خراسان افشارنژاد (ساختار JY(st)Y) از هادی مسی آنیل‌شده مفتولی کلاس ۱ به قطر ۰.۶ میلی‌متر ساخته شده و برای محیط داخلی مناسب است؛ نباید در معرض نور مستقیم آفتاب قرار گیرد. عایق هر رشته از PVC به ضخامت ۰.۲ میلی‌متر است. دور کل رشته‌ها یک نوار پلی‌استر و یک نوار آلومینیومی به ضخامت ۰.۰۳۶ میلی‌متر همراه با یک سیم تخلیه (Drain Wire) قلع‌اندود به قطر ۰.۴ میلی‌متر قرار دارد که نویز و تداخل الکترومغناطیسی را دفع می‌کند. حداکثر ظرفیت خازنی متقابل آن ۱۰۰ نانوفاراد بر کیلومتر است.</p>
<p>روکش نهایی PVC خاکستری کابل را در برابر ضربه‌های مکانیکی و خوردگی محافظت می‌کند. قطر کلی کابل حدود ۵.۱ میلی‌متر و وزن آن حدود ۳.۱ کیلوگرم بر کلاف ۱۰۰ متری است. با حداکثر ولتاژ کاری ۳۰۰ ولت DC و تست ولتاژ ۲ کیلوولت، مطابق استانداردهای IEC 60189 و VDE 0815 تولید شده و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 4 - Legrand Mosaic dimmer 078405
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK02، IP20، EN 60669-1، IEC 60695-2-11", "application": "کنترل شدت نور در دفاتر اداری، مراکز آموزشی و منازل"},
        "content_html": """<p>کلید دیمر موزائیک لگراند ۰۷۸۴۰۵ با طراحی ماژولار، قابلیت نصب توکار و روکار را دارد و با آداپتور مخصوص روی دیوارهای نازک نیز قابل نصب است. با دکمه فشاری، فشردن کوتاه چراغ را روشن/خاموش می‌کند و فشردن طولانی شدت نور را تنظیم می‌کند. توان خروجی آن ۶۰۰ وات است و انواع لامپ‌های قابل دیم (رشته‌ای، هالوژن ۲۳۰ ولت و برخی ترانسفورماتورهای مغناطیسی) را کنترل می‌کند؛ برای هالوژن‌های مجهز به ترانس الکترونیکی مناسب نیست.</p>
<p>درجه حفاظت آن IP20 و مقاومت ضربه آن IK02 است. بدنه از پلی‌کربنات و کلیدها از ABS سفید (RAL 9003) با خاصیت خودخاموش‌شوندگی ساخته شده‌اند. برای محیط‌های عمومی مانند ایستگاه مترو، سالن کنفرانس و آمفی‌تئاتر مناسب است و در بازه دمایی ۰ تا ۳۵+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 5 - Legrand Mosaic surface box 2-module 080281
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP20، IEC 60695-2-11", "application": "نصب روکار مکانیزم‌های موزائیک لگراند در فضاهای داخلی"},
        "content_html": """<p>قوطی روکار دو ماژول موزائیک لگراند ۰۸۰۲۸۱ از ABS سفید (RAL 9003) مقاوم در برابر UV ساخته شده و مطابق استاندارد IK04 در برابر ضربه‌های تا ۰.۵ ژول مقاوم است. برای نصب کلید و پریزهای سری موزائیک به‌صورت روکار مناسب است و همراه با کادر و مکانیزم مربوطه یک راهکار کامل نصب روکار ایجاد می‌کند. ورودی‌های پیش‌برش‌داده‌شده در بالا و پایین قوطی، عبور کابل را بدون برش اضافه ممکن می‌سازند.</p>
<p>درجه حفاظت IP20 آن از ورود اجسام جامد بزرگ‌تر از ۱۲.۵ میلی‌متر جلوگیری می‌کند. به همراه دو پیچ برای نصب ساپورت چنگکی لگراند عرضه می‌شود که امکان تبدیل سریع مکانیزم توکار به روکار را فراهم می‌کند. در بازه دمایی ۵- تا ۳۵+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 6 - Legrand 3-phase 4-pin male plug 055155
        "category_name": "پریز صنعتی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NF C 61-314، IEC 60884-1", "application": "اتصال برق سه‌فاز در تاسیسات صنعتی، موتورخانه و تابلو برق"},
        "content_html": """<p>نری سه‌فاز چهار شاخ سفید لگراند ۰۵۵۱۵۵ با درجه حفاظت IP20 در برابر ورود اجسام جامد بزرگ‌تر از ۱۲.۵ میلی‌متر محافظت می‌کند. با قابلیت اتصال سه فاز به همراه یک نول، برای سیستم‌های نیازمند انتقال برق سه‌فاز طراحی شده و با مادگی سه‌فاز چهار شاخ لگراند (کد ۰۵۵۷۰۶) سازگار است.</p>
<p>با ولتاژ نامی ۴۰۰ ولت و جریان نامی ۲۰ آمپر، در تاسیسات صنعتی، موتورخانه‌ها، پالایشگاه‌ها، نیروگاه‌ها و سیستم‌های CNC کاربرد دارد. طراحی ماژولار آن نصب سریع و آسان را فراهم می‌کند و در بازه دمایی ۲۵- تا ۴۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 7 - Legrand 3-phase 5-pin male plug 055157
        "category_name": "پریز صنعتی", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NF C 61-314، IEC 60884-1", "application": "اتصال برق سه‌فاز به همراه نول و ارت در محیط‌های صنعتی"},
        "content_html": """<p>نری سه‌فاز پنج شاخ سفید لگراند ۰۵۵۱۵۷ دارای سه اتصال برای برق سه‌فاز، یک سیم نول و یک ارت است و انتقال برق سه‌فاز کامل (با نول و ارت) را فراهم می‌کند. با ولتاژ نامی ۴۰۰ ولت و جریان نامی ۲۰ آمپر، برای کابل‌های پنج‌رشته‌ای مناسب است و با مادگی سه‌فاز لگراند (کد ۰۵۵۷۰۸) یک سیستم برق کامل و پایدار می‌سازد.</p>
<p>درجه حفاظت آن IP20 است و برای محیط‌های داخلی و صنعتی مانند کارخانه‌ها، استخرها، موتورخانه‌ها و آزمایشگاه‌های صنعتی مناسب است. طراحی ماژولار آن نصب و تعویض سریع را ممکن می‌کند و در بازه دمایی ۲۵- تا ۴۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 8 - XS3 1P 6A B 403202
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از مدارهای حساس روشنایی و تجهیزات الکترونیکی"},
        "content_html": xs3_content(6, "B"),
    },
    {  # 9 - XS3 1P 10A B 403203
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از مدارهای روشنایی"},
        "content_html": xs3_content(10, "B"),
    },
    {  # 10 - XS3 1P 16A B 403204
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از پریزهای برق خانگی و اداری"},
        "content_html": xs3_content(16, "B"),
    },
    {  # 11 - XS3 1P 20A B 403205
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از ورودی برق آپارتمان‌ها و مصرف‌کننده‌های حساس به اضافه‌بار"},
        "content_html": xs3_content(20, "B"),
    },
    {  # 12 - XS3 1P 25A B 403206
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از مدار کولر گازی و مصرف‌کننده‌های مشابه"},
        "content_html": xs3_content(25, "B"),
    },
    {  # 13 - XS3 1P 32A B 403207
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از ورودی برق آپارتمان‌ها و مصرف‌کننده‌های صنعتی"},
        "content_html": xs3_content(32, "B"),
    },
    {  # 14 - XS3 1P 40A B 403208
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از مدارهای الکتریکی حساس خانگی و صنعتی"},
        "content_html": xs3_content(40, "B"),
    },
    {  # 15 - XS3 1P 50A B 403209
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از ورودی برق آپارتمان‌ها و مصرف‌کننده‌های صنعتی"},
        "content_html": xs3_content(50, "B"),
    },
    {  # 16 - XS3 1P 63A B 403210
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از ورودی برق آپارتمان‌ها و مصرف‌کننده‌های صنعتی"},
        "content_html": xs3_content(63, "B"),
    },
    {  # 17 - XS3 1P 63A C 403335
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از ورودی برق آپارتمان‌ها و مصرف‌کننده‌های صنعتی"},
        "content_html": xs3_content(63, "C"),
    },
    {  # 18 - XS3 1P 50A C 403334
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از ورودی برق آپارتمان‌ها و مصرف‌کننده‌های صنعتی"},
        "content_html": xs3_content(50, "C"),
    },
    {  # 19 - XS3 1P 40A C 403333
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از ورودی برق آپارتمان‌ها و مصرف‌کننده‌های صنعتی"},
        "content_html": xs3_content(40, "C"),
    },
    {  # 20 - XS3 1P 32A C 403332
        "category_name": "فیوز مینیاتوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60898-1، IEC 60947-2", "application": "حفاظت از مدارهای عمومی با جریان هجومی متوسط"},
        "content_html": xs3_content(32, "C"),
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
    with open(os.path.join(DATA_DIR, "batch29_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch29_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch29_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
