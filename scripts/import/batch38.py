# -*- coding: utf-8 -*-
"""Batch 38: 20 products -- 3 Legrand LCS2 patch panels (Cat6A SFTP,
Cat6 SFTP, Cat6 UTP), 13 Legrand SFTP/UTP patch cords of varying
lengths, and 4 Legrand bulk network cable reels (Cat6A FTP LSZH,
Cat6 SFTP PVC, Cat6 FTP PVC, Cat6 FTP LSZH)."""
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

NETWORK_PARENT = "تجهیزات شبکه"


def patch_panel_content(code, category, structure_fa, speed, bandwidth):
    return f"""<p>پچ پنل ۲۴ پورت لگراند {category} {structure_fa} (کد {code}) بدنه‌ای از ورق فولادی گالوانیزه DC01 دارد که مقاومت بالایی در برابر ضربه و خوردگی از خود نشان می‌دهد و بلوک‌ها و کانکتورهای آن از پلی‌کربنات مقاوم در برابر حرارت و ضربه ساخته شده‌اند. جعبه محصول به‌صورت لودد (Loaded) عرضه می‌شود و شامل یک ریل پچ‌پنلی، ۲۴ عدد کیستون فلزی، جایگاه برچسب همراه با ۶ مجموعه برچسب رنگی شماره‌دار (۱ تا ۲۴) و دفترچه راهنما است.</p>
<p>این پچ پنل با ساختار {structure_fa}، سرعت انتقال داده {speed} و پهنای باند {bandwidth} را پشتیبانی می‌کند و برای نصب در رک استاندارد ۱۹ اینچ طراحی شده است. کانکتورهای RJ45 آن بدون نیاز به ابزار خاص (Tool-Free) از جلوی پنل نصب می‌شوند و در پشت آن یک نظم‌دهنده کابل برای مدیریت بهتر سیم‌کشی تعبیه شده است. در بازه دمایی ۴۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند. برای بهترین عملکرد شبکه، توصیه می‌شود کابل شبکه و کیستون هم‌خانواده با ساختار {structure_fa} به کار رود.</p>"""


def patch_cord_content(code, category, structure_fa, structure_short, length_fa, color, speed, bandwidth, detail=""):
    return f"""<p>پچ‌کورد {length_fa} {category} {structure_fa} لگراند (کد {code}) با ساختار {structure_short} از زوج‌های مسی افشان تولید شده که انعطاف‌پذیری بالایی به کابل می‌بخشد و نصب و جابجایی آن را در فضاهای مختلف تسهیل می‌کند. روکش PVC رنگ {color} آن، ضمن محافظت فیزیکی، شناسایی و سازماندهی کابل را در میان سایر اتصالات شبکه آسان می‌سازد.{detail}</p>
<p>این پچ‌کورد با سرعت انتقال داده {speed} و پهنای باند {bandwidth}، مطابق استانداردهای ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156 و IEC 60603-7 تولید شده و از قابلیت PoE تا ۹۰ وات (مطابق IEEE 802.3af/at/bt) پشتیبانی می‌کند. قطر خارجی آن ۶.۲±۰.۲ میلی‌متر، حداقل شعاع خمش آن ۲۴ میلی‌متر و استحکام کششی آن حداقل ۵۰ نیوتن است و در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def network_cable_content(code, category, structure_fa, jacket, speed, bandwidth, temp_max, extra=""):
    return f"""<p>کابل شبکه {category} {structure_fa} لگراند با روکش {jacket} (کد {code}) از چهار زوج سیم مسی به‌هم‌تابیده تشکیل شده که هر رشته با عایق پلی‌اتیلن پوشانده شده است.{extra} این کابل با سرعت انتقال داده {speed} و پهنای باند {bandwidth} برای زیرساخت‌های شبکه محلی، دیتاسنتر و پروژه‌های بزرگ کابل‌کشی ساختاریافته مناسب است و به‌صورت قرقره ۵۰۰ متری عرضه می‌شود.</p>
