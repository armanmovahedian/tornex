# -*- coding: utf-8 -*-
"""Batch 41: 20 products -- 1 Legrand trunking internal angle + 3
trunking bodies (50x150, 50x105, 50x80), 3 Legrand power strips
(6-way, 6-way surge-protected, 4-way), 2 Legrand mosaic accessories
(doorbell push + screw-mount support), 4 Legrand mosaic frames
(1/2/3/4-gang), 2 Legrand antenna/SAT sockets, 3 Legrand AV sockets
(HDMI/VGA/USB), and 2 Legrand colored grounded power sockets."""
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


def internal_angle_content(code, width_label, trunking_example):
    return f"""<p>زاویه داخلی ترانکینگ {width_label} لگراند (کد {code}) از جنس PVC بدون سرب ساخته شده و برای استفاده با {trunking_example} مناسب است. این محصول از دو قطعه مثلثی تشکیل شده که محل اتصال دو شاخه ترانک را در گوشه‌های داخلی به‌طور کامل می‌پوشاند و با هماهنگی درب نرم ترانکینگ، نمایی یکدست ایجاد می‌کند.</p>
<p>رنگ آن سفید است و ساخت کشور فرانسه است.</p>"""


def trunking_body_content(code, dims, weight, capacity_desc):
    return f"""<p>ترانکینگ {dims} لگراند (کد {code}) در شاخه‌های ۲ متری از جنس PVC بدون سرب تولید می‌شود و شامل بدنه و دربی است که روی انواع دیوار (بتنی، آجری، کاذب) قابل نصب است و امکان جای‌گیری مکانیزم‌های سری موزائیک/آرتئور روی درب آن وجود دارد. وزن آن حدود {weight} در هر متر است.</p>
<p>{capacity_desc} استحکام دی‌الکتریک آن بیش از ۲ کیلوولت، ولتاژ نامی ۵۰۰ ولت و درجه مقاومت مکانیکی IK07 است. در بازه دمایی کارکرد ۵- تا ۶۰+ و نگهداری ۲۵- تا ۶۰+ درجه سانتی‌گراد کار می‌کند و خاصیت خودخاموش‌شوندگی تا دمای ۶۵۰ درجه سانتی‌گراد دارد.</p>"""


def power_strip_content(outlets_desc, cable_len, extra=""):
    return f"""<p>چندراهی برق لگراند با {outlets_desc} و کابل {cable_len} متری عرضه می‌شود. بدنه آن از PVC ساخته شده و رنگ آن سفید است. برای جلوگیری از خطر برق‌گرفتگی کودکان، پریزهای آن به محافظ کودک مجهزند که از ورود اشیاء فلزی به داخل پریز جلوگیری می‌کند.{extra}</p>
<p>نگهدارنده داخلی آن از شل شدن و هرزگردی دوشاخه در پریز جلوگیری می‌کند.</p>"""


def four_way_strip_content():
    return """<p>چهارراهی برق لگراند با ۴ خروجی ارت‌دار و کابل ۱.۵ متری عرضه می‌شود. برای جلوگیری از خطر برق‌گرفتگی کودکان، پریزهای آن به محافظ کودک مجهزند که از ورود اشیاء فلزی جلوگیری می‌کند. جریان نامی آن ۱۶ آمپر و ولتاژ کاری آن ۲۵۰ ولت است.</p>
<p>دوشاخه آن دارای سر چرخشی است که امکان پیچ شدن به سطوح مختلف را فراهم می‌کند. بدنه آن از PVC به رنگ سفید-طوسی ساخته شده است.</p>"""


def doorbell_switch_content(code):
    return f"""<p>شاسی زنگ دو ماژول سفید موزائیک لگراند (کد {code}) ابعاد ۴۵×۴۵ میلی‌متر دارد و با تمامی کادرها و حلقه‌های سری موزائیک و آرتئور سازگار است. بدنه آن از پلی‌کربنات (PC) مقاوم در برابر حرارت و اشعه UV ساخته شده و هالوژن‌فری است، به این معنا که در آتش‌سوزی دود سمی تولید نمی‌کند.</p>
<p>از جریان ۶ آمپر و ولتاژ ۲۵۰ ولت پشتیبانی می‌کند و درجه حفاظت آن IP31D (محافظت در برابر گردوغبار و تماس تصادفی) و مقاومت ضربه آن IK04 (تا ۰.۵ ژول) است. ترمینال‌های اتوماتیک آن با ظرفیت سیم‌کشی ۲×۲.۵ میلی‌متر مربع و طول سیم‌لختی استاندارد ۱۲ میلی‌متر، نصب سریع و ایمن را فراهم می‌کند و قابلیت نصب چراغ نشانگر (Easy-LED) نیز دارد. در بازه دمایی ۵- تا ۳۵+ درجه سانتی‌گراد کار می‌کند.</p>"""


