# -*- coding: utf-8 -*-
"""Prepares the next N unprocessed products as plain-text for the model to
read and rewrite (strips HTML tags from core_html since the model doesn't
need to preserve barghsan's markup -- it writes fresh <p> paragraphs anyway).
Usage: python prepare_batch.py [N]"""
import json
import os
import re
import sys

HERE = os.path.dirname(__file__)
DATA_DIR = os.path.join(HERE, "..", "..", "data")
PRE_PATH = os.path.join(DATA_DIR, "preprocessed_products.jsonl")
PROGRESS_PATH = os.path.join(DATA_DIR, "progress.json")
OUT_PATH = os.path.join(DATA_DIR, "batch_review.txt")

N = int(sys.argv[1]) if len(sys.argv) > 1 else 15


def strip_tags(html):
    text = re.sub(r'<(h2|/h2|/p|li|/li|/tr)>', lambda m: '\n', html)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n+', '\n', text)
    return text.strip()


def main():
    with open(PROGRESS_PATH, encoding='utf-8') as f:
        progress = json.load(f)
    done = set(progress.get('processed_slugs', []))

    picked = []
    with open(PRE_PATH, encoding='utf-8') as f:
        for line in f:
            row = json.loads(line)
            if row['slug'] in done:
                continue
            picked.append(row)
            if len(picked) >= N:
                break

    lines = []
    for i, row in enumerate(picked, 1):
        lines.append(f"===== #{i} | slug={row['slug']} =====")
        lines.append(f"title: {row['title']}")
        lines.append(f"barghsan_categories: {row['barghsan_categories']}")
        lines.append(f"suggested_category: {row['suggested_category']}")
        lines.append(f"auto_specs: {json.dumps(row['specs'], ensure_ascii=False)}")
        lines.append(f"extra_specs: {json.dumps(row['extra_specs'], ensure_ascii=False)}")
        lines.append(f"price: {json.dumps(row['price'], ensure_ascii=False)}")
        lines.append(f"datasheet_url: {row['datasheet_url'] or '(none)'}")
        lines.append("--- content to rewrite ---")
        lines.append(strip_tags(row['core_html'])[:3000])
        lines.append("")

    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"prepared {len(picked)} products -> {OUT_PATH}")
    # also dump the picked slugs for the batch-builder script to reference
    with open(os.path.join(DATA_DIR, 'batch_slugs.json'), 'w', encoding='utf-8') as f:
        json.dump([r['slug'] for r in picked], f, ensure_ascii=False)


if __name__ == '__main__':
    main()
