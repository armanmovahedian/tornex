# -*- coding: utf-8 -*-
"""Phase 4 prep: mechanically strip barghsan's known boilerplate (rep/agent ad
block, images, video, VC shortcode junk, catalogue/datasheet CTA paragraphs,
cross-sell "other brands" blocks, variant linkboxes) out of every raw
product's description + short_description, extract the datasheet URL, and
auto-map barghsan attributes onto Tornex's 5 fixed spec fields + a leftover
"extra specs" list. Writes data/preprocessed_products.jsonl -- one record per
product NOT already in progress.json, with a much shorter `core_html` left
for the model to actually read and rewrite (the real per-product work).
Nothing here writes to production; this is pure local text processing.
"""
import json
import os
import re

HERE = os.path.dirname(__file__)
DATA_DIR = os.path.join(HERE, "..", "..", "data")
RAW_PATH = os.path.join(DATA_DIR, "raw_products.jsonl")
CATMAP_PATH = os.path.join(DATA_DIR, "category_mapping.json")
PROGRESS_PATH = os.path.join(DATA_DIR, "progress.json")
OUT_PATH = os.path.join(DATA_DIR, "preprocessed_products.jsonl")


# ---------------------------------------------------------------------------
# generic balanced-tag block remover
# ---------------------------------------------------------------------------
def remove_block(html, tag, marker):
    """Remove the first (and any further) <tag ...marker...>...</tag> block,
    counting nested same-tag opens/closes to find the true matching close."""
    open_re = re.compile(r"<" + tag + r"\b[^>]*>")
    close_str = "</" + tag + ">"
    while True:
        m = re.search(r"<" + tag + r"\b[^>]*" + re.escape(marker) + r"[^>]*>", html)
        if not m:
            return html
        start = m.start()
        pos = m.end()
        depth = 1
        scan_re = re.compile(r"<" + tag + r"\b[^>]*>|</" + tag + r">")
        end = None
        for tm in scan_re.finditer(html, pos):
            if tm.group().startswith("</"):
                depth -= 1
            else:
                depth += 1
            if depth == 0:
                end = tm.end()
                break
        if end is None:
            return html  # unbalanced -- bail out, leave as-is
        html = html[:start] + html[end:]


def remove_all_blocks(html, tag):
    """Remove every <tag>...</tag> occurrence (non-nested assumption, e.g. figure/table)."""
    return re.sub(r"<" + tag + r"\b.*?</" + tag + r">", "", html, flags=re.S)


def clean_common(html):
    if not html:
        return ""
    # datasheet CTA + catalogue paragraph (datasheet URL already extracted separately)
    html = re.sub(r'<p[^>]*wy-sh-desc-dl-catalogue[^>]*>.*?</p>', '', html, flags=re.S)
    html = re.sub(r'<p>\s*جهت\s*<a[^>]+\.pdf[^>]*>.*?</a>\s*بر روی لینک کلیک نمایید\.\s*</p>', '', html, flags=re.S)
    # "other brands" cross-sell block
    html = re.sub(r'<p[^>]*>\s*برندهای دیگر\s*</p>', '', html)
    html = remove_block(html, 'div', 'ss-brand-box-product')
    # barghsan rep/agent ad block ("برق سان / نماینده رسمی ...")
    html = remove_block(html, 'div', 'wy-agent')
    # per-attribute variant linkbox widget (links to sibling barghsan products)
    html = remove_block(html, 'div', 'wy-p-linkbox')
    # video + all images/figures (images are categorically excluded from the import)
    html = remove_all_blocks(html, 'video')
    html = remove_all_blocks(html, 'figure')
    html = re.sub(r'<img\b[^>]*/?>', '', html)
    # VC (WPBakery) shortcode junk left over from older products -- strip
    # every [vc_xxx]...[/vc_xxx] pair (content included, e.g. vc_raw_html
    # blocks hold base64-encoded junk) for whatever vc_ tags actually appear,
    # not just the outer vc_row wrapper.
    vc_tags = set(re.findall(r'\[vc_(\w+)[^\]]*\]', html))
    for _ in range(3):
        for tag in vc_tags:
            html = re.sub(r'\[vc_' + tag + r'[^\]]*\](.*?)\[/vc_' + tag + r'\]', '', html, flags=re.S)
    html = re.sub(r'\[/?vc_[^\]]*\]', '', html)  # any stray unmatched tags
    html = re.sub(r'\.vc_custom_\d+\{[^}]*\}', '', html)
    # unwrap (keep text, drop link) any remaining barghsan.com/docs.barghsan.com links
    for _ in range(3):
        html = re.sub(r'<a\s+[^>]*href="[^"]*barghsan\.com[^"]*"[^>]*>(.*?)</a>', r'\1', html, flags=re.S)
    # tidy: empty leftover wrapper tags after stripping images/blocks
    for _ in range(4):
        html = re.sub(r'<(div|p|span|a)\b[^>]*>\s*</\1>', '', html, flags=re.S)
    html = re.sub(r'\n{3,}', '\n\n', html).strip()
    return html


