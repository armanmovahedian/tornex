# -*- coding: utf-8 -*-
"""Batch 9: 20 products -- Cisco switches, Legrand Plexo (waterproof) accessories,
Simia Cat6 network cable, Simia telephone cable family, antenna cable, ground wire."""
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

CISCO_STD = "IEEE 802.3، IEEE 802.1Q، IEEE 802.1D، IEEE 802.3ad، IEEE 802.1s، IEEE 802.1w"
CISCO_APP = "شبکه‌های سازمانی، دیتاسنترها و زیرساخت‌های ISP با نیاز به سوئیچینگ لایه ۲ پرسرعت"


def switch_content(ports, poe, uplink, edition, switching, forward):
    poe_desc = (f"{ports} پورت PoE+ دارد که امکان تغذیه مستقیم دوربین‌های نظارتی، اکسس‌پوینت‌های وایرلس و تلفن‌های VoIP را از طریق کابل شبکه فراهم می‌کند"
                if poe else f"{ports} پورت اترنت استاندارد (بدون PoE) دارد")
    uplink_desc = ("۴ پورت آپلینک ۱۰ گیگابیت بر ثانیه" if uplink == "10G" else "۴ پورت آپلینک ۱ گیگابیت بر ثانیه")
    edition_desc = ("و از نرم‌افزار Network Advantage با قابلیت‌های مسیریابی لایه ۳ مانند OSPF و EIGRP پشتیبانی می‌کند"
                     if edition == "Advantage" else "و از نرم‌افزار Network Essentials با امکانات مدیریتی و امنیتی ضروری لایه ۲ پشتیبانی می‌کند")
    return f"""<p>سوییچ {ports} پورت سیسکو سری Catalyst 9200L با {uplink_desc} طراحی شده است. این سوییچ {poe_desc} {edition_desc}. ظرفیت سوئیچینگ آن {switching} گیگابیت بر ثانیه و نرخ پردازش بسته آن {forward} میلیون بسته در ثانیه است.</p>
<p>این سوییچ از رمزگذاری AES-128 MACsec، Full Flexible NetFlow برای پایش ترافیک، Jumbo Frame تا ۹۱۹۸ بایت، VLAN (تا ۱۰۲۴ عدد) و QoS پشتیبانی می‌کند. پهنای باند استکینگ آن ۸۰ گیگابیت بر ثانیه است و از Cisco SD-Access و Plug and Play پشتیبانی می‌کند.</p>"""


def telephone_content(pairs, gauge, resistance, weight_100m, diameter):
    return f"""<p>کابل تلفن {pairs} زوج {gauge} سیمیا با ساختار J-2Y(St)Y از هادی مسی مفتولی (کلاس ۱) با قطر {gauge} میلی‌متر و عایق پلی‌اتیلن ساخته شده است. مقاومت DC هادی آن {resistance} اهم بر کیلومتر در دمای ۲۰ درجه سانتی‌گراد است. شیلد OSCR شامل یک سیم تخلیه مسی قلع‌اندود به قطر ۰.۴ میلی‌متر و نوار آلومینیوم-پلی‌استر با همپوشانی ۲۵٪، محافظت در برابر نویز و تداخل الکترومغناطیسی را فراهم می‌کند.</p>
<p>روکش PVC خاکستری آن به ضخامت ۰.۶ میلی‌متر در برابر سایش و عوامل محیطی مقاوم است. قطر نهایی کابل حدود {diameter} میلی‌متر و وزن هر کلاف ۱۰۰ متری آن حدود {weight_100m} کیلوگرم است. این کابل مطابق IEC 60332-1 در برابر گسترش شعله مقاوم است، در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و برای سیم‌کشی داخلی سیستم‌های تلفن و مخابرات مناسب است.</p>"""


TEL_APP = "سیم‌کشی داخلی سیستم‌های تلفن و مخابرات در ساختمان‌های مسکونی، اداری و تجاری"

