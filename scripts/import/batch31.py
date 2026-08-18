# -*- coding: utf-8 -*-
"""Batch 31: 20 products -- 2 Legrand XC3 RCCB (residual current)
breakers, 4 EEC emergency lighting fixtures, a Khorasan Afsharnejad
coaxial antenna cable, and 13 Khorasan Afsharnejad NYAF flexible
colored wires (1.5mm2 up to 240mm2)."""
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


def rccb_content(amp):
    return f"""<p>کلید محافظ جان دو پل {amp} آمپر لگراند از سری XC3 با حساسیت نشتی جریان ۳۰ میلی‌آمپر، کوچک‌ترین نشتی جریان (اتصال بدنه) را تشخیص داده و مدار را قطع می‌کند. این کلید یک فیوز نیست و تنها در برابر نشتی جریان واکنش نشان می‌دهد؛ برای حفاظت کامل مدار در برابر اتصال کوتاه و اضافه‌بار باید در کنار یک کلید مینیاتوری (MCB) هم‌جریان به کار رود.</p>
<p>ظرفیت قطع آن ۶ کیلوآمپر و ولتاژ نامی آن ۲۲۰ تا ۲۵۰ ولت است. روی ریل استاندارد DIN نصب می‌شود، درجه حفاظت آن IP20 است و برای سیم‌های مسی مفتولی و افشان مناسب است. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند و به‌ویژه در آشپزخانه، حمام، استخر و محیط‌های صنعتی مرطوب کاربرد دارد.</p>"""


def nyaf_content(size, tar_count, tar_dia, resistance, insulation, dia, weight):
    return f"""<p>سیم برق افشان رنگی {size} خراسان افشارنژاد (NYAF) از هادی مسی آنیل‌شده افشان کلاس ۵ ({tar_count} تار به قطر {tar_dia} میلی‌متر) با عایق PVC به ضخامت {insulation} میلی‌متر ساخته شده و در رنگ‌های قرمز، آبی، مشکی، قهوه‌ای، زرد، سبز، ارت یا رنگ سفارشی مشتری تولید می‌شود. مقاومت هادی آن در دمای ۲۰ درجه سانتی‌گراد {resistance} است و مطابق IEC 60332-1-2 در برابر گسترش آتش مقاوم است.</p>
<p>قطر کلی این سیم حدود {dia} میلی‌متر و وزن آن حدود {weight} است. با ولتاژ نامی ۴۵۰/۷۵۰ ولت و تست ولتاژ ۲.۵ کیلوولت، عایق آن در اتصال کوتاه لحظه‌ای تا ۱۶۰ درجه سانتی‌گراد دوام می‌آورد و در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


RECORDS = [
    {  # 1 - Legrand RCCB 2P 40A 403183
        "category_name": "محافظ جان", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 61008-1", "application": "حفاظت جانی در برابر نشتی جریان در آشپزخانه، حمام و مدارهای پرمصرف"},
        "content_html": rccb_content(40),
    },
    {  # 2 - Legrand RCCB 2P 25A 403182
        "category_name": "محافظ جان", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 61008-1", "application": "حفاظت جانی در برابر نشتی جریان در آپارتمان‌ها و پریزهای خانگی"},
        "content_html": rccb_content(25),
    },
    {  # 3 - EEC Elegance exit light
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "ای ای سی", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 60598-2-22، تاییدیه TUV",
                   "application": "روشنایی و نشانگر خروج اضطراری در ساختمان‌های عمومی و تجاری"},
        "content_html": """<p>چراغ خروج اضطراری EEC مدل Elegance (ساخت ترکیه) با باتری نیکل کادمیوم داخلی، هم به‌صورت روکار و هم با افزودن براکت مخصوص به‌صورت توکار قابل نصب است. مدت‌زمان پشتیبانی باتری بین ۱ تا ۳ ساعت قابل تنظیم است و می‌توان آن را در حالت Maintained (روشن دائم) یا Non-Maintained (فقط هنگام قطع برق) تنظیم کرد.</p>
<p>منبع نور آن از نوع Power LED با توان مصرفی ۸ وات است که طبق اعلام سازنده تا ۲۵ سال طول عمر دارد. درجه حفاظت آن IP65 و کلاس عایقی آن ۲ است. مطابق استاندارد EN 60598-2-22 تولید شده و دارای تاییدیه کیفی TUV است و با ولتاژ ۲۲۰ تا ۲۵۰ ولت کار می‌کند.</p>""",
    },
    {  # 4 - EEC Elegance Double exit light
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "ای ای سی", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 60598-2-22، تاییدیه TUV",
                   "application": "روشنایی و نشانگر خروج اضطراری در فضاهای داخلی و پارکینگ"},
        "content_html": """<p>چراغ خروج اضطراری EEC مدل Elegance Double (ساخت ترکیه) با باتری نیکل کادمیوم و مدت‌زمان پشتیبانی قابل تنظیم ۱ یا ۳ ساعت، به‌صورت روکار برای فضاهای داخلی و پارکینگ طراحی شده است. بدنه آن از پلی‌کربنات مقاوم در برابر شرایط آب‌وهوایی ساخته شده و منبع نور آن LED با توان مصرفی ۶ وات است.</p>
