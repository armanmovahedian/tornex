# -*- coding: utf-8 -*-
"""Batch 4: next 12 products, hand-rewritten."""
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

NYRY_STD = "IEC 60502-1، ISIRI 3569-1، DIN VDE 0271"
NYRY_APP = "شبکه‌های توزیع برق فشار ضعیف، تاسیسات صنعتی، دفن مستقیم در زمین و نصب در کانال‌های کابل"
FIRE_STD = "BS 7629-1، BS 50200، IEC 60228، IEC 60754-1/2، IEC 61034-2، IEC 60332-1-2"
FIRE_APP = "مدارهای اضطراری، سیستم‌های اعلام حریق، آسانسور و تخلیه دود در ساختمان‌های بلند، بیمارستان‌ها و مراکز کنترل"
MCB_STD = "IEC 60947-2، IEC 60898"
MCB_APP = "حفاظت از مدارهای الکتریکی تک‌فاز در تابلوهای برق، ساختمان‌های مسکونی و تجاری"


def mcb_content(amp):
    return f"""<p>کلید مینیاتوری دو پل {amp} آمپر کلاس B اشنایدر از سری Multi9 (خانواده C60N) برای حفاظت از مدارهای الکتریکی تک‌فاز طراحی شده و هر دو سیم فاز و نول را هم‌زمان پوشش می‌دهد. این کلید با تکنولوژی تریپ حرارتی-مغناطیسی، در برابر اضافه‌بار طولانی‌مدت و اتصال کوتاه ناگهانی محافظت می‌کند و ظرفیت قطع آن ۶ کیلوآمپر است.</p>
<p>منحنی قطع کلاس B این کلید برای مدارهای روشنایی، پریزهای صنعتی پرمصرف و مدارهای کنترلی در منازل بزرگ، آپارتمان‌ها و مراکز تجاری کاربرد دارد. طراحی فشرده و قابلیت نصب آسان روی ریل استاندارد DIN، نصب در تابلوهای برق با فضای محدود را ساده می‌کند.</p>"""


