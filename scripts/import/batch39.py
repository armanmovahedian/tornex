# -*- coding: utf-8 -*-
"""Batch 39: 20 products -- 2 Legrand telephone keystones, 8 Legrand
network keystones (Cat6A SFTP, Cat6 SFTP, Cat6 UTP, Cat5e UTP), 3
Khorasan Afsharnejad flexible wires (50, 0.75, 0.5 mm2), 1 Legrand
Cat6 SFTP LSZH network cable reel, and 6 Legrand trunking accessories
(1 under-door partition + 5 module frames)."""
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


def phone_socket_content(width_label, code, dims):
    return f"""<p>پریز تلفن {width_label} لگراند (کد {code}) برای کاربردهای تلفنی معمول در منازل، دفاتر کار و فضاهای تجاری طراحی شده و از فناوری RJ11 چهارپین برای برقراری ارتباطات صوتی استفاده می‌کند که با اکثر خطوط تلفن استاندارد سازگاری دارد و با انواع قاب و فریم‌های لگراند هماهنگ است.</p>
<p>بدنه آن از پلی‌کربنات ساخته شده و سیستم اتصال سریع (بدون نیاز به ابزار) دارد که نصب یا تعویض آن را ساده می‌کند. ابعاد آن {dims} میلی‌متر است و در بازه دمایی ۵- تا ۳۵+ درجه سانتی‌گراد کار می‌کند. مطابق دسته‌بندی Cat3 است و در برابر گردوغبار محافظت‌شده است.</p>"""


def network_socket_content(width_label, category, structure_fa, code, speed, bandwidth, extra=""):
    return f"""<p>پریز شبکه {category} {structure_fa} {width_label} لگراند (کد {code}) از نوع RJ45 است و با سرعت انتقال داده {speed} و پهنای باند {bandwidth} برای شبکه‌های داخلی و اداری مناسب است. بدنه آن از پلی‌کربنات مقاوم در برابر حرارت و اشعه UV ساخته شده و با استانداردهای رنگی T568A و T568B سازگار است.{extra}</p>
<p>این پریز از قابلیت PoE تا ۹۰ وات (مطابق IEEE 802.3af/at/bt) پشتیبانی می‌کند و مطابق استانداردهای ISO/IEC 11801، ANSI/TIA 568، EN 50173 و IEC 60603-7 تولید شده است. درجه حفاظت آن IP20 در برابر گردوغبار و IK04 در برابر ضربه است و در بازه دمایی ۱۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند. نصب آن بدون نیاز به ابزار خاص و در جعبه‌ای با عمق حداقل ۴۰ میلی‌متر انجام می‌شود.</p>"""


def cat5e_socket_content(width_label, code, extra=""):
    return f"""<p>پریز شبکه Cat5e UTP {width_label} لگراند (کد {code}) برای استفاده در شبکه‌های ساختاریافته با استاندارد Cat5e طراحی شده و امکان اتصال کابل به دو روش رنگ‌بندی استاندارد T568A و T568B را با کمک برچسب‌های راهنمای رنگی روی بدنه فراهم می‌کند. این کیستون دارای دربی شیشه‌ای در قسمت بالایی برای قرار دادن لیبل شماره یا نام است.{extra}</p>
<p>برای شبکه‌هایی با نیاز به سرعت و پهنای باند بالاتر، پریز شبکه Cat6 UTP لگراند از همین خانواده محصول در دسترس است.</p>"""


def afshan_wire_content(size, conductor_desc, od, resistance, voltage, test_voltage, application, standard_extra=""):
    return f"""<p>سیم برق افشان {size} خراسان افشارنژاد با هادی مسی افشان (کلاس ۵) {conductor_desc} قطر کلی آن {od} میلی‌متر است. عایق آن از جنس PVC است که با فرآیند اکستروژن روی هادی مسی اعمال می‌شود و مطابق استانداردهای IEC 60227، ISIRI 607، IEC 60228{standard_extra} تولید می‌شود. در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و خاصیت عدم انتشار شعله دارد.</p>
<p>با ولتاژ نامی {voltage} و تست ولتاژ {test_voltage}، مقاومت هادی آن {resistance} در دمای ۲۰ درجه سانتی‌گراد است و دمای اتصال کوتاه آن ۱۶۰+ درجه سانتی‌گراد است. این سیم برای {application} کاربرد دارد و به دلیل انعطاف‌پذیری بالای هادی افشان، در مسیرهای پیچیده و پرخم نیز به‌راحتی قابل نصب است.</p>"""