<p>این چراغ قابلیت تغییر بین حالت Maintained (روشن دائم پس از اتصال به برق همراه با شارژ باتری) و Non-Maintained (خاموش تا زمان قطع برق، سپس روشن خودکار) را دارد. درجه حفاظت آن IP65، کلاس عایقی آن ۲ است و مطابق استاندارد EN 60598-2-22 با تاییدیه TUV تولید شده و با ولتاژ ۲۲۰ تا ۲۵۰ ولت کار می‌کند.</p>""",
    },
    {  # 5 - EEC UTLANK-M310 exit light
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "ای ای سی", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 60598-2-22، تاییدیه TUV، گواهی CE",
                   "application": "نشانگر مسیر خروج قابل نصب در سقف کاذب کناف"},
        "content_html": """<p>چراغ خروج اضطراری EEC مدل UTLANK-M310 (ساخت ترکیه) از خانواده UTL این شرکت است که در سه حالت آویز با زنجیر، توکار و روکار قابل نصب است. نگهدارنده بالایی طراحی‌شده این مدل امکان نصب توکار در انواع سقف کاذب کناف را فراهم می‌کند؛ در مقابل مدل UTLZNC همین خانواده با زنجیر مخصوص به‌صورت آویز نصب می‌شود.</p>
<p>با باتری نیکل کادمیوم و توان مصرفی ۴ وات، پس از شارژ کامل تا ۳ ساعت روشنایی LED را تامین می‌کند. این محصول دارای گواهی CE اروپا، تاییدیه TUV هلند و مطابق استاندارد EN 60598-2-22 است و با ولتاژ ۲۲۰ تا ۲۵۰ ولت کار می‌کند.</p>""",
    },
    {  # 6 - EEC UTLBRK-M310 exit light
        "category_name": "روشنایی اضطراری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "ای ای سی", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 60598-2-22، تاییدیه TUV",
                   "application": "نشانگر مسیر خروج با ساین قابل تعویض، دو طرفه"},
        "content_html": """<p>چراغ خروج اضطراری EEC مدل UTLBRK-M310 (ساخت ترکیه) با ساین (تابلوی علائم) قابل تعویض عرضه می‌شود و می‌تواند به‌جای علامت «خروج»، سایر علائم را نیز به‌صورت درخشان و دوطرفه با LED نمایش دهد. بدنه آن از آلومینیوم ساخته شده که مقاومت بالایی در برابر ضربه و عوامل محیطی به آن می‌دهد و موفق به کسب گواهینامه IP30 شده است.</p>
<p>باتری آن از نوع نیکل کادمیوم است که پس از شارژ کامل تا ۳ ساعت به‌صورت پیوسته روشنایی LED را تامین می‌کند. توان مصرفی آن ۶ وات و ولتاژ کاری آن ۲۲۰ تا ۲۵۰ ولت است و در سه حالت آویز با زنجیر، توکار و روکار قابل نصب است.</p>""",
    },
    {  # 7 - Coaxial antenna cable
        "category_name": "کابل آنتن", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1.0", "conductor_material": "مس",
                   "standard": "JIS C 3501", "application": "سیستم‌های آنتن تلویزیون و ماهواره خانگی"},
        "content_html": """<p>کابل آنتن کواکسیال صادراتی خراسان افشارنژاد از نوع 4.5C-2V و امپدانس ۷۵ اهم (تلورانس ±۳ اهم) است که هادی مرکزی ضخیم‌تر آن نسبت به کابل‌های نازک‌تر مانند 3C-2V، افت سیگنال کمتری در مسافت‌های طولانی دارد. هادی مرکزی آن از مس آنیل‌شده مفتولی کلاس ۱ و عایق آن از فوم پلی‌اتیلن است که علاوه بر استحکام مکانیکی، تلفات سیگنال را کاهش می‌دهد و از تداخل الکتریکی جلوگیری می‌کند.</p>
