#!/usr/bin/env python3
"""Read-only candidate scan. Never detects AI authorship or certifies a manuscript.
Exit 0: no candidates, 1: manual review needed, 2: input error.
DOCX includes body/tables/headers/footers/comments/notes; no OCR or layout check.
"""
import argparse
import collections
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
PATTERNS = {
    'INTERNAL': r'교수님\s*확인\s*대기|(?:최종\s*)?잠금(?:된|\s*완료)|검수\s*(?:통과|완료)|재검증\s*완료|실행\s*(?:불가|실패).{0,15}종결|QA\s*(?:PASS|passed)|locked\s+(?:analysis|model)',
    'PLACEHOLDER': r'\bTODO\b|\bTBD\b|\[(?:초록|주제어|고찰|결론|연구의 한계)[^\]]*삽입[^\]]*\]',
    'DEFENSIVE': r'해석해서는\s*안|입증하지\s*않|의미하지\s*않|뜻하지\s*않|does\s+not\s+imply|should\s+not\s+be\s+interpreted|cannot\s+be\s+interpreted',
    'TEMPLATE': r'중요한\s*시사점을\s*제공|복잡하고\s*다층적|\bTaken\s+together\b|\bImportantly\b|\bNotably\b',
}


def paragraphs(path):
    if path.suffix.lower() == '.docx':
        with zipfile.ZipFile(path) as z:
            names = [n for n in z.namelist() if re.fullmatch(
                r'word/(?:document|header\d+|footer\d+|footnotes|endnotes|comments)\.xml', n)]
            if 'word/document.xml' not in names:
                raise ValueError('DOCX body missing')
            for n in sorted(names):
                root = ET.fromstring(z.read(n))
                for i, p in enumerate(root.iter(W + 'p'), 1):
                    # Preserve tabs and breaks; do not scan deleted revision text.
                    txt = ''.join((e.text or '') if e.tag == W+'t' else ' '
                                  for e in p.iter() if e.tag in (W+'t', W+'tab', W+'br'))
                    if txt.strip():
                        yield f'{n}:p{i}', txt
        return
    if path.suffix.lower() not in ('.txt', '.md'):
        raise ValueError('Supported inputs: .docx, .txt, .md')
    for i, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        if line.strip():
            yield f'line:{i}', line


def scan(rows, single_author=False):
    out = []
    sentences = collections.defaultdict(list)
    openers = collections.defaultdict(list)
    for loc, text in rows:
        for kind, regex in PATTERNS.items():
            hits = list(re.finditer(regex, text, re.I))
            # A single necessary boundary is not a density candidate.
            if hits and (kind != 'DEFENSIVE' or len(hits) >= 2):
                out.append({'kind': kind, 'location': loc, 'excerpt': text[max(0,hits[0].start()-30):hits[0].end()+100]})
        if '—' in text:
            out.append({'kind': 'AUTHOR_PUNCTUATION', 'location': loc, 'excerpt': text[:140]})
        if single_author and re.search(r'\b(?:I|we|our)\b', text, re.I):
            out.append({'kind': 'AUTHOR_PERSON', 'location': loc, 'excerpt': text[:140]})
        # Deliberately conservative: no split at decimals or abbreviations.
        for s in re.split(r'(?<=[.!?。])\s+(?=[A-Z가-힣])', text):
            norm = re.sub(r'\s+', ' ', s).strip()
            if len(norm) >= 45:
                sentences[norm].append(loc)
        words = text.strip().split()
        if len(words) >= 8:
            openers[' '.join(words[:4]).lower()].append(loc)
    for s, locs in sentences.items():
        if len(locs) > 1:
            out.append({'kind': 'REPEATED_SENTENCE', 'location': ', '.join(locs), 'excerpt': s[:160]})
    for s, locs in openers.items():
        if len(locs) >= 3:
            out.append({'kind': 'REPEATED_OPENER', 'location': ', '.join(locs), 'excerpt': s})
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('manuscript', type=Path)
    p.add_argument('--single-author', action='store_true')
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    try:
        rows = list(paragraphs(args.manuscript))
        if not rows:
            raise ValueError('No readable text; scanned images are not supported')
        candidates = scan(rows, args.single_author)
    except (OSError, ValueError, ET.ParseError, zipfile.BadZipFile) as e:
        print(f'Input error: {e}', file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({'scope': 'text candidates only; no OCR, layout, facts or citations verified',
                          'candidates': candidates}, ensure_ascii=False, indent=2))
    else:
        print('문체 후보 검색만 수행했습니다. AI 판별·사실 검증·제출 가능 판정이 아닙니다.')
        for c in candidates:
            print(f"[{c['kind']}] {c['location']} | {c['excerpt']}")
        print(f'후보 {len(candidates)}건. 표·인용·필수 한계는 문맥을 읽고 유지 여부를 결정하세요.')
    return 1 if candidates else 0


if __name__ == '__main__':
    sys.exit(main())
