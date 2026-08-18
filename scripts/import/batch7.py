# -*- coding: utf-8 -*-
"""Batch 7: Legrand Salbei/Mosaic switch-and-outlet accessories + a Cisco switch."""
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

SWITCH_APP = "منازل، دفاتر اداری، هتل‌ها و مراکز تجاری"

AUTHORED = [
    {  # 1 - network outlet
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IP20، IEC 60695-2-11",
                   "application": "اتصال شبکه پرسرعت CAT6 در منازل، دفاتر، هتل‌ها و مراکز تجاری"},
        "category_name": "پریز شبکه", "category_parent_name": "تجهیزات شبکه",
        "content_html": """<p>پریز شبکه دو پورت سالبی لگراند از استاندارد CAT6 STP پشتیبانی می‌کند که سرعت انتقال داده تا ۱ گیگابیت بر ثانیه را فراهم کرده و در برابر تداخل الکترومغناطیسی محافظت می‌کند. بدنه آن از ترموپلاستیک باکیفیت ساخته شده و نصب آن به‌صورت توکار و همسطح با دیوار انجام می‌شود.</p>
<p>این پریز با ظرفیت ۲ ماژول و رنگ سفید، برای منازل، دفاتر، هتل‌ها و مراکز تجاری مناسب است و درجه حفاظت IP20 دارد.</p>""",
    },
    {  # 2 - surface box
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IEC 60695-2-11",
                   "application": "نصب روکار کلید و پریز در منازل، دفاتر، فروشگاه‌ها و هتل‌ها"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>باکس روکار سالبی لگراند از مواد هالوژن‌فری و ظاهر پلی‌گلاس (شبیه شیشه) ساخته شده که در برابر خط‌وخش و ضربه مقاوم است و به‌راحتی تمیز می‌شود. قطعات عایق آن خودخاموش‌شونده هستند و تا دمای ۶۵۰ درجه سانتی‌گراد را به مدت ۳۰ ثانیه تحمل می‌کنند.</p>
<p>این باکس با ظرفیت ۲ ماژول و رنگ سفید، برای نصب روکار در منازل، دفاتر، فروشگاه‌ها و هتل‌ها مناسب است و در بازه دمایی ۵- تا ۳۵+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 3 - 5-gang frame
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IEC 60695-2-11",
                   "application": "نصب هم‌زمان چند مکانیزم کلید و پریز در یک قاب، مناسب فضاهای بزرگ اداری و مسکونی"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>کادر پنج خانه سالبی لگراند از پلاستیک هالوژن‌فری ساخته شده که در هنگام آتش‌سوزی گاز سمی تولید نمی‌کند. با ظرفیت ۱۰ ماژول، امکان نصب هم‌زمان تعداد زیادی مکانیزم کلید و پریز را در یک قاب واحد فراهم می‌کند و نیاز به کادرهای متعدد را در فضاهای بزرگ کاهش می‌دهد.</p>
<p>نصب آن به‌صورت توکار است و با رنگ سفید یا کرم (کد ۷۶۷۳۴۵) عرضه می‌شود.</p>""",
    },
    {  # 4 - 4-gang frame
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IEC 60695-2-11",
                   "application": "نصب چند مکانیزم کلید و پریز در یک قاب"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>کادر چهار خانه سالبی لگراند با ظرفیت ۸ ماژول، امکان نصب تعداد زیادی از مکانیزم‌های کلید و پریز را در یک قاب واحد فراهم می‌کند. بدنه آن از پلاستیک مرغوب و عایق ساخته شده که در برابر ضربه و فشار مقاوم است.</p>
<p>نصب آن به‌صورت توکار و همسطح با دیوار انجام می‌شود و با رنگ سفید یا کرم (کد ۷۶۷۳۴۴) عرضه می‌شود.</p>""",
    },
    {  # 5 - 3-gang frame
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IEC 60695-2-11",
                   "application": "نصب چند مکانیزم کلید و پریز در محیط‌های اداری، هتل‌ها و فضاهای پرتردد"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>کادر سه خانه سالبی لگراند از مواد هالوژن‌فری و مقاوم در برابر اشعه ماوراءبنفش ساخته شده که از تغییر رنگ در اثر نور خورشید جلوگیری می‌کند. طبق دیتاشیت، قطعات عایق آن تا دمای ۸۵۰ درجه سانتی‌گراد و سایر قطعات تا ۶۵۰ درجه سانتی‌گراد به مدت ۳۰ ثانیه در برابر شعله مقاومت می‌کنند.</p>
<p>با ظرفیت ۶ ماژول، برای محیط‌های اداری، هتل‌ها و فضاهای پرتردد مناسب است و به‌صورت توکار (چنگکی یا پیچی) نصب می‌شود. با رنگ سفید یا کرم (کد ۷۶۷۳۴۳) عرضه می‌شود.</p>""",
    },
    {  # 6 - 2-gang frame
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IEC 60695-2-11",
                   "application": "نصب چند مکانیزم کلید و پریز در منازل، ادارات، هتل‌ها و مراکز تجاری"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>کادر دو خانه سالبی لگراند با ظرفیت ۴ ماژول، امکان نصب چند مکانیزم کلید و پریز را در یک قاب فراهم می‌کند. جنس پلاستیکی آن مقاومت خوبی در برابر ضربه و حرارت دارد و طراحی آن از جدا شدن ناخواسته مکانیزم‌ها جلوگیری می‌کند.</p>
<p>نصب آن به‌صورت توکار و در جعبه‌های برق استاندارد انجام می‌شود و با رنگ سفید یا کرم (کد ۷۶۷۳۴۲) عرضه می‌شود.</p>""",
    },
    {  # 7 - 1-gang frame
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IEC 60695-2-11",
                   "application": "نصب یک مکانیزم کلید یا پریز در منازل و فضاهای تجاری"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>کادر تک خانه سالبی لگراند با ظرفیت ۲ ماژول، به همراه یک عدد قاب کامل عرضه می‌شود و نیازی به تهیه قاب جداگانه ندارد. مکانیزم‌های کلید و پریز به‌صورت محکم در آن جای می‌گیرند و از جنس پلاستیک مرغوب و مقاوم در برابر ضربه و فشار ساخته شده است.</p>
<p>نصب آن به‌صورت توکار است و با رنگ سفید یا کرم (کد ۷۶۷۳۴۱) عرضه می‌شود.</p>""",
    },
    {  # 8 - socket with door
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IP20، IEC 60884-1",
                   "application": "پریز برق خانگی و اداری با نیاز به محافظت کودک و مقاومت در برابر گردوغبار"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>پریز برق درب‌دار سالبی لگراند دارای درب محافظ است که ایمنی کودکان را تضمین کرده و از نفوذ گردوغبار و رطوبت جلوگیری می‌کند. با ولتاژ نامی ۲۵۰ ولت و جریان نامی ۱۶ آمپر، توانی معادل ۳۶۸۰ وات را پشتیبانی می‌کند که برای اغلب وسایل برقی خانگی و اداری کافی است.</p>
<p>ابعاد آن ۷۱×۷۱×۵۰.۵ میلی‌متر و وزن آن ۸۱ گرم است. بدنه آن از آکریلونیتریل استایرن اکریلات (ASA) و پلی‌کربنات مطابق استاندارد IEC 60884-1 ساخته شده و نصب آن به‌صورت توکار انجام می‌شود.</p>""",
    },
    {  # 9 - intermediate switch
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IP20، IEC 60669-1",
                   "application": "کنترل روشنایی از سه نقطه یا بیشتر در راهروها و فضاهای بزرگ"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>کلید تک پل صلیبی (Permütatör) سالبی لگراند برای کنترل روشنایی از سه نقطه یا بیشتر استفاده می‌شود و در راهروهای طولانی و فضاهای بزرگ کاربرد دارد. این کلید تنها یک مسیر جریان را قطع و وصل می‌کند و اتصالات داخلی آن برای سیستم‌های چند نقطه‌ای طراحی شده است.</p>
<p>با ولتاژ نامی ۲۵۰ ولت و جریان نامی ۱۰ آمپر، توان ۲۳۰۰ وات را پشتیبانی می‌کند. ابعاد آن ۷۱×۷۱×۴۲ میلی‌متر و وزن آن ۷۷ گرم است و از ترموپلاستیک مطابق استاندارد IEC 60669-1 ساخته شده است.</p>""",
    },
    {  # 10 - MK earthed socket
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IK04، IP41، IEC 60695-2-11",
                   "application": "اتصال تجهیزات حساس مانند کولر گازی، سیستم‌های کامپیوتری و تجهیزات شبکه با استاندارد انگلیسی BS1363"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>پریز برق ارتدار سه‌شاخ موزائیک لگراند مطابق استاندارد انگلیسی BS1363 طراحی شده و برای اتصال تجهیزات حساس مانند کولرهای گازی، سیستم‌های کامپیوتری و تجهیزات شبکه مناسب است. ترمینال‌های پیچی آن ظرفیت ۴ میلی‌متر مربع دارند و طول سیم‌لختی استاندارد برای نصب ۹ میلی‌متر است.</p>
<p>درجه حفاظت IP41 در برابر نفوذ اجسام جامد و رطوبت محدود، و مقاومت مکانیکی IK04 در برابر ضربه تا ۰.۵ ژول دارد. بدنه آن از پلی‌کربنات هالوژن‌فری با ابعاد ۴۵×۴۵ میلی‌متر ساخته شده و در دمای ۵- تا ۳۵+ درجه سانتی‌گراد کار می‌کند.</p>""",
    },
    {  # 11 - narrow single switch
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IK04، IP31D، IEC 60695-2-11",
                   "application": "ادارات، دانشگاه‌ها، بیمارستان‌ها، فروشگاه‌های زنجیره‌ای، مترو و هتل‌ها"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>کلید تک پل باریک موزائیک لگراند با ابعاد ۴۵×۲۲.۵ میلی‌متر، با تمامی مکانیزم‌های سری موزائیک و کادرهای استاندارد ۴۵×۴۵ میلی‌متری سازگار است. بدنه آن از پلی‌کربنات مقاوم در برابر اشعه UV و حرارت ساخته شده و فاقد هالوژن است.</p>
<p>ترمینال‌های اتوماتیک آن نصب را بدون نیاز به ابزار خاص ساده می‌کند و قابلیت افزودن چراغ نشانگر LED دارد. با جریان نامی ۱۰ آمپر و ولتاژ نامی ۲۵۰ ولت، درجه حفاظت IP31D و مقاومت مکانیکی IK04 دارد.</p>""",
    },
    {  # 12 - cisco switch
        "specs": {"brand": "سیسکو", "size_diameter": "", "conductor_material": "",
                   "standard": "IEEE 802.3، IEEE 802.1Q، IEEE 802.1D، IEEE 802.3ad",
                   "application": "شبکه‌های سازمانی، دیتاسنترها و زیرساخت‌های ISP با نیاز به سوئیچینگ لایه ۲ پرسرعت"},
        "category_name": "سوییچ و مبدل شبکه", "category_parent_name": "تجهیزات شبکه",
        "content_html": """<p>سوییچ ۴۸ پورت سیسکو Catalyst C9200L-48T-4X-A برای شبکه‌های سازمانی طراحی شده و ۴ پورت آپلینک ۱۰ گیگابیت بر ثانیه دارد (برخلاف مدل 4G که فقط ۱ گیگابیت بر ثانیه ارائه می‌دهد). ظرفیت سوئیچینگ آن ۱۷۶ گیگابیت بر ثانیه و نرخ پردازش بسته آن ۲۶۱.۹ میلیون بسته در ثانیه است که آن را برای دیتاسنترها و سازمان‌های بزرگ مناسب می‌سازد. پهنای باند استکینگ ۸۰ گیگابیت بر ثانیه امکان اتصال یکپارچه چند سوییچ را فراهم می‌کند.</p>
<p>این سوییچ از رمزگذاری AES-128 MACsec، VLAN (تا ۱۰۲۴ عدد)، ACL و QoS برای مدیریت پهنای باند پشتیبانی می‌کند. حافظه رم آن ۲ گیگابایت و حافظه فلش آن ۴ گیگابایت است. نسخه Network Advantage آن قابلیت‌های مدیریتی پیشرفته‌تری نسبت به نسخه Essentials دارد و از Cisco SD-Access و Plug and Play پشتیبانی می‌کند.</p>""",
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
    with open(os.path.join(DATA_DIR, "batch7_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch7_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch7_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