<p>مقاومت هادی آن ۲۴ اهم بر کیلومتر در دمای ۲۰ درجه سانتی‌گراد و بازه فرکانسی کاری آن از ۵ هرتز تا ۱ گیگاهرتز است. مقاومت عایقی آن بیش از ۱۰۰۰۰ مگااهم بر کیلومتر و تست ولتاژ آن ۱ کیلوولت است. قطر کلی کابل حدود ۶.۲۴ میلی‌متر و وزن آن حدود ۴۵ گرم بر متر است؛ در کلاف و قرقره ۱۰۰ و ۵۰۰ متری عرضه می‌شود و در بازه دمایی ۴۰- تا ۸۵+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 8 - NYAF 1.5mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "1.5", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0271، IEC 60228", "application": "سیم‌کشی مدارهای روشنایی و اتصالات داخلی ساختمان‌های مسکونی و اداری"},
        "content_html": nyaf_content("۱.۵", "مطابق دیتاشیت", "مطابق دیتاشیت", "۱۳.۳۰ اهم بر کیلومتر", "0.7", "2.92", "مطابق دیتاشیت"),
    },
    {  # 9 - NYAF 2.5mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "2.5", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "سیم‌کشی لوله‌های خرطومی، تابلوهای فرمان و پریز برق"},
        "content_html": nyaf_content("۲.۵", "50", "0.24", "۷.۹۸ اهم بر کیلومتر", "مطابق دیتاشیت", "مطابق دیتاشیت", "مطابق دیتاشیت"),
    },
    {  # 10 - NYAF 4mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "4", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "مدارهای فشار ضعیف، تجهیزات صنعتی و مدارهای روشنایی با بار زیاد"},
        "content_html": nyaf_content("۴", "56", "0.29", "۴.۹۵ اهم بر کیلومتر", "0.8", "4.15", "4.5 کیلوگرم بر کلاف ۱۰۰ متری"),
    },
    {  # 11 - NYAF 6mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "6", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "سیم‌کشی ورودی ساختمان‌های کوچک، تغذیه تجهیزات صنعتی و کولر گازی بزرگ"},
        "content_html": nyaf_content("۶", "مطابق دیتاشیت", "مطابق دیتاشیت", "۳.۳۰ اهم بر کیلومتر", "مطابق دیتاشیت", "4.71", "6.28 کیلوگرم بر کلاف ۱۰۰ متری"),
    },
    {  # 12 - NYAF 10mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "10", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "سیم‌کشی اصلی ساختمان‌ها و اتصال پمپ‌های آب"},
        "content_html": nyaf_content("۱۰", "80", "0.39", "۱.۹۱ اهم بر کیلومتر", "1", "6.1", "11.3 کیلوگرم بر کلاف ۱۰۰ متری"),
    },
    {  # 13 - NYAF 16mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "16", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "اتصال تجهیزات قدرت صنعتی"},
        "content_html": nyaf_content("۱۶", "126", "0.39", "۱.۲۱ اهم بر کیلومتر", "1", "7.3", "16.8 کیلوگرم بر کلاف ۱۰۰ متری"),
    },
    {  # 14 - NYAF 25mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "25", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "سیم‌کشی مدارهای پرجریان و تغذیه ماشین‌آلات و الکتروموتورهای صنعتی"},
        "content_html": nyaf_content("۲۵", "مطابق دیتاشیت", "مطابق دیتاشیت", "۰.۷۸ اهم بر کیلومتر", "مطابق دیتاشیت", "9.2", "25.4 کیلوگرم بر کلاف"),
    },
    {  # 15 - NYAF 35mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "35", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "اتصال اینورترها در سیستم‌های انرژی تجدیدپذیر و مدارهای پرجریان"},
        "content_html": nyaf_content("۳۵", "مطابق دیتاشیت", "مطابق دیتاشیت", "۰.۵۵۴ اهم بر کیلومتر", "مطابق دیتاشیت", "10.4", "350 گرم بر متر"),
    },
    {  # 16 - NYAF 240mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "240", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "تغذیه تابلوهای توزیع اصلی برق ساختمان‌ها و تجهیزات صنعتی"},
        "content_html": nyaf_content("۲۴۰", "1170", "مطابق دیتاشیت", "۰.۰۸۰۱ اهم بر کیلومتر", "2.2", "25.4", "2.3 کیلوگرم بر متر"),
    },
    {  # 17 - NYAF 185mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "185", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "تامین انرژی ماشین‌آلات جوشکاری سیار و تابلوهای صنعتی پرجریان"},
        "content_html": nyaf_content("۱۸۵", "875", "مطابق دیتاشیت", "۰.۱۰۶ اهم بر کیلومتر", "2", "22.5", "1.8 کیلوگرم بر متر"),
    },
    {  # 18 - NYAF 150mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "150", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "سیستم‌های انتقال قدرت و ماشین‌آلات صنعتی متحرک"},
        "content_html": nyaf_content("۱۵۰", "722", "0.49", "۰.۱۲۹ اهم بر کیلومتر", "1.8", "20.1", "1.4 کیلوگرم بر متر"),
    },
    {  # 19 - NYAF 120mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "120", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "سیستم‌های برق‌رسانی ساختمان‌های بزرگ و کارخانجات صنعتی"},
        "content_html": nyaf_content("۱۲۰", "570", "0.49", "۰.۱۶۱ اهم بر کیلومتر", "1.6", "17.9", "1.1 کیلوگرم بر متر"),
    },
    {  # 20 - NYAF 95mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "95", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "مدارهای الکتریکی استاندارد با نیاز به جریان بالا"},
        "content_html": nyaf_content("۹۵", "456", "0.49", "۰.۲۰۶ اهم بر کیلومتر", "1.6", "16.7", "913 گرم بر متر"),
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
    with open(os.path.join(DATA_DIR, "batch31_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch31_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch31_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