AUTHORED = [
    {  # 1
        "specs": {"brand": "افشارنژاد", "size_diameter": "5x10", "conductor_material": "مس", "standard": NYRY_STD, "application": NYRY_APP},
        "category_name": "کابل زره‌دار", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "content_html": """<p>کابل زره‌دار ۵×۱۰ خراسان افشارنژاد از هادی مس نیمه‌افشان با ۷ تار مفتولی به قطر ۱.۳۳ میلی‌متر و زره فولادی گالوانیزه (SWA) ساخته شده که مقاومت مکانیکی بالایی در برابر فشار و ضربه ایجاد می‌کند. عایق، لایه بستر و روکش نهایی همگی از جنس PVC هستند. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت، برای سیستم‌های توزیع برق فشار ضعیف، زیرساخت‌های شهری و کارخانجات مناسب است و می‌تواند مستقیماً در زمین دفن یا داخل کانال نصب شود.</p>
<p>وزن تقریبی کابل ۱۶۲۵ کیلوگرم بر کیلومتر است و کابل در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. مطابق IEC 60332-1-2 در برابر گسترش شعله مقاوم است و در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد را تحمل می‌کند.</p>""",
    },
    {  # 2
        "specs": {"brand": "افشارنژاد", "size_diameter": "2x16", "conductor_material": "مس", "standard": NYRY_STD, "application": NYRY_APP},
        "category_name": "کابل زره‌دار", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "content_html": """<p>کابل زره‌دار ۲×۱۶ خراسان افشارنژاد از دو رشته هادی مس آنیل‌شده با سطح مقطع ۱۶ میلی‌متر مربع (۷ مفتول به قطر ۱.۶۸ میلی‌متر) و زره مفتول استیل گالوانیزه ساخته شده که امکان دفن مستقیم در خاک بدون نیاز به لوله محافظ را فراهم می‌کند. عایق بین رشته‌ها با نوار پلی‌استر تقویت شده و روکش نهایی از PVC است. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت، برای زیرزمین، کانال‌کشی و محیط‌های صنعتی و نیروگاهی مناسب است.</p>
<p>مقاومت هادی ۱.۱۵ اهم بر کیلومتر در دمای ۲۰ درجه سانتی‌گراد است. وزن تقریبی هر کیلومتر کابل ۱۳۰۰ کیلوگرم است و کابل در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد را تحمل می‌کند و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 3
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x120", "conductor_material": "مس", "standard": "IEC 60502-1، ISIRI 3084، ISIRI 3569-1", "application": NYRY_APP},
        "category_name": "کابل زره‌دار", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "content_html": """<p>کابل زره‌دار ۱×۱۲۰ خراسان افشارنژاد از هادی مس آنیل‌شده با ۳۷ تار مفتولی به قطر تقریبی ۲ میلی‌متر (سطح مقطع ۱۲۰ میلی‌متر مربع) و زره مفتول آلومینیومی ساخته شده که در برابر نیروهای مکانیکی، فشار خاک و جوندگان محافظت می‌کند. عایق و روکش نهایی از جنس PVC هستند. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت، برای شبکه‌های توزیع برق، نیروگاه‌ها و تغذیه ماشین‌آلات سنگین مناسب است و می‌تواند مستقیماً در زمین دفن شود.</p>
<p>مقاومت هادی ۰.۱۵۳ اهم بر کیلومتر در دمای ۲۰ درجه سانتی‌گراد است. کابل تست ولتاژ ۴ کیلوولت را پاس کرده و در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد را تحمل می‌کند.</p>""",
    },
    {  # 4
        "specs": {"brand": "افشارنژاد", "size_diameter": "1x50", "conductor_material": "مس", "standard": NYRY_STD, "application": NYRY_APP},
        "category_name": "کابل زره‌دار", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "content_html": """<p>کابل زره‌دار ۱×۵۰ خراسان افشارنژاد از هادی مس نیمه‌افشان با ۱۹ تار مفتولی به قطر تقریبی ۱.۷۵ میلی‌متر و زره آلومینیومی ساخته شده که در برابر ضربه و فشار مقاوم است. عایق PVC به ضخامت ۱.۴ میلی‌متر و روکش نهایی PVC به ضخامت ۱.۸ میلی‌متر، ایمنی و دوام کابل را تضمین می‌کند. با ولتاژ نامی ۶۰۰/۱۰۰۰ ولت، برای صنایع، نیروگاه‌ها و سیستم‌های توزیع برق با نیاز به دفن زیرزمینی مناسب است.</p>
<p>مقاومت هادی ۰.۳۸۷ اهم بر کیلومتر در دمای ۲۰ درجه سانتی‌گراد است. قطر کلی کابل ۲۰.۵ میلی‌متر و وزن تقریبی آن ۸۶۰ کیلوگرم بر کیلومتر است. کابل در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 5
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "NF C 61-314، IEC 60884-1، NFC 68-104",
                   "application": "نصب روکار پریز برق سه‌فاز در محیط‌های صنعتی، استخر، سونا و آشپزخانه‌های صنعتی با نیاز به مقاومت آب و گردوغبار"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>باکس روکار پریز برق سه‌فاز پلکسو لگراند، یک محفظه استاندارد است که به‌صورت روکار روی سطح نصب می‌شود و از ورودی‌های داکت و کابل پشتیبانی می‌کند. بدنه آن از ترموپلاستیک مقاوم در برابر اشعه ماوراءبنفش، ضربه، رطوبت، گردوغبار و خوردگی ساخته شده و از مواد فاقد هالوژن است که در صورت آتش‌سوزی دود کمتری تولید می‌کند. ابعاد آن ۷۹ میلی‌متر ارتفاع، ۸۶ میلی‌متر عرض و ۴۰ میلی‌متر عمق است.</p>
<p>این باکس با درجه حفاظت IP55 در برابر نفوذ گردوغبار و پاشش آب از هر جهت مقاوم است و برای محیط‌های پرچالش مانند استخر، سونا و آشپزخانه‌های صنعتی مناسب است. دمای کاری مجاز آن ۲۰- تا ۴۰+ درجه سانتی‌گراد است. نصب آن باید توسط افراد متخصص و مطابق استانداردهای نصب الکتریکی انجام شود.</p>""",
    },
    {  # 6
        "specs": {"brand": "یاقوت", "size_diameter": "3x2.5+2.5", "conductor_material": "مس قلع‌اندود", "standard": FIRE_STD, "application": FIRE_APP},
        "category_name": "کابل ضد حریق", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "content_html": """<p>کابل ضد حریق نیمه افشان ۳×۲.۵+۲.۵ یاقوت از هادی مس با خلوص بالا و مقاومت ۷.۴۱ میلی‌اهم بر متر ساخته شده است. عایق سیلیکون نسوز سرامیکی به ضخامت ۰.۸ میلی‌متر با استحکام کششی ۵ مگاپاسکال، در بازه دمایی ۶۰- تا ۲۰۰+ درجه سانتی‌گراد پایدار می‌ماند و طبق آزمون، دمای ۸۳۰ درجه سانتی‌گراد را به مدت ۱۲۰ دقیقه تحمل می‌کند. نوار پلی‌استر با پشت‌بند آلومینیومی و روکش نهایی LTS3 به ضخامت ۱ میلی‌متر، محافظت الکترومغناطیسی و مکانیکی کامل ایجاد می‌کند.</p>
<p>وزن این کابل حدود ۱۹۸ گرم بر متر است. مطابق استانداردهای BS 7629-1، BS 50200 و IEC 60332-1-2 تست شده و ولتاژ نامی آن ۳۰۰/۵۰۰ ولت است.</p>""",
    },
    {  # 7
        "specs": {"brand": "یاقوت", "size_diameter": "2x2.5+2.5", "conductor_material": "مس قلع‌اندود", "standard": FIRE_STD, "application": FIRE_APP},
        "category_name": "کابل ضد حریق", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "content_html": """<p>کابل ضد حریق نیمه افشان ۲×۲.۵+۲.۵ یاقوت از هادی مس با خلوص بالا و عایق سیلیکونی به ضخامت ۰.۸ میلی‌متر ساخته شده که استحکام کششی ۵ مگاپاسکال و کشیدگی ۱۵۰٪ دارد و در بازه دمایی ۶۰- تا ۲۰۰+ درجه سانتی‌گراد پایدار می‌ماند. یک رشته CPC (درین وایر) مسی قلع‌اندود بدون عایق با قطر ۲.۵ میلی‌متر برای تخلیه جریان اضافی تعبیه شده است. طبق آزمون، دمای ۸۳۰ درجه سانتی‌گراد را تا ۱۲۰ دقیقه تحمل می‌کند.</p>
<p>روکش نهایی LTS3 به ضخامت ۰.۸ میلی‌متر و سختی ۵۰ Shore D، دمای کاری ۴۰- تا ۹۰+ درجه سانتی‌گراد را پوشش می‌دهد. دو لایه نوار پلی‌استر و پلی‌استر آلومینیومی، نویز الکترومغناطیسی را کاهش می‌دهد. وزن کابل حدود ۱۶۱ گرم بر متر و ولتاژ نامی آن ۳۰۰/۵۰۰ ولت است.</p>""",
    },
    {  # 8
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "", "standard": MCB_STD, "application": MCB_APP},
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": mcb_content(32),
    },
    {  # 9
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "", "standard": MCB_STD, "application": MCB_APP},
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": mcb_content(25),
    },
    {  # 10
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "", "standard": MCB_STD, "application": MCB_APP},
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": mcb_content(20),
    },
    {  # 11
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "", "standard": MCB_STD, "application": MCB_APP},
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": mcb_content(16),
    },
    {  # 12
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "", "standard": MCB_STD, "application": MCB_APP},
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": mcb_content(10),
    },
]

assert len(AUTHORED) == len(slugs), f"{len(AUTHORED)} authored vs {len(slugs)} slugs"

batch = []
for slug, authored in zip(slugs, AUTHORED):
    pre = pre_by_slug[slug]
    batch.append({
        "slug": pre["slug"],
        "title": pre["title"],
        "excerpt_html": pre["excerpt_html"],
        "content_html": authored["content_html"],
        "extra_specs": pre["extra_specs"],
        "category_name": authored["category_name"],
        "category_parent_name": authored["category_parent_name"],
        "specs": authored["specs"],
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
    with urllib.request.urlopen(req, timeout=180) as resp:
        result = resp.read().decode("utf-8")
    with open(os.path.join(DATA_DIR, "batch4_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch4_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch4_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