def extract_datasheet_url(short_desc_html):
    m = re.search(r'href="([^"]+\.pdf)"', short_desc_html or '')
    return m.group(1) if m else ''


def strip_html_tags(s):
    return re.sub(r'<[^>]+>', '', s or '').strip()


# ---------------------------------------------------------------------------
# attribute -> 5 fixed spec fields mapping
# ---------------------------------------------------------------------------
SPEC_ALIASES = {
    'brand': ['برند'],
    'conductor_material': ['جنس هادی'],
    'size_diameter': ['سطح مقطع', 'قطر', 'سایز'],
}
SKIP_FROM_EXTRA = set(SPEC_ALIASES['brand'])  # brand already consumed


def map_attributes(attributes):
    specs = {'brand': '', 'size_diameter': '', 'conductor_material': '', 'standard': '', 'application': ''}
    extra = []
    used_attr_ids = set()

    for field, aliases in SPEC_ALIASES.items():
        for attr in attributes:
            name = attr.get('name', '')
            if attr['id'] in used_attr_ids:
                continue
            if any(alias in name for alias in aliases):
                terms = ', '.join(t['name'] for t in attr.get('terms', []))
                if terms:
                    specs[field] = terms
                    used_attr_ids.add(attr['id'])
                    break

    for attr in attributes:
        if attr['id'] in used_attr_ids:
            continue
        name = attr.get('name', '')
        terms = ', '.join(t['name'] for t in attr.get('terms', []))
        if name and terms:
            extra.append([name, terms])

    return specs, extra


CODE_LINE_RE = re.compile(r'^[A-Z]{2,6}[\s/-]?[\dA-Z][\d.\-/A-Z\s]*$')


def extract_standard(core_html):
    m = re.search(r'<h2[^>]*>\s*استاندارد[^<]*</h2>(.*?)(?=<h2\b|$)', core_html, re.S)
    if not m:
        return ''
    section = m.group(1)
    pieces = re.split(r'<br\s*/?>|</p>\s*<p[^>]*>', section)
    codes = []
    for piece in pieces:
        text = strip_html_tags(piece)
        if text and CODE_LINE_RE.match(text):
            codes.append(text)
    return '، '.join(codes)


def load_category_map():
    with open(CATMAP_PATH, encoding='utf-8') as f:
        rows = json.load(f)
    return {r['slug']: r for r in rows}


def main():
    cat_map = load_category_map()

    progress = {'processed_slugs': []}
    if os.path.exists(PROGRESS_PATH):
        with open(PROGRESS_PATH, encoding='utf-8') as f:
            progress = json.load(f)
    done = set(progress.get('processed_slugs', []))

    out = []
    with open(RAW_PATH, encoding='utf-8') as f:
        for line in f:
            p = json.loads(line)
            if p['slug'] in done:
                continue

            core_html = clean_common(p.get('description', ''))
            excerpt_html = clean_common(p.get('short_description', ''))
            datasheet_url = extract_datasheet_url(p.get('short_description', ''))

            specs, extra_specs = map_attributes(p.get('attributes', []))
            standard = extract_standard(core_html)
            if standard:
                specs['standard'] = standard

            prices = p.get('prices', {})
            minor = prices.get('currency_minor_unit', 0)
            def toman(key):
                v = prices.get(key)
                if not v:
                    return 0
                return int(int(v) / (10 ** minor))

            cat_info = cat_map.get(p['slug'], {})

            out.append({
                'id': p['id'],
                'slug': p['slug'],
                'title': strip_html_tags(p.get('name', '')),
                'core_html': core_html,
                'excerpt_html': excerpt_html,
                'datasheet_url': datasheet_url,
                'specs': specs,
                'extra_specs': extra_specs,
                'price': {
                    'regular_toman': toman('regular_price'),
                    'sale_toman': toman('sale_price'),
                    'on_sale': bool(p.get('on_sale')),
                    'is_variable': p.get('type') == 'variable',
                },
                'suggested_category': cat_info.get('matched_category'),
                'barghsan_categories': cat_info.get('barghsan_categories', []),
                'source_url': p.get('permalink', ''),
            })

    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        for row in out:
            f.write(json.dumps(row, ensure_ascii=False) + '\n')

    print(f"preprocessed {len(out)} products (skipped {len(done)} already done) -> {OUT_PATH}")


if __name__ == '__main__':
    main()