def network_cable_lszh_content(code, category, structure_fa, speed, bandwidth):
    return f"""<p>کابل شبکه {category} {structure_fa} لگراند با روکش LSZH (کد {code}) برای انتقال داده در شبکه‌های محلی با سرعت بالا طراحی شده و از استاندارد PoE++ (IEEE 802.3bt) برای تأمین همزمان برق و داده پشتیبانی می‌کند که برای دوربین‌های امنیتی و تلفن‌های VoIP کاربرد دارد. استاندارد هادی آن AWG 23 است.</p>
<p>روکش LSZH آن در هنگام آتش‌سوزی دود کم و بدون هالوژن تولید می‌کند و مطابق درجه‌بندی حریق EUROCLASS Dca s2 d2 a1 و استانداردهای EN 50399 و IEC 60332-1-2 ساخته شده است. با سرعت انتقال داده {speed} و پهنای باند {bandwidth}، به‌صورت قرقره ۵۰۰ متری آبی‌رنگ عرضه می‌شود و در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def trunking_partition_content():
    return """<p>پارتیشن زیر درب ترانکینگ لگراند (کد ۰۱۰۵۸۲) در بسته‌های ۲۴ متری شامل ۱۲ شاخه ۲ متری عرضه می‌شود و از جنس PVC بدون سرب ساخته شده است. این پارتیشن با نصب زیر درب ترانکینگ‌های DLP لگراند (مانند مدل‌های ۵۰ در ۱۰۵ و ۵۰ در ۱۵۰ میلی‌متر)، دو مسیر مجزا در داخل ترانک ایجاد می‌کند و امکان عبور منظم و ایمن کابل‌های برق و شبکه را از هم جدا نگه می‌دارد.</p>
<p>نصب آن ساده و بدون نیاز به ابزار خاص است و رنگ آن سفید است تا با بدنه ترانکینگ هماهنگی داشته باشد.</p>"""


def kadre_content(code, door_width, trunking_examples, mechanism_desc):
    return f"""<p>کادر {mechanism_desc.split(' یا')[0]} درب {door_width} ترانک لگراند (کد {code}) به‌طور اختصاصی برای نصب روی ترانکینگ‌های لگراند با درب {door_width} میلی‌متر طراحی شده که شامل مدل‌های {trunking_examples} می‌شود. این محصول از دو بخش ساپورت و کادر تشکیل شده و امکان نصب {mechanism_desc} را روی ترانک یا مستقیم روی دیوار فراهم می‌کند.</p>