def screw_support_content(code):
    return f"""<p>ساپورت پیچی موزائیک لگراند (کد {code}) با ابعاد ۷۴×۴۰.۵ میلی‌متر برای نصب روی قوطی‌های پیچی استاندارد طراحی شده و مکانیزم‌های موزائیک و سلین را به‌صورت افقی و عمودی پشتیبانی می‌کند و روی قوطی‌های ۵۷ میلی‌متری نیز قابل نصب است. برای نصب روکار نیز می‌توان آن را همراه باکس مخصوص لگراند استفاده کرد.</p>
<p>از فولاد گالوانیزه با پوشش Galfan (ترکیب روی و آلومینیوم با مقاومت بالا در برابر خوردگی) ساخته شده و خاصیت خوداطفایی تا دمای ۶۵۰ درجه سانتی‌گراد به مدت ۳۰ ثانیه دارد. با نشانگرهای Easy-LED نیز سازگار است.</p>"""


def mosaic_frame_content(code, module_count, gang_desc):
    return f"""<p>کادر {gang_desc} موزائیک لگراند (کد {code}) برای نصب پریز برق، پریز شبکه، پریز تلفن، کلید و سایر مکانیزم‌های استاندارد موزائیک طراحی شده و روی انواع دیوار (کاذب، چوبی، بتنی) با استفاده از ساپورت مخصوص (پیچی یا چنگکی) قابل نصب است. ظرفیت آن {module_count} ماژول است.</p>
<p>از پلیمر ABS بدون هالوژن با سطح پلی‌گلاس (مقاوم در برابر خط‌وخش) ساخته شده و مطابق استاندارد IK04 در برابر ضربه تا ۰.۵ ژول مقاوم است. خاصیت خوداطفایی آن تا دمای ۶۵۰ درجه سانتی‌گراد به مدت ۳۰ ثانیه است. رنگ آن سفید است و در بازه دمایی ۵- تا ۳۵+ درجه سانتی‌گراد کار می‌کند.</p>"""


def antenna_socket_content(code, type_label, extra_signal, ik):
    return f"""<p>پریز {type_label} دو ماژول سفید موزائیک لگراند (کد {code}) امپدانس ۷۵ اهمی دارد و برای نصب در جعبه برق با عمق حداقل ۴۰ میلی‌متر طراحی شده است. با پشتیبانی از کابل کواکسیال ۱۷/۱۹ VATC، سیگنال را با کیفیت بالا و افت کم منتقل می‌کند.{extra_signal}</p>
<p>کلاس حفاظتی A آن از تداخل سیگنال‌های 4G و LTE جلوگیری می‌کند. بدنه آن از پلاستیک ABS استاندارد RAL 9003 و قطعات داخلی از فلز زاماک ساخته شده که در برابر ضربه، تغییرات دمایی، اشعه UV و مواد شیمیایی رایج مقاوم است. درجه حفاظت آن IP21 و مقاومت ضربه آن {ik} است و در بازه دمایی ۵- تا ۳۵+ درجه سانتی‌گراد کار می‌کند.</p>"""


def av_socket_content(code, port_label, module_count, tech_desc):
    return f"""<p>پریز {port_label} {module_count} سفید موزائیک لگراند (کد {code}) بدنه‌ای از جنس ABS با رنگ RAL 9003 دارد و به‌راحتی در انواع ترانکینگ، مینی‌ستون و باکس‌های رومیزی پاپ‌آپ نصب می‌شود. {tech_desc}</p>
<p>درجه حفاظت آن IP40 (مقاومت در برابر نفوذ اجسام جامد بزرگ‌تر از ۱ میلی‌متر) و مقاومت ضربه آن IK04 (تا ۰.۵ ژول) است و خاصیت خودخاموش‌شوندگی دارد. در بازه دمایی ۵- تا ۵۰+ درجه سانتی‌گراد کار می‌کند.</p>"""


