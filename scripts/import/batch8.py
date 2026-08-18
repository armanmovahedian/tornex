# -*- coding: utf-8 -*-
"""Batch 8: 12 Cisco Catalyst C9200L switch variants."""
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


def switch_content(model, ports, poe, uplink, edition, switching, forward):
    poe_desc = (f"{ports} پورت PoE+ دارد که امکان تغذیه مستقیم دوربین‌های نظارتی، اکسس‌پوینت‌های وایرلس و تلفن‌های VoIP را از طریق کابل شبکه فراهم می‌کند"
                if poe else f"{ports} پورت اترنت استاندارد (بدون PoE) دارد")
    uplink_desc = ("۴ پورت آپلینک ۱۰ گیگابیت بر ثانیه" if uplink == "10G" else "۴ پورت آپلینک ۱ گیگابیت بر ثانیه")
    edition_desc = ("و از نرم‌افزار Network Advantage با قابلیت‌های مسیریابی لایه ۳ مانند OSPF و EIGRP پشتیبانی می‌کند"
                     if edition == "Advantage" else "و از نرم‌افزار Network Essentials با امکانات مدیریتی و امنیتی ضروری لایه ۲ پشتیبانی می‌کند")
    return f"""<p>سوییچ {ports} پورت سیسکو Catalyst {model} با {uplink_desc} طراحی شده است. این سوییچ {poe_desc} {edition_desc}. ظرفیت سوئیچینگ آن {switching} گیگابیت بر ثانیه و نرخ پردازش بسته آن {forward} میلیون بسته در ثانیه است که آن را برای دیتاسنترها و شبکه‌های سازمانی پرترافیک مناسب می‌سازد.</p>
<p>این سوییچ از رمزگذاری AES-128 MACsec، VLAN (تا ۱۰۲۴ عدد)، ACL و QoS برای مدیریت پهنای باند پشتیبانی می‌کند و پهنای باند استکینگ آن ۸۰ گیگابیت بر ثانیه است. حافظه رم آن ۲ گیگابایت و حافظه فلش آن ۴ گیگابایت است و از Cisco SD-Access و Plug and Play پشتیبانی می‌کند.</p>"""


MODELS = [
    {"model": "C9200L-48P-4X-A", "ports": 48, "poe": True, "uplink": "10G", "edition": "Advantage", "switching": "176", "forward": "261.9"},
    {"model": "C9200L-24T-4X-A", "ports": 24, "poe": False, "uplink": "10G", "edition": "Advantage", "switching": "128", "forward": "190.4"},
    {"model": "C9200L-24P-4X-A", "ports": 24, "poe": True, "uplink": "10G", "edition": "Advantage", "switching": "128", "forward": "190.4"},
    {"model": "C9200L-48T-4X-E", "ports": 48, "poe": False, "uplink": "10G", "edition": "Essentials", "switching": "176", "forward": "261.9"},
    {"model": "C9200L-48P-4X-E", "ports": 48, "poe": True, "uplink": "10G", "edition": "Essentials", "switching": "176", "forward": "261.9"},
    {"model": "C9200L-24T-4X-E", "ports": 24, "poe": False, "uplink": "10G", "edition": "Essentials", "switching": "128", "forward": "190.4"},
    {"model": "C9200L-24P-4X-E", "ports": 24, "poe": True, "uplink": "10G", "edition": "Essentials", "switching": "128", "forward": "190.4"},
    {"model": "C9200L-48T-4G-A", "ports": 48, "poe": False, "uplink": "1G", "edition": "Advantage", "switching": "104", "forward": "154.76"},
    {"model": "C9200L-48P-4G-A", "ports": 48, "poe": True, "uplink": "1G", "edition": "Advantage", "switching": "104", "forward": "154.76"},
    {"model": "C9200L-24T-4G-A", "ports": 24, "poe": False, "uplink": "1G", "edition": "Advantage", "switching": "56", "forward": "83.33"},
    {"model": "C9200L-24P-4G-A", "ports": 24, "poe": True, "uplink": "1G", "edition": "Advantage", "switching": "56", "forward": "83.33"},
    {"model": "C9200L-48P-4G-E", "ports": 48, "poe": True, "uplink": "1G", "edition": "Essentials", "switching": "104", "forward": "154.76"},
]

assert len(MODELS) == len(slugs), f"{len(MODELS)} authored vs {len(slugs)} slugs"

batch = []
for slug, m in zip(slugs, MODELS):
    pre = pre_by_slug[slug]
    batch.append({
        "slug": pre["slug"],
        "title": pre["title"],
        "excerpt_html": pre["excerpt_html"],
        "content_html": switch_content(m["model"], m["ports"], m["poe"], m["uplink"], m["edition"], m["switching"], m["forward"]),
        "extra_specs": pre["extra_specs"],
        "category_name": "سوییچ و مبدل شبکه",
        "category_parent_name": "تجهیزات شبکه",
        "specs": {"brand": "سیسکو", "size_diameter": "", "conductor_material": "",
                   "standard": CISCO_STD,
                   "application": "شبکه‌های سازمانی، دیتاسنترها و زیرساخت‌های ISP با نیاز به سوئیچینگ لایه ۲ پرسرعت"},
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
    with open(os.path.join(DATA_DIR, "batch8_result.txt"), "w", encoding="utf-8") as f:
        f.write(result)
    print("done, see data/batch8_result.txt")

    progress_path = os.path.join(DATA_DIR, "progress.json")
    with open(progress_path, encoding="utf-8") as f:
        progress = json.load(f)
    progress.setdefault("processed_slugs", [])
    for slug in slugs:
        if slug not in progress["processed_slugs"]:
            progress["processed_slugs"].append(slug)
    progress["phase"] = "phase7_batch8_done"
    with open(progress_path, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)