<p>بدنه آن از PVC سفید ساخته شده و ساخت کشور فرانسه است. این کادر به کاربر امکان می‌دهد طیف وسیعی از پریزها و مکانیزم‌های استاندارد لگراند را به شکلی منظم و یکپارچه در سیستم ترانکینگ خود جای دهد.</p>"""


RECORDS = [
    {  # 1 - phone socket wide 2-module 078731
        "category_name": "پریز تلفن", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "اتصال تلفن ثابت در منزل، دفتر کار و فضای تجاری"},
        "content_html": phone_socket_content("پهن ۲ ماژول", "078731", "۴۵×۴۵×۴۰"),
    },
    {  # 2 - phone socket narrow 1-module 078730
        "category_name": "پریز تلفن", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "اتصال تلفن ثابت در منزل، دفتر کار و فضای تجاری"},
        "content_html": phone_socket_content("باریک ۱ ماژول", "078730", "۲۲.۵×۴۵×۴۰"),
    },
    {  # 3 - Cat6A SFTP 2-module 076576
        "category_name": "پریز شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "اتصال کابل شبکه Cat6A SFTP در اتاق سرور و دیتاسنتر"},
        "content_html": network_socket_content("دو ماژول (پهن)", "Cat6A", "SFTP", "076576", "۱۰ گیگابیت بر ثانیه", "۵۰۰ مگاهرتز"),
    },
    {  # 4 - Cat6A SFTP 1-module 076573
        "category_name": "پریز شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "اتصال کابل شبکه Cat6A SFTP در اتاق سرور و دیتاسنتر"},
        "content_html": network_socket_content("یک ماژول (باریک)", "Cat6A", "SFTP", "076573", "۱۰ گیگابیت بر ثانیه", "۵۰۰ مگاهرتز"),
    },
    {  # 5 - Cat6 SFTP 2-module 076566
        "category_name": "پریز شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "اتصال کابل شبکه Cat6 SFTP در محیط با نویز الکترومغناطیسی"},
        "content_html": network_socket_content("دو ماژول (پهن)", "Cat6", "SFTP", "076566", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 6 - Cat6 SFTP 1-module 076563
        "category_name": "پریز شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "اتصال کابل شبکه Cat6 SFTP در محیط با نویز الکترومغناطیسی"},
        "content_html": network_socket_content("یک ماژول (باریک)", "Cat6", "SFTP", "076563", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 7 - Cat5e UTP 2-module 076554
        "category_name": "پریز شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "اتصال کابل شبکه Cat5e UTP در شبکه‌های خانگی و اداری کوچک"},
        "content_html": cat5e_socket_content("دو ماژول (پهن)", "076554"),
    },
    {  # 8 - Cat5e UTP 1-module 076551
        "category_name": "پریز شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "اتصال کابل شبکه Cat5e UTP در شبکه‌های خانگی و اداری کوچک"},
        "content_html": cat5e_socket_content("یک ماژول (باریک)", "076551", " بسته‌بندی این پریز به صورت ۱۰ عددی و کارتن مادر ۱۰۰ عددی است."),
    },
    {  # 9 - Cat6 UTP 2-module 076564
        "category_name": "پریز شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "اتصال کابل شبکه Cat6 UTP در شبکه‌های اداری و خانگی"},
        "content_html": network_socket_content("دو ماژول (پهن)", "Cat6", "UTP", "076564", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز",
                                                 " دوام آن تا ۲۵۰۰ بار اتصال و قطع مکرر بدون افت کیفیت است."),
    },
    {  # 10 - Cat6 UTP 1-module 076561
        "category_name": "پریز شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "اتصال کابل شبکه Cat6 UTP در دفاتر کار و مراکز تجاری"},
        "content_html": network_socket_content("یک ماژول (باریک)", "Cat6", "UTP", "076561", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز",
                                                 " ابعاد آن ۲۲.۵×۴۵ میلی‌متر است."),
    },
    {  # 11 - afshan wire 50mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "50", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "سیم‌کشی مدارهای اصلی، تغذیه تابلوهای برق صنعتی و مدارهای روشنایی با بار سنگین"},
        "content_html": afshan_wire_content("۱×۵۰", "از ۳۸۴ تار با قطر ۰.۳۹ میلی‌متر تشکیل شده است و", "12.4",
                                             "۰.۳۸۶ اهم بر کیلومتر", "۴۵۰/۷۵۰ ولت", "۲.۵ کیلوولت",
                                             "سیم‌کشی مدارهای اصلی، تغذیه تابلوهای برق صنعتی و مدارهای روشنایی با بار سنگین",
                                             " و DIN VDE 0295"),
    },
    {  # 12 - afshan wire 0.75mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "0.75", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0271، IEC 60228", "application": "سیم‌کشی تابلوهای برق، داخل دستگاه‌های الکتریکی و اتصال قطعات با جریان کم"},
        "content_html": afshan_wire_content("۱×۰.۷۵", "از رشته‌های نازک متعدد تشکیل شده است (مطابق دیتاشیت) و", "2.34",
                                             "۲۶ اهم بر کیلومتر", "۳۰۰/۵۰۰ ولت", "۲.۵ کیلوولت",
                                             "سیم‌کشی تابلوهای برق، داخل دستگاه‌های الکتریکی و اتصال قطعات با جریان کم در لوازم خانگی",
                                             " و DIN VDE 0271"),
    },
    {  # 13 - network cable Cat6 SFTP LSZH 032757
        "category_name": "کابل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "AWG 23", "conductor_material": "مس",
                   "standard": "", "application": "کابل‌کشی شبکه محلی با الزامات ایمنی حریق بالا"},
        "content_html": network_cable_lszh_content("032757", "Cat6", "SFTP", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 14 - afshan wire 0.5mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "0.5", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0271، IEC 60228", "application": "سیم‌کشی داخلی تجهیزات و دستگاه‌های الکتریکی ظریف و لوازم خانگی"},
        "content_html": afshan_wire_content("۱×۰.۵", "از ۱۶ تار با قطر ۰.۱۹ میلی‌متر تشکیل شده است و", "2.1",
                                             "مطابق دیتاشیت", "۳۰۰/۵۰۰ ولت", "۴ کیلوولت",
                                             "سیم‌کشی داخلی تجهیزات و دستگاه‌های الکتریکی ظریف و لوازم خانگی",
                                             " و DIN VDE 0271"),
    },
    {  # 15 - trunking partition 010582
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "جداسازی مسیر کابل برق و شبکه داخل ترانکینگ DLP لگراند"},
        "content_html": trunking_partition_content(),
    },
    {  # 16 - kadre 8-module door85 010998
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب هشت پریز یا مکانیزم روی ترانکینگ عرض ۱۰۵/۱۹۵ لگراند"},
        "content_html": kadre_content("010998", "۸۵ میلی‌متر", "ترانکینگ ۵۰ در ۱۰۵ و ۵۰ در ۱۹۵ لگراند", "هشت ماژول باریک یا چهار مکانیزم دو ماژولی"),
    },
    {  # 17 - kadre 6-module door85 010996
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب شش پریز یا مکانیزم روی ترانکینگ عرض ۱۰۵/۱۹۵ لگراند"},
        "content_html": kadre_content("010996", "۸۵ میلی‌متر", "ترانکینگ ۵۰ در ۱۰۵ و ۵۰ در ۱۹۵ لگراند", "شش ماژول باریک یا سه مکانیزم دو ماژولی"),
    },
    {  # 18 - kadre 4-module door85 010994
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب چهار پریز یا مکانیزم روی ترانکینگ عرض ۱۰۵/۱۹۵ لگراند"},
        "content_html": kadre_content("010994", "۸۵ میلی‌متر", "ترانکینگ ۵۰ در ۱۰۵ و ۵۰ در ۱۹۵ لگراند", "چهار ماژول باریک یا دو مکانیزم دو ماژولی"),
    },
    {  # 19 - kadre 2-module door85 010992
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب دو پریز یا یک مکانیزم روی ترانکینگ عرض ۱۰۵/۱۹۵ لگراند"},
        "content_html": kadre_content("010992", "۸۵ میلی‌متر", "ترانکینگ ۵۰ در ۱۰۵ و ۵۰ در ۱۹۵ لگراند", "دو ماژول باریک یا یک مکانیزم دو ماژولی"),
    },
    {  # 20 - kadre 8-module door65 010958
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب هشت پریز یا مکانیزم روی ترانکینگ عرض ۸۰/۱۵۰ لگراند"},
        "content_html": kadre_content("010958", "۶۵ میلی‌متر", "ترانکینگ ۵۰ در ۸۰ و ۵۰ در ۱۵۰ لگراند", "هشت ماژول باریک یا چهار مکانیزم دو ماژولی"),
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
    with open(os.path.join(DATA_DIR, "batch39_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch39_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch39_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
