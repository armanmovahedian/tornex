# -*- coding: utf-8 -*-
"""Batch 42 (FINAL): 25 products -- completes the 790-product import.
2 Legrand colored power sockets (red/white), 1 blank filler, 4
Legrand mosaic switches (cross, 2-way wide/narrow, single-pole), 1
doorbell buzzer, 1 Plexo claw mount, 7 Legrand Plexo IP55 waterproof
switches/sockets, 2 Plexo recessed frames, 1 Plexo glass door
adaptor, 2 Plexo switch mechanisms, 1 Leoni Cat6 UTP network cable,
2 Legrand network cable reels (Cat6A SFTP LSZH, Cat6 UTP PVC), and 1
Khorasan Afsharnejad flexible wire (300 mm2)."""
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


def colored_power_socket_content(code, color_label, extra=""):
    return f"""<p>پریز برق ارتدار {color_label} دو ماژول موزائیک لگراند (کد {code}) ابعاد استاندارد ۴۵×۴۵ میلی‌متر دارد و در تمامی کادرها و مکانیزم‌های سری موزائیک قابل نصب است. بدنه آن از پلی‌کربنات (PC) مقاوم در برابر حرارت و اشعه UV و هالوژن‌فری ساخته شده، یعنی در آتش‌سوزی دود سمی تولید نمی‌کند.{extra}</p>
<p>ترمینال‌های پیچی آن امکان اتصال سیم تا ۴ میلی‌متر مربع را با طول سیم‌لختی ۱۰ میلی‌متر فراهم می‌کند. جریان نامی آن ۱۶ آمپر و ولتاژ نامی ۲۵۰ ولت است و درجه حفاظت آن IP20 و مقاومت ضربه آن IK04 است.</p>"""


def blank_content(code):
    return f"""<p>بلنک تک ماژول سفید موزائیک لگراند (کد {code}) برای پوشاندن فضای خالی یک ماژول در کادرهای موزائیک به کار می‌رود و با ابعاد ۴۵×۲۲.۵ میلی‌متر، بدون نیاز به پیچ یا ابزار، با گیره‌های کلیپسی در جای خود قرار می‌گیرد.</p>
<p>از ABS سفید با کد رنگی RAL 9003 و مقاوم در برابر اشعه UV ساخته شده و درجه حفاظت آن IP41 و مقاومت ضربه آن IK04 (تا ۰.۵ ژول) است و خاصیت خوداطفایی تا دمای ۶۵۰ درجه سانتی‌گراد به مدت ۳۰ ثانیه دارد.</p>"""


def switch_content(code, switch_type, dims, module_desc, extra_use=""):
    return f"""<p>{switch_type} موزائیک لگراند (کد {code}) با ابعاد {dims} میلی‌متر در تمامی کادرها و مکانیزم‌های سری موزائیک قابل نصب است. بدنه آن از پلی‌کربنات (PC) مقاوم در برابر حرارت و اشعه UV ساخته شده و ترمینال‌های اتوماتیک آن با سیم لخت استاندارد ۱۲ میلی‌متری، نصب سریع و ایمن را فراهم می‌کند.{extra_use}</p>
<p>از جریان {module_desc} پشتیبانی می‌کند و قابلیت نصب چراغ نشانگر (Easy-LED) نیز دارد. درجه حفاظت آن IP31D و مقاومت ضربه آن IK04 است و در بازه دمایی ۵- تا ۳۵+ درجه سانتی‌گراد کار می‌کند.</p>"""


def buzzer_content(code):
    return f"""<p>زنگ اخبار (بیزر) دو ماژول سفید موزائیک لگراند (کد {code}) با قابلیت اتصال به ولتاژ ۸ یا ۲۳۰ ولت، هشدار صوتی با شدت ۶۵ دسی‌بل در فاصله یک متری تولید می‌کند و برای نصب توکار یا روکار در دیوارهای نازک مناسب است. معمولاً همراه با شاسی زنگ موزائیک لگراند استفاده می‌شود.</p>
<p>درجه حفاظت آن IP41 (مقاومت در برابر اجسام جامد بزرگ‌تر از ۱ میلی‌متر و قطرات آب) و مقاومت ضربه آن IK05 (تا ۰.۷ ژول) است. در بازه دمایی ۱۰- تا ۵۵+ درجه سانتی‌گراد کار می‌کند.</p>"""