<p>در بازه دمایی ۲۰- تا {temp_max}+ درجه سانتی‌گراد کار می‌کند. توصیه می‌شود کیستون و پچ پنل هم‌خانواده با ساختار {structure_fa} استفاده شود تا یکپارچگی الکتریکی حفظ و از افت کیفیت سیگنال جلوگیری شود.</p>"""


RECORDS = [
    {  # 1 - patch panel Cat6A SFTP 033573
        "category_name": "پچ پنل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "نصب در رک شبکه ۱۹ اینچ برای پایانه‌سازی ۲۴ کابل Cat6A SFTP"},
        "content_html": patch_panel_content("033573", "Cat6A", "SFTP", "۱۰ گیگابیت بر ثانیه", "۵۰۰ مگاهرتز"),
    },
    {  # 2 - patch panel Cat6 SFTP 033563
        "category_name": "پچ پنل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "نصب در رک شبکه ۱۹ اینچ برای پایانه‌سازی ۲۴ کابل Cat6 SFTP"},
        "content_html": patch_panel_content("033563", "Cat6", "SFTP", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 3 - patch panel Cat6 UTP 033561
        "category_name": "پچ پنل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "", "application": "نصب در رک شبکه ۱۹ اینچ برای پایانه‌سازی ۲۴ کابل Cat6 UTP"},
        "content_html": patch_panel_content("033561", "Cat6", "UTP", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 4 - patch cord Cat6A SFTP 5m 051783
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال کور سوییچ‌ها و سرورهای پرسرعت"},
        "content_html": patch_cord_content("051783", "Cat6A", "SFTP", "شیلد و فویل", "پنج‌متری", "زرد", "۱۰ گیگابیت بر ثانیه", "۵۰۰ مگاهرتز",
                                            " این پچ‌کورد به‌ویژه برای اتصال به کور سوییچ‌ها و سرورهای پرترافیک در دیتاسنتر کاربرد دارد."),
    },
    {  # 5 - patch cord Cat6A SFTP 3m 051782
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال تجهیزات در رک شبکه و دیتاسنتر"},
        "content_html": patch_cord_content("051782", "Cat6A", "SFTP", "شیلد و فویل", "سه‌متری", "زرد", "۱۰ گیگابیت بر ثانیه", "۵۰۰ مگاهرتز"),
    },
    {  # 6 - patch cord Cat6A SFTP 2m 051781
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال تجهیزات نزدیک به هم در رک شبکه"},
        "content_html": patch_cord_content("051781", "Cat6A", "SFTP", "شیلد و فویل", "دومتری", "زرد", "۱۰ گیگابیت بر ثانیه", "۵۰۰ مگاهرتز"),
    },
    {  # 7 - patch cord Cat6A SFTP 1m 051780
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال کوتاه بین پچ پنل و سوییچ در رک شبکه"},
        "content_html": patch_cord_content("051780", "Cat6A", "SFTP", "شیلد و فویل", "یک‌متری", "زرد", "۱۰ گیگابیت بر ثانیه", "۵۰۰ مگاهرتز",
                                            " این پچ‌کورد یک متری از سریع‌ترین پچ‌کوردهای شبکه مسی است و برای اتصالات کوتاه داخل رک، مانند بین پچ پنل و سوییچ، مناسب است."),
    },
    {  # 8 - patch cord Cat6 SFTP 5m 051755
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال تجهیزات با فاصله بیشتر در رک یا اتاق سرور"},
        "content_html": patch_cord_content("051755", "Cat6", "SFTP", "شیلد و فویل", "پنج‌متری", "آبی", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز",
                                            " طول ایده‌آل کابل‌کشی مسی ۹۰ متر است و با استفاده از دو پچ‌کورد پنج‌متری در دو سر کابل اصلی می‌توان به متراژ استاندارد ۱۰۰ متر رسید."),
    },
    {  # 9 - patch cord Cat6 SFTP 3m 051754
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال سوییچ به پچ پنل یا مودم به دستگاه‌های LAN"},
        "content_html": patch_cord_content("051754", "Cat6", "SFTP", "شیلد و فویل", "سه‌متری", "آبی", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 10 - patch cord Cat6 SFTP 2m 051753
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال سوییچ به پچ پنل یا مودم به دستگاه‌های LAN"},
        "content_html": patch_cord_content("051753", "Cat6", "SFTP", "شیلد و فویل", "دومتری", "آبی", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 11 - patch cord Cat6 SFTP 1m 051752
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال کوتاه بین تجهیزات شبکه داخل رک"},
        "content_html": patch_cord_content("051752", "Cat6", "SFTP", "شیلد و فویل", "یک‌متری", "آبی", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز",
                                            " دو سر آن به کانکتورهای فلزی RJ45 مجهز است که اتصالی مطمئن و پایدار با تجهیزات شبکه برقرار می‌کند."),
    },
    {  # 12 - patch cord Cat6 UTP 5m 051775
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال کامپیوتر، سرور، روتر و سوییچ در محیط‌های کم‌نویز"},
        "content_html": patch_cord_content("051775", "Cat6", "UTP", "بدون شیلد", "پنج‌متری", "آبی", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز",
                                            " ساختار UTP بدون شیلد آن، گزینه‌ای اقتصادی برای محیط‌هایی با تداخل الکترومغناطیسی کم به شمار می‌رود."),
    },
    {  # 13 - patch cord Cat6 UTP 3m 051774
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال کامپیوتر، روتر، مودم و سوییچ در محیط‌های کم‌نویز"},
        "content_html": patch_cord_content("051774", "Cat6", "UTP", "بدون شیلد", "سه‌متری", "آبی", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 14 - patch cord Cat6 UTP 2m 051773
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال مودم، روتر، سوییچ و پچ پنل در محیط‌های کم‌نویز"},
        "content_html": patch_cord_content("051773", "Cat6", "UTP", "بدون شیلد", "دومتری", "آبی", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 15 - patch cord Cat6 UTP 1m 051772
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568، ISO/IEC 11801، EN 50173، IEC 61156، IEC 60603-7", "application": "اتصال کوتاه بین پچ پنل و سوییچ در رک شبکه"},
        "content_html": patch_cord_content("051772", "Cat6", "UTP", "بدون شیلد", "یک‌متری", "آبی", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز"),
    },
    {  # 16 - patch cord Cat6 UTP 0.5m 051818
        "category_name": "پچ کورد", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "مس",
                   "standard": "IEC 60332-1، IEC 61034-2، IEC 60754-2", "application": "اتصال بسیار کوتاه بین پچ پنل و سوییچ داخل رک"},
        "content_html": patch_cord_content("051818", "Cat6", "UTP", "بدون شیلد", "نیم‌متری", "آبی", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز",
                                            " کاورهای محافظ (Snagless Boot) دو سر کابل، از شکستن قفل کانکتور جلوگیری کرده و طول عمر آن را افزایش می‌دهند؛ این پچ‌کورد نیم‌متری از پرکاربردترین اندازه‌ها برای رک‌های فشرده است و طبق مشخصات فنی دوام آن تا ۲۵۰۰ بار نصب و جدا شدن است."),
    },
    {  # 17 - network cable Cat6A FTP LSZH 032778
        "category_name": "کابل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "AWG 23", "conductor_material": "مس",
                   "standard": "", "application": "کابل‌کشی Backbone و زیرساخت شبکه دیتاسنتر و شرکت‌های بزرگ"},
        "content_html": network_cable_content("032778", "Cat6A", "FTP", "LSZH", "۱۰ گیگابیت بر ثانیه", "۵۰۰ مگاهرتز", "60",
                                                " یک فویل دور تمام چهار زوج سیم پیچیده شده که تداخل و نویز الکترومغناطیسی را کاهش می‌دهد و قطر کلی کابل ۷.۳ میلی‌متر است. روکش LSZH آن در صورت آتش‌سوزی دود سمی متصاعد نمی‌کند."),
    },
    {  # 18 - network cable Cat6 SFTP PVC 032759
        "category_name": "کابل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "AWG 24", "conductor_material": "مس",
                   "standard": "ANSI/TIA 568.2-D، ISO/IEC 11801", "application": "شبکه‌های محلی (LAN) پرسرعت و محیط‌های صنعتی حساس به نویز"},
        "content_html": network_cable_content("032759", "Cat6", "SFTP", "PVC", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز", "60",
                                                " هر چهار زوج سیم علاوه بر شیلد کلی، دارای فویل جداگانه هستند که سطح بالایی از محافظت در برابر نویز فراهم می‌کند."),
    },
    {  # 19 - network cable Cat6 FTP PVC 032758
        "category_name": "کابل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "AWG 23", "conductor_material": "مس",
                   "standard": "", "application": "شبکه‌های محلی، دوربین مداربسته و دیتاسنتر در محیط با نویز بالا"},
        "content_html": network_cable_content("032758", "Cat6", "FTP", "PVC", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز", "60",
                                                " یک لایه فویل آلومینیوم/پلی‌استر دور هر چهار زوج سیم پیچیده شده که در برابر تداخلات الکترومغناطیسی محافظت می‌کند."),
    },
    {  # 20 - network cable Cat6 FTP LSZH 032756
        "category_name": "کابل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "AWG 23", "conductor_material": "مس",
                   "standard": "IEC 61156-5، IEEE 802.3bt", "application": "کابل‌کشی ساختمانی با الزامات ایمنی حریق بالا"},
        "content_html": network_cable_content("032756", "Cat6", "FTP", "LSZH", "۱ گیگابیت بر ثانیه", "۲۵۰ مگاهرتز", "75",
                                                " یک لایه فویل آلومینیوم/پلی‌استر دور هر چهار زوج سیم پیچیده شده و قطر متوسط کابل حدود ۷.۲ میلی‌متر با وزن حدود ۴۷ کیلوگرم در هر کیلومتر است. روکش LSZH آن مطابق EN 50399 و IEC 60332-1-2 در برابر آتش مقاوم است و دود سمی تولید نمی‌کند و از قابلیت PoE++ نیز پشتیبانی می‌کند."),
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
    with open(os.path.join(DATA_DIR, "batch38_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch38_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch38_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