RECORDS = [
    {  # 1 - cisco switch
        "category_name": "سوییچ و مبدل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "سیسکو", "size_diameter": "", "conductor_material": "", "standard": CISCO_STD, "application": CISCO_APP},
        "content_html": switch_content(48, False, "1G", "Essentials", "104", "154.76"),
    },
    {  # 2
        "category_name": "سوییچ و مبدل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "سیسکو", "size_diameter": "", "conductor_material": "", "standard": CISCO_STD, "application": CISCO_APP},
        "content_html": switch_content(24, False, "1G", "Essentials", "56", "83.33"),
    },
    {  # 3
        "category_name": "سوییچ و مبدل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "سیسکو", "size_diameter": "", "conductor_material": "", "standard": CISCO_STD, "application": CISCO_APP},
        "content_html": switch_content(24, True, "1G", "Essentials", "56", "83.33"),
    },
    {  # 4 - plexo box
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "NF C 61-314، IEC 60884-1، NFC 68-104",
                   "application": "نصب روکار کلید و پریز در محیط‌های مرطوب و صنعتی مانند استخر، حمام و موتورخانه"},
        "content_html": """<p>باکس روکار ضد آب پلکسو لگراند از پلی‌پروپیلن (PP) مقاوم در برابر اشعه ماوراءبنفش و فاقد مواد هالوژنی ساخته شده و درجه حفاظت IP55 دارد؛ یعنی در برابر نفوذ گردوغبار و پاشش آب از هر جهت محافظت می‌کند. برای نصب در فضاهای مرطوب مانند استخر، حمام، موتورخانه و آزمایشگاه مناسب است.</p>
<p>طراحی ماژولار این باکس امکان ترکیب با مغزی‌های کلید و پریز پلکسو را فراهم می‌کند و به همراه ورودی‌های کابل تعبیه‌شده، نصب سریعی دارد. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 5 - plexo switch mechanism
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "CEI 60695-2-11، NF EN 60669-1، NBN EN 60669-1، CEI 60669-1",
                   "application": "نصب کلید در محیط‌های مرطوب و صنعتی مانند حمام، استخر و آزمایشگاه"},
        "content_html": """<p>مغزی کلید تک پل ضد آب پلکسو لگراند با درجه حفاظت IP55 در برابر گردوغبار و پاشش آب از هر جهت محافظت می‌کند و برای نصب در حمام، استخر، موتورخانه و سرویس‌های بهداشتی مناسب است. با ولتاژ نامی ۲۵۰ ولت و جریان نامی ۱۰ آمپر، عملکرد پایدار و ایمنی دارد.</p>
<p>این مغزی به‌صورت توکار با کادر سری پلکسو یا به‌صورت روکار همراه با باکس روکار پلکسو قابل نصب است و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 6 - plexo socket mechanism
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "CEI 60695-2-11، IEC 60884-1",
                   "application": "اتصال برق در محیط‌های مرطوب، صنعتی و فضاهای باز با نیاز به محافظت در برابر آب"},
        "content_html": """<p>مغزی پریز برق ارتدار ضد آب پلکسو لگراند با درجه حفاظت IP55 در برابر نفوذ گردوغبار و پاشش آب از هر جهت مقاوم است و برای نصب در حمام، استخر، موتورخانه، آزمایشگاه و حتی فضاهای باز مانند حیاط مناسب است. با ولتاژ نامی ۲۵۰ ولت و جریان نامی ۱۶ آمپر، اتصال ایمن تجهیزات برقی را فراهم می‌کند.</p>
<p>این مغزی به‌صورت توکار با کادر پلکسو یا به‌صورت روکار همراه با باکس روکار (کد ۰۶۹۶۸۹) قابل نصب است و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 7 - cat6 utp pvc
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "سیمیا", "size_diameter": "", "conductor_material": "مس", "standard": "TIA/EIA 568.B، IEC 60332-1",
                   "application": "شبکه‌های داخلی ساختمان با نیاز به انتقال داده گیگابیتی"},
        "content_html": """<p>کابل شبکه Cat6 UTP سیمیا با روکش PVC از ساختار Cu/PE/PE/PVC و قطر کلی ۶.۴ میلی‌متر ساخته شده است. هادی‌های آن از مس مفتولی با قطر ۰.۵۶ میلی‌متر و عایق پلی‌اتیلن به ضخامت ۰.۲۲ میلی‌متر تشکیل شده که رسانایی خوب و کاهش افت سیگنال را تضمین می‌کند. پهنای باند آن ۲۵۰ مگاهرتز و سرعت انتقال داده آن تا ۱ گیگابیت بر ثانیه است.</p>
