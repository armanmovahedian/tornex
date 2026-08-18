# -*- coding: utf-8 -*-
"""Batch 40: 20 products -- all Legrand DLP trunking accessories:
3 module frames (kadre), 2 door seals, 4 flat 90-degree angles, 3
T-junctions, 3 end caps, 2 body joint seals, 2 external angles, and
1 internal angle."""
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


def kadre_content(code, door_width, trunking_examples, mechanism_desc):
    return f"""<p>کادر {mechanism_desc.split(' یا')[0]} درب {door_width} ترانک لگراند (کد {code}) به‌طور اختصاصی برای نصب روی ترانکینگ‌های لگراند با درب {door_width} میلی‌متر طراحی شده که شامل مدل‌های {trunking_examples} می‌شود. این محصول از دو بخش ساپورت (نگهدارنده داخل ترانک) و فیس‌پلیت (صفحه جلویی) تشکیل شده و امکان نصب {mechanism_desc} را روی ترانک یا مستقیم روی دیوار فراهم می‌کند.</p>
<p>بدنه آن از PVC سفید ساخته شده و ساخت کشور فرانسه است. این کادر به کاربر امکان می‌دهد طیف وسیعی از پریزها و مکانیزم‌های استاندارد لگراند را به شکلی منظم و یکپارچه در سیستم ترانکینگ خود جای دهد.</p>"""


def door_seal_content(code, door_width, trunking_examples):
    return f"""<p>درزگیر درب {door_width} ترانکینگ لگراند (کد {code}) به‌طور اختصاصی برای ترانکینگ‌های سری DLP لگراند با درب {door_width} میلی‌متر طراحی شده که شامل مدل‌های {trunking_examples} می‌شود. این نوار درزگیر روی لبه درب ترانک نصب می‌شود و اتصال محکم‌تر و آب‌بندی بهتری بین درب و بدنه ترانک ایجاد می‌کند.</p>
<p>از جنس PVC سفید‌رنگ ساخته شده و ساخت کشور فرانسه است.</p>"""


def flat_angle_content(code, width_label, trunking_example):
    return f"""<p>زاویه تخت ۹۰ درجه ترانکینگ عرض {width_label} لگراند (کد {code}) به‌طور اختصاصی برای استفاده در {trunking_example} طراحی شده و با ابعاد دقیق تولید می‌شود تا تغییر مسیر ۹۰ درجه‌ای مسیر کابل‌کشی روی سطح صاف به‌سادگی و با استحکام کافی انجام شود.</p>
<p>از جنس PVC سفید‌رنگ ساخته شده و ساخت کشور فرانسه است.</p>"""


def tee_junction_content(code, width_label, trunking_example):
    return f"""<p>سه‌راهی ترانکینگ {width_label} لگراند (کد {code}) {trunking_example} نقش مهمی در ایجاد انشعاب T شکل در مسیرهای کابل‌کشی ایفا می‌کند و یک اتصال محکم و مطمئن بین سه شاخه ترانک ایجاد می‌کند تا از جدا شدن ترانک‌ها در محل انشعاب جلوگیری شود.</p>
<p>از جنس PVC سفید‌رنگ ساخته شده و ساخت کشور فرانسه است. استفاده از آن علاوه بر ایجاد نظم و زیبایی در کابل‌کشی، به حفظ ایمنی سیستم و جلوگیری از آسیب‌دیدن کابل‌ها در محل انشعاب کمک می‌کند.</p>"""


def end_cap_content(code, width_label, trunking_example, extra=""):
    return f"""<p>ته‌بند ترانکینگ {width_label} لگراند (کد {code}) {trunking_example} با پوشاندن انتهای باز ترانک، از ورود گردوغبار، حشرات و اشیاء خارجی به داخل آن جلوگیری می‌کند و با پوشاندن لبه‌های تیز، خطر آسیب‌دیدگی کابل‌ها و افراد را کاهش می‌دهد و نمایی یکدست به مسیر کابل‌کشی می‌بخشد.{extra}</p>
<p>از جنس PVC سفید‌رنگ ساخته شده و ساخت کشور فرانسه است.</p>"""


def body_seal_content(code, method_label, method_desc):
    return f"""<p>درزگیر بدنه ترانکینگ لگراند مدل {method_label} (کد {code}) در شاخه‌های ۲ متری و از جنس PVC بدون سرب تولید می‌شود و محل اتصال دو شاخه ترانکینگ را می‌پوشاند تا مسیر کابل‌کشی نمایی یکدست و حرفه‌ای پیدا کند. {method_desc}</p>
<p>رنگ آن سفید است و ساخت کشور فرانسه است.</p>"""