def power_socket_content(code, color_label, extra=""):
    return f"""<p>پریز برق ارتدار {color_label} دو ماژول موزائیک لگراند (کد {code}) ابعاد استاندارد ۴۵×۴۵ میلی‌متر دارد و با تمامی کادرها و مکانیزم‌های سری موزائیک سازگار است. بدنه آن از پلی‌کربنات (PC) مقاوم در برابر حرارت و اشعه UV و هالوژن‌فری است، یعنی در آتش‌سوزی دود سمی تولید نمی‌کند.{extra}</p>
<p>ترمینال‌های اتوماتیک آن با ظرفیت سیم‌کشی ۲×۲.۵ میلی‌متر مربع و طول سیم‌لختی استاندارد ۱۲ میلی‌متر، نصب بدون پیچ و سریع را فراهم می‌کند. جریان نامی آن ۱۶ آمپر و ولتاژ نامی ۲۵۰ ولت است و درجه حفاظت آن IP20 و مقاومت ضربه آن IK04 است.</p>"""


RECORDS = [
    {  # 1 - internal angle width80-105 010602
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "عبور ترانکینگ از زاویه داخلی دیوار در عرض ۸۰ یا ۱۰۵"},
        "content_html": internal_angle_content("010602", "عرض ۸۰ و ۱۰۵", "ترانکینگ ۸۰ در ۵۰ و ترانکینگ ۱۰۵ در ۵۰ لگراند"),
    },
    {  # 2 - trunking body 50x150 010427
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "150x50 mm", "conductor_material": "",
                   "standard": "", "application": "کابل‌کشی روکار حجم بالا در ادارات و ساختمان‌های تجاری"},
        "content_html": trunking_body_content("010427", "۵۰ در ۱۵۰", "۱.۲۰ کیلوگرم",
                                                "سطح مقطع داخلی آن ۶۷۰۰ میلی‌متر مربع است و ظرفیت عبور حدود ۶۷ کابل با قطر ۷.۵ میلی‌متر یا ۲۷ کابل ۳×۱.۵ میلی‌متر مربع را دارد."),
    },
    {  # 3 - trunking body 50x105 010464
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "105x50 mm", "conductor_material": "",
                   "standard": "", "application": "کابل‌کشی روکار حجم متوسط در ادارات و ساختمان‌های تجاری و آموزشی"},
        "content_html": trunking_body_content("010464", "۵۰ در ۱۰۵", "۰.۸۵ کیلوگرم",
                                                "سطح مقطع داخلی آن ۴۳۰۰ میلی‌متر مربع است و ظرفیت عبور حدود ۴۳ کابل با قطر ۷.۵ میلی‌متر را دارد."),
    },
    {  # 4 - trunking body 50x80 010462
        "category_name": "ترانکینگ و اکسسوری", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "80x50 mm", "conductor_material": "",
                   "standard": "", "application": "کابل‌کشی روکار حجم کم در ساختمان‌های مسکونی و مسیرهای کوتاه"},
        "content_html": trunking_body_content("010462", "۵۰ در ۸۰", "۷۰ گرم",
                                                "سطح مقطع داخلی آن ۳۲۰۰ میلی‌متر مربع است و ظرفیت عبور حدود ۳۲ کابل با قطر ۷.۵ میلی‌متر را دارد."),
    },
    {  # 5 - 6-way strip
        "category_name": "چند راهی برق", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "تغذیه چند دستگاه برقی از یک پریز با محافظ کودک"},
        "content_html": power_strip_content("۶ خروجی ارت‌دار", "۱.۵", " این محصول فاقد محافظ نوسان برق است."),
    },
    {  # 6 - 6-way strip surge-protected
        "category_name": "چند راهی برق", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "تغذیه و محافظت تجهیزات الکترونیکی در برابر نوسان ولتاژ"},
        "content_html": power_strip_content("۶ خروجی محافظ‌دار", "۱.۵", " این محصول در برابر نوسانات و افزایش ناگهانی ولتاژ محافظت می‌کند و از آسیب دیدن تجهیزات الکترونیکی متصل جلوگیری می‌کند."),
    },
    {  # 7 - 4-way strip
        "category_name": "چند راهی برق", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "", "application": "تغذیه چند دستگاه برقی از یک پریز با محافظ کودک"},
        "content_html": four_way_strip_content(),
    },
    {  # 8 - doorbell switch 278040L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP31D، IEC 60695-2-11", "application": "زنگ اخبار در منزل، اداره یا فضای عمومی"},
        "content_html": doorbell_switch_content("278040L"),
    },
    {  # 9 - screw support 080251
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IEC 60695-2-11", "application": "نصب مکانیزم‌های موزائیک روی قوطی پیچی استاندارد"},
        "content_html": screw_support_content("080251"),
    },
    {  # 10 - 4-gang frame 078808L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IEC 60695-2-11", "application": "نصب چهار مکانیزم دو ماژولی موزائیک روی دیوار"},
        "content_html": mosaic_frame_content("078808L", "۸", "چهار خانه"),
    },
    {  # 11 - 3-gang frame 277806L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IEC 60695-2-11", "application": "نصب سه مکانیزم دو ماژولی موزائیک روی دیوار"},
        "content_html": mosaic_frame_content("277806L", "۶", "سه خانه"),
    },
    {  # 12 - 2-gang frame 277804L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IEC 60695-2-11", "application": "نصب دو مکانیزم دو ماژولی موزائیک روی دیوار"},
        "content_html": mosaic_frame_content("277804L", "۴", "دو خانه"),
    },
    {  # 13 - 1-gang frame 277802L
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IEC 60695-2-11", "application": "نصب یک مکانیزم دو ماژولی موزائیک روی دیوار"},
        "content_html": mosaic_frame_content("277802L", "۲", "یک خانه"),
    },
    {  # 14 - antenna+SAT socket 078786
        "category_name": "پریز آنتن", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP21، IEC 60695-2-11", "application": "دریافت همزمان سیگنال تلویزیون، رادیو و ماهواره"},
        "content_html": antenna_socket_content("078786", "آنتن و ماهواره",
                                                 " سیگنال‌های تلویزیونی (۵ تا ۸۶۲ مگاهرتز)، رادیویی (۸۷.۵ تا ۲۴۰ مگاهرتز) و ماهواره‌ای (۹۵۰ تا ۲۴۰۰ مگاهرتز) را دریافت می‌کند.", "IK04"),
    },
    {  # 15 - antenna socket 078782
        "category_name": "پریز آنتن", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK03، IP21، IEC 60695-2-11", "application": "دریافت سیگنال تلویزیون دیجیتال و آنالوگ"},
        "content_html": antenna_socket_content("078782", "آنتن",
                                                 " فرکانس کاری آن ۰ تا ۲۴۰۰ مگاهرتز است و سیگنال‌های دیجیتال را با حداکثر تضعیف ۱ دسی‌بل منتقل می‌کند.", "IK03"),
    },
    {  # 16 - HDMI socket 078778
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP40، EN 60669-1، IEC 60695-2-11", "application": "اتصال تصویری HDMI در سالن کنفرانس یا فضای اداری"},
        "content_html": av_socket_content("078778", "HDMI", "یک ماژول",
                                           "مجهز به یک کابل ۱۵ سانتی‌متری با دو کانکتور مادگی است و از استاندارد Plug & Play و HDMI 1.4 با پشتیبانی از وضوح 1080p برخوردار است."),
    },
    {  # 17 - VGA socket 078777
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP40، EN 60669-1، IEC 60695-2-11", "application": "اتصال تصویری VGA در فضای اداری یا آموزشی"},
        "content_html": av_socket_content("078777", "VGA", "یک ماژول",
                                           "از استاندارد HD15 پشتیبانی می‌کند و وضوح‌های VGA، XGA و UXGA را با حداکثر طول کابل ۲۰ متر پشتیبانی می‌کند."),
    },
    {  # 18 - USB socket 078761
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP40، EN 60669-1، IEC 60695-2-11", "application": "اتصال و انتقال داده USB در فضای اداری"},
        "content_html": av_socket_content("078761", "USB", "یک ماژول",
                                           "از استاندارد USB 1.1 با سرعت انتقال ۱۲ مگابیت بر ثانیه پشتیبانی می‌کند و حداکثر طول کابل قابل استفاده برای آن ۵ متر است."),
    },
    {  # 19 - green power socket 077216
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP20، IEC 60695-2-11", "application": "پریز برق عمومی با کد رنگی سبز"},
        "content_html": power_socket_content("077216", "سبز"),
    },
    {  # 20 - orange power socket 077217
        "category_name": "کلید و پریز", "category_parent_name": SWITCH_PARENT,
        "specs": {"brand": "لگراند", "size_diameter": "", "conductor_material": "",
                   "standard": "IK04، IP20، IEC 60695-2-11", "application": "پریز برق اضطراری UPS با کد رنگی نارنجی"},
        "content_html": power_socket_content("077217", "نارنجی", " رنگ نارنجی متمایز آن معمولاً برای تفکیک مدار برق اضطراری (UPS) از برق شهری استفاده می‌شود."),
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
    with open(os.path.join(DATA_DIR, "batch41_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch41_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch41_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