<p>این کابل تحت تست فلوک (پارامترهایی مانند ACR-N و RL) مطابق استانداردهای TIA Cat 6 تأیید شده و مطابق IEC 60332-1 در برابر گسترش شعله مقاوم است. وزن آن حدود ۴۲ کیلوگرم بر کیلومتر است و در کارتن ۳۰۵ متری عرضه می‌شود.</p>""",
    },
    {  # 8 - cat6 utp lszh
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "سیمیا", "size_diameter": "", "conductor_material": "مس", "standard": "TIA/EIA 568.B، IEC 60332-1، IEC 60754-1، IEC 61034-1، ASTM D 2863",
                   "application": "شبکه‌های داخلی حساس به ایمنی حریق مانند بیمارستان‌ها، دیتاسنترها و متروها"},
        "content_html": """<p>کابل شبکه Cat6 UTP سیمیا با روکش LSZH (کم‌دود و بدون هالوژن) با ساختار بدون شیلد (UTP) طراحی شده و برای شبکه‌های با نویز پایین و پهنای باند بالا مناسب است. قطر خارجی آن ۶.۴ میلی‌متر، ضخامت عایق پلی‌اتیلن آن ۰.۲۲ میلی‌متر و وزن آن حدود ۴۳ کیلوگرم بر کیلومتر است. پهنای باند آن ۲۵۰ مگاهرتز است.</p>
<p>مطابق استاندارد IEC 60754-1 گازهای اسیدی کمتر از ۰.۵٪ تولید می‌کند و طبق IEC 61034-1 و IEC 60332-1 دود و شعله کمی دارد، به همین دلیل برای بیمارستان‌ها، دیتاسنترها، مترو و مراکز پرتردد مناسب است. در کارتن ۳۰۵ متری عرضه می‌شود.</p>""",
    },
    {  # 9 - cat6 sftp pvc
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "سیمیا", "size_diameter": "", "conductor_material": "مس", "standard": "TIA/EIA 568.B، IEC 60332-1",
                   "application": "شبکه‌های سازمانی و خانگی با نیاز به شیلدینگ در برابر نویز"},
        "content_html": """<p>کابل شبکه Cat6 SFTP سیمیا با روکش PVC از چهار زوج سیم با شیلد دوتایی (نوار پلی‌استر و فویل آلومینیوم طولی) ساخته شده که تداخل الکترومغناطیسی را به حداقل می‌رساند. هادی مسی آن قطر ۰.۵۶ میلی‌متر و عایق آن ضخامت ۰.۲۸ میلی‌متر دارد. پهنای باند آن ۲۵۰ مگاهرتز است.</p>