def plexo_claw_content(code, color):
    return f"""<p>چنگکی مخصوص کلید و پریز {color} ضد آب پلکسو لگراند (کد {code}) برای نصب کلید و پریزهای سری پلکسو در مکان‌هایی طراحی شده که استفاده از پیچ ممکن نیست، مانند دیوارهای گچی یا سطوح بدون قوطی پیچی. با استفاده از دو محل ویژه در سمت چپ و راست کلید یا پریز، آن را به‌صورت کامل و ایمن در جای خود نگه می‌دارد.</p>
<p>نوع نصب آن توکار است و از مواد مقاوم در برابر شرایط سخت محیطی ساخته شده است. درجه حفاظت نهایی مجموعه به نوع کلید یا پریز نصب‌شده وابسته است.</p>"""


def plexo_socket_content(code, color, mount_label, extra=""):
    return f"""<p>پریز برق ارتدار {mount_label} {color} ضد آب پلکسو لگراند (کد {code}) با استاندارد IP55 از پلی‌پروپیلن و ABS مقاوم در برابر مواد شیمیایی ساخته شده و در برابر پاشش آب از هر جهت و گردوغبار محافظت می‌کند. ولتاژ نامی آن ۲۲۰ تا ۲۵۰ ولت و جریان نامی آن ۱۶ آمپر است.{extra}</p>
<p>واشربندی دقیق آن مانع نفوذ رطوبت به داخل پریز می‌شود و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند. در صورت نبود جای پیچ روی دیوار، می‌توان از چنگکی مخصوص پلکسو برای نصب استفاده کرد.</p>"""


def plexo_switch_content(code, pole_label, color, mount_label, dims_note=""):
    return f"""<p>{pole_label} {mount_label} {color} ضد آب پلکسو لگراند (کد {code}) با استاندارد IP55 در برابر پاشش آب از هر جهت و نفوذ گردوغبار محافظت می‌کند و برای نصب در فضاهای مرطوب مانند حمام، استخر، موتورخانه و محیط‌های صنعتی مناسب است. ولتاژ نامی آن ۲۲۰ تا ۲۵۰ ولت و جریان نامی آن ۱۰ آمپر است.{dims_note}</p>
<p>بدنه آن از پلی‌کربنات و ABS با مقاومت بالا در برابر مواد شیمیایی و اشعه UV ساخته شده و خاصیت خودخاموش‌شوندگی دارد. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند. در صورت نبود جای پیچ روی دیوار، می‌توان از چنگکی مخصوص پلکسو برای نصب استفاده کرد.</p>"""


def plexo_frame_content(code, color):
    return f"""<p>کادر توکار {color} ضد آب پلکسو لگراند (کد {code}) با استاندارد IP55 روی قوطی‌های استاندارد نصب می‌شود و می‌تواند با انواع مغزی کلید و پریز پلکسو و درب‌های شیشه‌ای ضدآب پلکسو ترکیب شده و یک کلید یا پریز توکار کامل ضدآب را تشکیل دهد. طراحی ماژولار آن امکان تعویض تنها بخش آسیب‌دیده را فراهم می‌کند.</p>
<p>از پلی‌پروپیلن تقویت‌شده مقاوم در برابر ضربه، خوردگی و مواد شیمیایی ساخته شده و در صورت نبود جای پیچ روی دیوار، می‌توان از چنگکی مخصوص پلکسو (کد 084900) استفاده کرد. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def plexo_glass_door_content(code):
    return f"""<p>درب شیشه‌ای تبدیل موزائیک به ضد آب پلکسو لگراند (کد {code}) امکان تبدیل مکانیزم‌های موزائیک مانند پریز شبکه، پریز تلفن و شاسی زنگ را به یک مجموعه ضدآب با استاندارد IP55 فراهم می‌کند و روی کادر توکار یا باکس روکار پلکسو نصب می‌شود.</p>
