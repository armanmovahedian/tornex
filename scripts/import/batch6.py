# -*- coding: utf-8 -*-
"""Batch 6: 9 more MCB variants + 3 Legrand Salbei switch/outlet products."""
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

MCB_STD = "IEC 60947-2، IEC 60898"
POLE_APP = {
    "دو پل": "حفاظت از مدارهای الکتریکی تک‌فاز در تابلوهای برق، ساختمان‌های مسکونی و تجاری",
    "یک پل": "حفاظت از مدارهای تک‌فاز سبک تا سنگین در تابلوهای برق مسکونی، تجاری و صنعتی",
}


def mcb_content(amp, poles, curve):
    return f"""<p>کلید مینیاتوری {poles} {amp} آمپر کلاس {curve} اشنایدر از سری Multi9 (خانواده C60N) با تکنولوژی تریپ حرارتی-مغناطیسی، در برابر اضافه‌بار طولانی‌مدت و اتصال کوتاه ناگهانی محافظت می‌کند. ظرفیت قطع آن ۶ کیلوآمپر است و طول عمر مکانیکی آن تا ۲۰۰۰۰ سیکل عملکرد تست شده است.</p>
<p>منحنی قطع {curve} این کلید برای مدارهایی با جریان هجومی راه‌اندازی متوسط مانند موتورها و تجهیزات القایی مناسب است. نصب آن روی ریل استاندارد DIN ساده است و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


MCB_LIST = [
    {"amp": 25, "poles": "دو پل", "curve": "C"},
    {"amp": 4, "poles": "دو پل", "curve": "C"},
    {"amp": 2, "poles": "دو پل", "curve": "C"},
    {"amp": 63, "poles": "یک پل", "curve": "C"},
    {"amp": 50, "poles": "یک پل", "curve": "C"},
    {"amp": 40, "poles": "یک پل", "curve": "C"},
    {"amp": 32, "poles": "یک پل", "curve": "C"},
    {"amp": 25, "poles": "یک پل", "curve": "C"},
    {"amp": 4, "poles": "یک پل", "curve": "C"},
]

AUTHORED = []
for m in MCB_LIST:
    AUTHORED.append({
        "specs": {"brand": "اشنایدر", "size_diameter": "", "conductor_material": "",
                   "standard": MCB_STD, "application": POLE_APP[m["poles"]]},
        "category_name": "فیوز مینیاتوری", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": mcb_content(m["amp"], m["poles"], m["curve"]),
    })

AUTHORED += [
    {  # 10 - push button
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IP54، IEC 60669-1",
                   "application": "مدارهای روشنایی و کنترل تردد با توان پایین در راهروها، پارکینگ‌ها، راه‌پله‌ها و فضاهای مشاع"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>دکمه فشاری Push Button سری سالبی لگراند با سطح مات و ضدلک ساخته شده که در برابر جذب گردوغبار و اثر انگشت مقاوم است و برای فضاهای پرتردد مانند راهروها و مشاعات مناسب است. با درجه حفاظت IP54 در برابر گردوغبار و پاشش آب از هر جهت محافظت شده و برای محیط‌های داخلی و نیمه‌باز مناسب است.</p>
<p>این دکمه از نوع لحظه‌ای (Momentary) است: فقط هنگام فشار دادن مدار را وصل می‌کند و با رها کردن قطع می‌شود، مناسب برای زنگ درب، روشنایی راهرو و سیستم‌های اعلام حریق. جریان نامی آن ۶ آمپر و ولتاژ نامی ۲۵۰ ولت است و در قالب ۲ ماژول توکار نصب می‌شود.</p>""",
    },
    {  # 11 - adapter
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "EN 62208، EN 61439-3",
                   "application": "ترکیب مکانیزم‌های سری Mosaic با کلید و پریزهای سری Salbei در پروژه‌های برقی"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>آداپتور تبدیل موزاییک به سالبی لگراند قطعه‌ای کوچک از جنس ترموپلاستیک است که امکان استفاده از مکانیزم‌های سری Mosaic را در ترکیب با کلید و پریزهای سری Salbei فراهم می‌کند. این ویژگی انعطاف‌پذیری بیشتری در طراحی و اجرای پروژه‌های الکتریکی ایجاد می‌کند.</p>
<p>این آداپتور با رنگ سفید و ظرفیت ۲ ماژول، نصب توکار دارد و مطابق استانداردهای EN 62208 (محفظه‌های تجهیزات ولتاژ پایین) و EN 61439-3 (تابلوهای توزیع) تولید شده است.</p>""",
    },
    {  # 12 - antenna outlet
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "", "standard": "IP20، IEC 60695-2-11",
                   "application": "اتصال کابل آنتن و ماهواره در ساختمان‌های مسکونی و اداری با قابلیت انتقال سیگنال زنجیره‌ای بین چند پریز"},
        "category_name": "کلید و پریز", "category_parent_name": "سایر تجهیزات کابل",
        "content_html": """<p>پریز میانی آنتن و ماهواره سالبی لگراند با کانکتورهای F و ۹.۵۲ میلی‌متری، سازگاری گسترده‌ای با کابل‌های آنتن و ماهواره دارد. وزن آن ۱۰۰ گرم و عمق نصب ۱۷.۴ میلی‌متر است که آن را برای دیوارهای با عمق کم نیز مناسب می‌سازد. درجه حفاظت IP20 دارد و برای محیط‌های داخلی طراحی شده است.</p>
<p>این پریز قابلیت Loop-through (حلقه‌ای) دارد که امکان انتقال سیگنال به‌صورت متوالی به پریزهای بعدی را فراهم می‌کند و در ساختمان‌های چندواحدی هزینه کابل‌کشی را کاهش می‌دهد. ظرفیت آن ۲ ماژول و نصب آن به‌صورت توکار است.</p>""",
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
    with open(os.path.join(DATA_DIR, "batch6_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch6_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch6_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