<p>قطر نهایی این کابل ۷.۹ میلی‌متر و وزن آن حدود ۶۷ کیلوگرم بر کیلومتر است. مطابق IEC 60332-1 در برابر گسترش شعله مقاوم است و در قرقره‌های ۵۰۰ متری عرضه می‌شود. مناسب پروژه‌های داخلی است و مقاومت در برابر اشعه UV ندارد.</p>""",
    },
    {  # 10 - cat6 sftp lszh
        "category_name": "کابل شبکه", "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "سیمیا", "size_diameter": "", "conductor_material": "مس", "standard": "TIA/EIA 568.B، IEC 60332-1، IEC 60754-1، IEC 61034-1، ASTM D 2863",
                   "application": "شبکه‌های سازمانی حساس به ایمنی حریق با نیاز به شیلدینگ در برابر نویز"},
        "content_html": """<p>کابل شبکه Cat6 SFTP سیمیا با روکش LSZH از چهار زوج به‌هم‌تابیده با شیلد فویل آلومینیومی و شیلد بافته‌شده از مس قلع‌اندود ساخته شده که محافظت قوی در برابر نویز و تداخل الکترومغناطیسی (EMI) ایجاد می‌کند. پهنای باند آن ۲۵۰ مگاهرتز و سرعت انتقال آن تا ۱ گیگابیت بر ثانیه است. قطر نهایی آن ۷.۹ میلی‌متر و وزن آن حدود ۶۸ کیلوگرم بر کیلومتر است.</p>
<p>روکش LSZH آن هنگام آتش‌سوزی دود و گازهای سمی کمی تولید می‌کند (مطابق IEC 60754-1، IEC 61034-1 و ASTM D2863) و برای بیمارستان‌ها، دیتاسنترها، مترو و مراکز پرتردد مناسب است. در قرقره‌های ۵۰۰ متری عرضه می‌شود.</p>""",
    },
    {  # 11 - سیم افشان 0.5
        "category_name": "سیم افشان", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "0.5", "conductor_material": "مس", "standard": "IEC 60227-3، IEC 60332-1",
                   "application": "مدارهای اتصال قطعات الکترونیکی ظریف، تابلوهای برق و اتصالات جزئی (غیرمجاز برای کابل‌کشی ساختمان طبق مقررات ملی)"},
        "content_html": """<p>سیم افشان ۰.۵ سیمیا (NYAF) از هادی مسی کلاس ۵ با ۱۶ تار به قطر ۰.۱۹۲ میلی‌متر ساخته شده که انعطاف‌پذیری بالایی برای نصب در فضاهای تنگ دارد. عایق PVC آن ضخامت ۰.۶ میلی‌متر دارد و مقاومت الکتریکی آن حداکثر ۳۹ اهم بر کیلومتر در دمای ۲۰ درجه سانتی‌گراد است. قطر نهایی آن ۲ میلی‌متر و وزن هر کلاف ۱۰۰ متری آن ۸۰۰ گرم است.</p>