<p>از پلی‌کربنات شفاف ساخته شده که امکان مشاهده وضعیت مکانیزم داخلی را می‌دهد. نصب آن ساده و بدون نیاز به ابزار خاص است و در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def plexo_mechanism_content(code, pole_label):
    return f"""<p>مغزی {pole_label} طوسی ضد آب پلکسو لگراند (کد {code}) با کادر توکار یا باکس روکار سری پلکسو ترکیب می‌شود و یک کلید کامل توکار یا روکار را تشکیل می‌دهد. ولتاژ نامی آن ۲۲۰ تا ۲۵۰ ولت و جریان نامی آن ۱۰ آمپر است.</p>
<p>عایق‌های لاستیکی و سیلیکونی آن مانع نفوذ رطوبت به داخل مکانیزم می‌شود و درجه حفاظت مجموعه نهایی IP55 است. در بازه دمایی ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def leoni_cable_content():
    return """<p>کابل شبکه لئونی Cat6 UTP با روکش LSZH مطابق با استانداردهای ایمنی RoHS و REACh تولید شده و فاقد مواد خطرناک است. روکش هالوژن‌فری آن در صورت آتش‌سوزی بدون تولید دود سمی می‌سوزد و مطابق استانداردهای مقاومت در برابر شعله IEC 60332-1-2، تراکم دود پایین IEC 61034-1/2 و میزان کم اسید حاصل از سوختن EN 60754-2 تولید شده است.</p>
<p>از چهار زوج سیم مسی با عایق پلی‌اتیلن تشکیل شده و با سرعت انتقال داده ۱ گیگابیت بر ثانیه و پهنای باند ۲۵۰ مگاهرتز، برای شبکه‌های محلی و صنعتی مناسب است. ولتاژ کاری آن ۱۲۵ ولت و ولتاژ تست آن ۱۰۰۰ ولت است و در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند و به‌صورت قرقره ۳۰۵ متری زرد رنگ عرضه می‌شود.</p>"""


def legrand_cable_sftp_lszh_content(code):
    return f"""<p>کابل شبکه Cat6A S/FTP لگراند با روکش LSZH (کد {code}) برای شبکه‌های محلی پرسرعت و حساس به نویز در دفاتر، ادارات و محیط‌های صنعتی طراحی شده است. هر زوج سیم با یک لایه فویل و کل کابل نیز با یک بافت مسی محافظت می‌شود که تداخلات فرکانس رادیویی (RFI) و الکترومغناطیسی (EMI) را به‌طور مؤثر کاهش می‌دهد. استاندارد هادی آن AWG 23 است.</p>
<p>روکش LSZH آن در آتش‌سوزی دود کمتری تولید می‌کند و هالوژن آزاد نمی‌کند. با سرعت انتقال داده ۱۰ گیگابیت بر ثانیه و پهنای باند ۵۰۰ مگاهرتز تا فاصله ۱۰۰ متر، به‌صورت قرقره ۵۰۰ متری زرد رنگ عرضه می‌شود و در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def legrand_cable_utp_pvc_content(code):
    return f"""<p>کابل شبکه Cat6 UTP لگراند با روکش PVC آبی‌رنگ (کد {code}) از چهار زوج سیم مسی با عایق پلی‌اتیلن تشکیل شده و برای شبکه‌های محلی (LAN) بدون نویز و پارازیت زیاد مناسب است. قطر کلی آن ۵.۸ میلی‌متر و استاندارد هادی آن AWG 24 است.</p>
<p>با سرعت انتقال داده ۱ گیگابیت بر ثانیه و پهنای باند ۲۵۰ مگاهرتز، برای شبکه‌های اداری، تجاری و خانگی مناسب است. وزن آن حدود ۱۳ کیلوگرم در هر کیلومتر است و به‌صورت قرقره ۳۰۵ متری عرضه می‌شود. در بازه دمایی ۲۰- تا ۶۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def afshan_wire_content(size, conductor_desc, od, resistance, voltage, test_voltage, application, standard_extra="", weight=""):
    return f"""<p>سیم برق افشان {size} خراسان افشارنژاد با هادی مسی افشان (کلاس ۵) {conductor_desc} قطر کلی آن {od} میلی‌متر است. عایق آن از جنس PVC است که با فرآیند اکستروژن روی هادی مسی اعمال می‌شود و مطابق استانداردهای IEC 60227، ISIRI 607، IEC 60228{standard_extra} تولید می‌شود. در بازه دمایی ۳۰- تا ۷۰+ درجه سانتی‌گراد کار می‌کند و خاصیت عدم انتشار شعله دارد.</p>