def external_angle_content(code, width_label, trunking_example, extra=""):
    return f"""<p>زاویه خارجی ترانکینگ {width_label} لگراند (کد {code}) از جنس PVC بدون سرب تولید شده و به‌طور اختصاصی برای استفاده با {trunking_example} طراحی شده است. این قطعه در زوایای خارجی دیوارها و سطوح، مسیر کابل‌کشی ترانکینگ را به شکلی منظم و ایمن ادامه می‌دهد.{extra}</p>
<p>رنگ آن سفید است و ساخت کشور فرانسه است.</p>"""


def internal_angle_content(code, width_label, trunking_example, extra=""):
    return f"""<p>زاویه داخلی ترانکینگ {width_label} لگراند (کد {code}) از جنس PVC بدون سرب تولید شده و برای استفاده با {trunking_example} مناسب است. این زاویه داخلی محل اتصال دو ترانک را در گوشه‌های داخلی به‌طور کامل می‌پوشاند و نمایی یکدست و حرفه‌ای ایجاد می‌کند.{extra}</p>
<p>رنگ آن سفید است و ساخت کشور فرانسه است.</p>"""


RECORDS = [
    {  # 1 - kadre 6-module door65 010956
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب شش پریز یا مکانیزم روی ترانکینگ عرض ۸۰/۱۵۰ لگراند"},
        "content_html": kadre_content("010956", "۶۵ میلی‌متر", "ترانکینگ ۵۰ در ۸۰ و ۵۰ در ۱۵۰ لگراند", "شش ماژول باریک یا سه مکانیزم دو ماژولی"),
    },
    {  # 2 - kadre 4-module door65 010954
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب چهار پریز یا مکانیزم روی ترانکینگ عرض ۸۰/۱۵۰ لگراند"},
        "content_html": kadre_content("010954", "۶۵ میلی‌متر", "ترانکینگ ۵۰ در ۸۰ و ۵۰ در ۱۵۰ لگراند", "چهار ماژول باریک یا دو مکانیزم دو ماژولی"),
    },
    {  # 3 - kadre 2-module door65 010952
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب دو پریز یا یک مکانیزم روی ترانکینگ عرض ۸۰/۱۵۰ لگراند"},
        "content_html": kadre_content("010952", "۶۵ میلی‌متر", "ترانکینگ ۵۰ در ۸۰ و ۵۰ در ۱۵۰ لگراند", "دو ماژول باریک یا یک مکانیزم دو ماژولی"),
    },
    {  # 4 - door seal 85mm 010802
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "آب‌بندی و اتصال محکم‌تر درب ترانکینگ عرض ۸۵ به بدنه"},
        "content_html": door_seal_content("010802", "۸۵ میلی‌متر", "ترانکینگ‌های سری ۸۵ (مانند ۵۰ در ۱۰۵ و ۵۰ در ۱۹۵ لگراند)"),
    },
    {  # 5 - door seal 65mm 010801
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "آب‌بندی و اتصال محکم‌تر درب ترانکینگ عرض ۶۵ به بدنه"},
        "content_html": door_seal_content("010801", "۶۵ میلی‌متر", "ترانکینگ ۵۰ در ۸۰ و ۵۰ در ۱۰۵ لگراند"),
    },
    {  # 6 - flat angle width195 010792
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "تغییر مسیر ۹۰ درجه در ترانکینگ عرض ۱۹۵ روی سطح صاف"},
        "content_html": flat_angle_content("010792", "۱۹۵", "ترانکینگ ۱۹۵ در ۵۰ لگراند"),
    },
    {  # 7 - flat angle width150 010789
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "تغییر مسیر ۹۰ درجه در ترانکینگ عرض ۱۵۰ روی سطح صاف"},
        "content_html": flat_angle_content("010789", "۱۵۰", "ترانکینگ ۱۵۰ در ۵۰ لگراند"),
    },
    {  # 8 - flat angle width105 010785
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "تغییر مسیر ۹۰ درجه در ترانکینگ عرض ۱۰۵ روی سطح صاف"},
        "content_html": flat_angle_content("010785", "۱۰۵", "ترانکینگ ۱۰۵ در ۵۰ لگراند"),
    },
    {  # 9 - flat angle width80 010767
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "تغییر مسیر ۹۰ درجه در ترانکینگ عرض ۸۰ روی سطح صاف"},
        "content_html": flat_angle_content("010767", "۸۰", "ترانکینگ ۸۰ در ۵۰ لگراند"),
    },
    {  # 10 - tee junction width105 010736
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "ایجاد انشعاب T شکل در ترانکینگ عرض ۱۰۵"},
        "content_html": tee_junction_content("010736", "عرض ۱۰۵", "به‌طور اختصاصی برای استفاده با ترانکینگ ۱۰۵ در ۵۰ لگراند طراحی شده و"),
    },
    {  # 11 - tee junction width80 010735
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "ایجاد انشعاب T شکل در ترانکینگ عرض ۸۰"},
        "content_html": tee_junction_content("010735", "عرض ۸۰", "به‌طور اختصاصی برای استفاده با ترانکینگ ۸۰ در ۵۰ لگراند طراحی شده و"),
    },
    {  # 12 - tee junction universal 010732
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "ایجاد انشعاب T شکل در تمام عرض‌های ترانکینگ DLP لگراند"},
        "content_html": tee_junction_content("010732", "فری‌سایز", "که به‌طور خاص برای استفاده با تمامی عرض‌های ترانکینگ DLP لگراند طراحی شده و"),
    },
    {  # 13 - end cap width150 010703
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "پوشاندن انتهای باز ترانکینگ عرض ۱۵۰"},
        "content_html": end_cap_content("010703", "عرض ۱۵۰", "به‌طور اختصاصی برای استفاده با ترانکینگ ۱۵۰ در ۵۰ لگراند طراحی شده و"),
    },
    {  # 14 - end cap width80 010722
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "80x50 mm", "conductor_material": "",
                   "standard": "", "application": "پوشاندن انتهای باز ترانکینگ عرض ۸۰"},
        "content_html": end_cap_content("010722", "عرض ۸۰", "به‌طور اختصاصی برای استفاده با ترانکینگ ۸۰ در ۵۰ لگراند طراحی شده و", " ابعاد آن ۸۰ در ۵۰ میلی‌متر است."),
    },
    {  # 15 - end cap width105 010702
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "پوشاندن انتهای باز ترانکینگ عرض ۱۰۵"},
        "content_html": end_cap_content("010702", "عرض ۱۰۵", "برای استفاده با ترانکینگ ۱۰۵ در ۵۰ لگراند مناسب است و", " این محصول همراه با پیچ‌های نصب عرضه می‌شود."),
    },
    {  # 16 - body seal adhesive 010692
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "پوشاندن سریع و موقت درز اتصال دو شاخه ترانکینگ"},
        "content_html": body_seal_content("010692", "چسبی", "این مدل با چسب دوطرفه تعبیه‌شده روی آن، نصب بسیار سریعی دارد و برای پوشاندن سریع درزهای بین ترانک‌ها مناسب است."),
    },
    {  # 17 - body seal clip-in 010691
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "پوشاندن درز اتصال دو شاخه ترانکینگ به‌صورت قابل‌استفاده مجدد"},
        "content_html": body_seal_content("010691", "خاری", "این مدل به‌صورت خاری (فشاری) نصب می‌شود و برخلاف مدل چسبی، در صورت نیاز به جابه‌جایی، قابلیت استفاده مجدد دارد و خاصیت خود را از دست نمی‌دهد."),
    },
    {  # 18 - external angle width150-195 010635
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "عبور ترانکینگ از زاویه خارجی دیوار در عرض ۱۵۰ یا ۱۹۵"},
        "content_html": external_angle_content("010635", "عرض ۱۵۰ و ۱۹۵", "ترانکینگ ۱۵۰ در ۵۰ و ترانکینگ ۱۹۵ در ۵۰ لگراند"),
    },
    {  # 19 - external angle width80-105 010622
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "عبور ترانکینگ از زاویه خارجی دیوار در عرض ۸۰ یا ۱۰۵"},
        "content_html": external_angle_content("010622", "عرض ۸۰ و ۱۰۵", "ترانکینگ ۸۰ در ۵۰ و ترانکینگ ۱۰۵ در ۵۰ لگراند", " این محصول در رنگ‌های سفید، نقره‌ای و مشکی نیز قابل تهیه است."),
    },
    {  # 20 - internal angle width150-195 010606
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "عبور ترانکینگ از زاویه داخلی دیوار در عرض ۱۵۰ یا ۱۹۵"},
        "content_html": internal_angle_content("010606", "عرض ۱۵۰ و ۱۹۵", "ترانکینگ ۱۵۰ در ۵۰ و ترانکینگ ۱۹۵ در ۵۰ لگراند", " در بازه دمایی ۲۵- تا ۶۵+ درجه سانتی‌گراد کاربرد خود را حفظ می‌کند."),
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
    with open(os.path.join(DATA_DIR, "batch40_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch40_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch40_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