<p>این سیم برای مدارهای اتصال قطعات الکترونیکی ظریف، روشنایی کم‌مصرف و پروژه‌های DIY مناسب است، مطابق IEC 60332-1 در برابر گسترش شعله مقاوم است و در بازه دمایی ۲۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. طبق نشریه ۱۱۰ و مقررات ملی ساختمان، استفاده از این سیم در کابل‌کشی ساختمان مجاز نیست و صرفاً برای مصارف دیگر مانند تابلوهای برقی مناسب است.</p>""",
    },
    {  # 12 - telephone 10 pair 0.5
        "category_name": "کابل تلفن", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "10 زوج × 0.5 میلی‌متر", "conductor_material": "مس", "standard": "IEC 60332-1", "application": TEL_APP},
        "content_html": telephone_content(10, "0.5", "97.8", "6.6", "7"),
    },
    {  # 13 - telephone 6 pair 0.6
        "category_name": "کابل تلفن", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "6 زوج × 0.6 میلی‌متر", "conductor_material": "مس", "standard": "IEC 60332-1", "application": TEL_APP},
        "content_html": telephone_content(6, "0.6", "67.9", "5.7", "6.1"),
    },
    {  # 14 - telephone 6 pair 0.5
        "category_name": "کابل تلفن", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "6 زوج × 0.5 میلی‌متر", "conductor_material": "مس", "standard": "IEC 60332-1", "application": TEL_APP},
        "content_html": telephone_content(6, "0.5", "97.8", "4.5", "5.8"),
    },
    {  # 15 - telephone 4 pair 0.5
        "category_name": "کابل تلفن", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "4 زوج × 0.5 میلی‌متر", "conductor_material": "مس", "standard": "IEC 60332-1", "application": TEL_APP},
        "content_html": telephone_content(4, "0.5", "97.8", "3.2", "5.5"),
    },
    {  # 16 - telephone 4 pair 0.6
        "category_name": "کابل تلفن", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "4 زوج × 0.6 میلی‌متر", "conductor_material": "مس", "standard": "IEC 60332-1", "application": TEL_APP},
        "content_html": telephone_content(4, "0.6", "67.9", "4", "5.6"),
    },
    {  # 17 - telephone 2 pair 0.6
        "category_name": "کابل تلفن", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "2 زوج × 0.6 میلی‌متر", "conductor_material": "مس", "standard": "IEC 60332-1", "application": TEL_APP},
        "content_html": telephone_content(2, "0.6", "67.9", "2.5", "4.6"),
    },
    {  # 18 - telephone 2 pair 0.5
        "category_name": "کابل تلفن", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "2 زوج × 0.5 میلی‌متر", "conductor_material": "مس", "standard": "IEC 60332-1", "application": TEL_APP},
        "content_html": telephone_content(2, "0.5", "97.8", "2", "4.3"),
    },
    {  # 19 - antenna cable
        "category_name": "کابل آنتن", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "", "conductor_material": "مس", "standard": "IEC 60332-1",
                   "application": "سیستم‌های آنتن و ماهواره خانگی و تجاری"},
        "content_html": """<p>کابل آنتن کواکسیال سیمیا (۴.۵C-2V) از هادی مسی مرکزی، عایق فوم پلی‌اتیلن، شیلد مسی بافته‌شده (قطر ۰.۱۱۵ میلی‌متر، پوشش ۶۵٪) و روکش PVC سفید ساخته شده است. امپدانس آن ۷۵ اهم است که با اکثر تجهیزات آنتن و گیرنده تلویزیونی سازگار است. وزن آن حدود ۴۸ گرم بر متر است.</p>
<p>این کابل مطابق IEC 60332-1 در برابر گسترش شعله مقاوم است، در بازه دمایی ۲۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و در کلاف‌های ۱۰۰ متری و قرقره‌های ۵۰۰ متری عرضه می‌شود.</p>""",
    },
    {  # 20 - ground wire
        "category_name": "سیم افشان", "category_parent_name": "سیم و کابل خراسان افشارنژاد",
        "specs": {"brand": "سیمیا", "size_diameter": "70", "conductor_material": "مس", "standard": "IEC 60227-3، IEC 60332-1",
                   "application": "سیستم‌های اتصال به زمین (ارتینگ) در ساختمان‌های مسکونی، تجاری و صنعتی"},
        "content_html": """<p>سیم ارت افشان ۷۰ سیمیا (NYAF، مطابق کد H07V-K) از ۵۷۶ تار مسی به قطر ۰.۳۸۲ میلی‌متر ساخته شده و قطر کلی آن ۱۴.۶ میلی‌متر است. عایق PVC آن ضخامت ۱.۴ میلی‌متر دارد و هادی آن از مس آنیل‌شده کلاس ۵ است که انعطاف‌پذیری بالایی ایجاد می‌کند. رنگ آن زرد-سبز (رنگ استاندارد سیم ارت) است.</p>
<p>این سیم با ولتاژ نامی ۴۵۰/۷۵۰ ولت، مقاومت الکتریکی حداکثر ۰.۲۷۲ اهم بر کیلومتر در دمای ۲۰ درجه سانتی‌گراد دارد و مطابق IEC 60332-1 در برابر گسترش شعله مقاوم است. برای اتصال زمین تجهیزات با جریان بالا در ساختمان‌های مسکونی، تجاری و صنعتی مناسب است و در بازه دمایی ۲۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. وزن هر کلاف ۱۰۰ متری آن حدود ۷۱.۲ کیلوگرم است.</p>""",
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
    with open(os.path.join(DATA_DIR, "batch9_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch9_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch9_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