<p>با ولتاژ نامی {voltage} و تست ولتاژ {test_voltage}، مقاومت هادی آن {resistance} در دمای ۲۰ درجه سانتی‌گراد است و دمای اتصال کوتاه آن ۱۶۰+ درجه سانتی‌گراد است.{weight} این سیم برای {application} کاربرد دارد.</p>"""


RECORDS = [
    {  # 1 - red power socket 077214
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP20، IEC 60695-2-11", "application": "اتصال دستگاه‌های حساس مانند UPS با قفل ایمنی اختصاصی"},
        "content_html": colored_power_socket_content("077214", "قرمز",
                                                        " این پریز به سیستم قفل ایمنی مجهز است که تنها دوشاخه‌های دارای ضامن مخصوص را می‌پذیرد و برای اتصال تجهیزات حساس مانند UPS طراحی شده تا از تخلیه ناخواسته باتری جلوگیری کند."),
    },
    {  # 2 - white power socket 278213L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP20، IEC 60695-2-11", "application": "پریز برق عمومی در فضای اداری، مسکونی و تجاری"},
        "content_html": colored_power_socket_content("278213L", "سفید"),
    },
    {  # 3 - blank 077070
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP41، IEC 60695-2-11", "application": "پوشاندن ماژول خالی در کادر موزائیک"},
        "content_html": blank_content("077070"),
    },
    {  # 4 - cross switch 077021L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP31D، IEC 60695-2-11", "application": "کنترل روشنایی از چندین نقطه مختلف"},
        "content_html": switch_content("077021L", "کلید صلیبی (کراکس) دو ماژول", "۴۵×۴۵", "۱۰ آمپر با ولتاژ ۲۵۰ ولت",
                                        " این کلید برای کنترل روشنایی از چندین نقطه مختلف به کار می‌رود."),
    },
    {  # 5 - two-way switch wide 278011L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP31D، IEC 60695-2-11", "application": "کنترل روشنایی راه‌پله و راهرو از دو نقطه"},
        "content_html": switch_content("278011L", "کلید تبدیل تک‌پل پهن دو ماژول", "۴۵×۴۵", "۱۰ آمپر با ولتاژ ۲۵۰ ولت",
                                        " مدل باریک آن با کد 077001L نیز عرضه می‌شود و این دو مدل معمولاً به‌صورت جفت به‌عنوان کلید دو پل تبدیل (راه‌پله) به کار می‌روند."),
    },
    {  # 6 - single pole switch wide 077010L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP31D، IEC 60695-2-11", "application": "روشن و خاموش کردن یک مدار روشنایی از یک نقطه"},
        "content_html": switch_content("077010L", "کلید تک‌پل پهن دو ماژول", "۴۵×۴۵", "۱۰ آمپر با ولتاژ ۲۵۰ ولت"),
    },
    {  # 7 - two-way switch narrow 077001L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP31D، IEC 60695-2-11", "application": "کنترل روشنایی راه‌پله و راهرو از دو نقطه در فضای کم"},
        "content_html": switch_content("077001L", "کلید تبدیل تک‌پل باریک یک ماژول", "۴۵×۲۲.۵", "۱۰ آمپر با ولتاژ ۲۵۰ ولت",
                                        " مدل پهن آن با کد 278011L نیز عرضه می‌شود و این دو مدل معمولاً به‌صورت جفت به‌عنوان کلید دو پل تبدیل (راه‌پله) به کار می‌روند."),
    },
    {  # 8 - buzzer 076641
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK05، IP41، EN 60669-1، NF C 61730، IEC 60695-2-11", "application": "هشدار صوتی ورودی همراه با شاسی زنگ موزائیک"},
        "content_html": buzzer_content("076641"),
    },
    {  # 9 - Plexo claw mount 084900
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "نصب کلید و پریز پلکسو روی سطوح بدون قوطی پیچی"},
        "content_html": plexo_claw_content("084900", "مشکی"),
    },
    {  # 10 - Plexo socket white recessed 069869
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، IEC 60884-1", "application": "پریز برق ضدآب توکار در فضای مرطوب یا صنعتی"},
        "content_html": plexo_socket_content("069869", "سفید", "توکار"),
    },
    {  # 11 - Plexo 2-pole switch white recessed 069855
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، NF EN 60669-1، NBN EN 60669-1، CEI 60669-1", "application": "کنترل همزمان دو مدار روشنایی در فضای مرطوب"},
        "content_html": plexo_switch_content("069855", "کلید دو پل", "سفید", "توکار",
                                              " امکان اتصال سیم‌های ۱.۵ تا ۲.۵ میلی‌متر مربع را دارد و با اتصال به دو مدار مجزا، کنترل همزمان دو منبع روشنایی را ممکن می‌کند."),
    },
    {  # 12 - Plexo 1-pole switch white recessed 069851
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، NF EN 60669-1، NBN EN 60669-1، CEI 60669-1", "application": "روشن و خاموش کردن مدار روشنایی در فضای مرطوب یا صنعتی"},
        "content_html": plexo_switch_content("069851", "کلید تک پل", "سفید", "توکار"),
    },
    {  # 13 - Plexo 1-pole switch grey recessed 069811
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، NF EN 60669-1، NBN EN 60669-1، CEI 60669-1", "application": "روشن و خاموش کردن مدار روشنایی در فضای مرطوب یا صنعتی"},
        "content_html": plexo_switch_content("069811", "کلید تک پل", "طوسی", "توکار",
                                              " اتصال با پیچ‌های چرخشی ۱/۴ انجام می‌شود و امکان اتصال سیم تک و دوگانه با ظرفیت ۲.۵ میلی‌متر مربع را دارد."),
    },
    {  # 14 - Plexo socket grey surface 069733
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، IEC 60884-1", "application": "پریز برق ضدآب روکار در فضای مرطوب یا صنعتی"},
        "content_html": plexo_socket_content("069733", "طوسی", "روکار",
                                              " این پریز به سیستم محافظ کودک مجهز است و طراحی ماژولار آن امکان تعویض بخش آسیب‌دیده بدون تعویض کل مجموعه را فراهم می‌کند."),
    },
    {  # 15 - Plexo 2-pole switch grey surface 069715
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، NF EN 60669-1، NBN EN 60669-1، CEI 60669-1", "application": "کنترل همزمان دو مدار روشنایی در فضای مرطوب"},
        "content_html": plexo_switch_content("069715", "کلید دو پل", "طوسی", "روکار"),
    },
    {  # 16 - Plexo 1-pole switch grey surface 069711
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، NF EN 60669-1، NBN EN 60669-1، CEI 60669-1", "application": "روشن و خاموش کردن مدار روشنایی در فضای مرطوب یا صنعتی"},
        "content_html": plexo_switch_content("069711", "کلید تک پل", "طوسی", "روکار",
                                              " در قسمت بالا و پایین آن محل‌های لاستیکی برای ورود لوله تعبیه شده تا نیازی به سوراخ‌کاری غیراستاندارد نباشد."),
    },
    {  # 17 - Plexo frame white 069692
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NF C 61-314، IEC 60884-1", "application": "پایه نصب توکار کلید یا پریز پلکسو ضدآب"},
        "content_html": plexo_frame_content("069692", "سفید"),
    },
    {  # 18 - Plexo frame grey 069681
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "NF C 61-314، IEC 60884-1", "application": "پایه نصب توکار کلید یا پریز پلکسو ضدآب"},
        "content_html": plexo_frame_content("069681", "طوسی"),
    },
    {  # 19 - Plexo glass door adaptor 069580
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "EN 54-3", "application": "تبدیل مکانیزم موزائیک به مجموعه ضدآب پلکسو"},
        "content_html": plexo_glass_door_content("069580"),
    },
    {  # 20 - Plexo mechanism 2-pole 069525
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، NF EN 60669-1، NBN EN 60669-1، CEI 60669-1", "application": "مغزی کلید دو پل برای تشکیل کلید کامل توکار یا روکار پلکسو"},
        "content_html": plexo_mechanism_content("069525", "کلید دو پل"),
    },
    {  # 21 - Plexo mechanism 1-pole 069511
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "CEI 60695-2-11، NF EN 60669-1، NBN EN 60669-1، CEI 60669-1", "application": "مغزی کلید تک پل برای تشکیل کلید کامل توکار یا روکار پلکسو"},
        "content_html": plexo_mechanism_content("069511", "کلید تک پل"),
    },
    {  # 22 - Leoni Cat6 UTP cable
        "category_name": "کابل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لئونی", "size_diameter": "", "conductor_material": "مس",
                   "standard": "EN 50575، EN 50399، IEC 60754-1/2، IEC 60754-2، IEC 61034-1/2", "application": "کابل‌کشی شبکه محلی و صنعتی با الزامات ایمنی حریق"},
        "content_html": leoni_cable_content(),
    },
    {  # 23 - Legrand Cat6A SFTP LSZH 032777
        "category_name": "کابل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "AWG 23", "conductor_material": "مس",
                   "standard": "", "application": "کابل‌کشی شبکه محلی پرسرعت با الزامات ایمنی حریق بالا"},
        "content_html": legrand_cable_sftp_lszh_content("032777"),
    },
    {  # 24 - Legrand Cat6 UTP PVC 032755
        "category_name": "کابل شبکه", "category_parent_name": NETWORK_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "AWG 24", "conductor_material": "مس",
                   "standard": "", "application": "کابل‌کشی شبکه محلی در محیط بدون نویز الکترومغناطیسی"},
        "content_html": legrand_cable_utp_pvc_content("032755"),
    },
    {  # 25 - afshan wire 300mm2
        "category_name": "سیم افشان", "category_parent_name": KHORASAN_PARENT,
        "specs": {"brand": "افشارنژاد", "size_diameter": "300", "conductor_material": "مس",
                   "standard": "IEC 60227، ISIRI 607، DIN VDE 0295، IEC 60228", "application": "تغذیه مدارهای صنعتی سنگین با جریان بالا و اتصال ژنراتور به تابلوهای برق"},
        "content_html": afshan_wire_content("۱×۳۰۰", "از رشته‌های مسی آنیل‌شده تشکیل شده است و", "28.2",
                                             "۰.۰۶۴۱ اهم بر کیلومتر", "۴۵۰/۷۵۰ ولت", "۲.۵ کیلوولت",
                                             "تغذیه مدارهای صنعتی سنگین با جریان بالا و اتصال ژنراتور به تابلوهای برق",
                                             " و DIN VDE 0295", " وزن آن حدود ۲.۸۱ کیلوگرم در هر متر و ضخامت عایق آن ۲.۴ میلی‌متر است."),
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
    with open(os.path.join(DATA_DIR, "batch42_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch42_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch42_done_ALL_IMPORTED"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
