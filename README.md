# SCI-reviewer — 핵심 규칙 v1.0

논문 작성·편집·검증을 위한 규칙. **많은 지침을 모두 적용하는 방식에서, 하나의 핵심 기준과 해당 작업 절차만 적용하는 방식으로 정리했다.**

## 시작

[START_HERE.md](START_HERE.md) → [CORE_RULES.md](CORE_RULES.md) → 작업별 프로토콜 하나.

| 문서 | 역할 |
|---|---|
| [CORE_RULES.md](CORE_RULES.md) | 유일한 현행 공통 의무. 기본 틀·양식, 문체, 근거·해석, 파일 편집, 완료 관문 |
| [AUTHOR_PROTOCOL.md](AUTHOR_PROTOCOL.md) | 초기 작성·내용 보완 |
| [REVISION_PROTOCOL.md](REVISION_PROTOCOL.md) | 심사의견(R&R) 대응. 심사의견 없는 편집 포함 |
| [REVIEW_PROTOCOL.md](REVIEW_PROTOCOL.md) | 투고 전 자체 리뷰·최종검수 |
| [AGENTS.md](AGENTS.md) | 지원하는 작업 도구의 자동 진입점 |

**내부 작업문구, 기능 없는 반복, 기계적 문단 틀, 불필요한 과잉 방어는 원고에 남기지 않는다.** 동시에 필요한 측정 정의·불확실성·연구한계·설명 깊이는 보존한다. 위반이나 미확인을 숨기고 완료라고 보고하지 않는다.

## 적용 방법

> https://github.com/jskwon89/SCI-reviewer 의 START_HERE.md 기준으로 첨부 원고를 수정해줘.

수정 표시, 특정 절, 목표 저널처럼 작업 조건만 덧붙이면 된다. 규칙 링크를 열지 못한 도구는 자동 적용됐다고 가정할 수 없다. 규칙 문서만으로 모든 AI의 무위반 동작을 보장하지 않으므로 실제 문장·근거·파일의 완료 관문을 사용한다.

## 간단한 후보 검사

Python 3 표준 라이브러리만 사용한다. 원고를 수정하거나 업로드하지 않는다.

```bash
python tools/prose_check.py /path/to/manuscript.docx --single-author
python -m unittest discover -s tests -v
```

입력: DOCX/TXT/MD. 결과: 내부 문구·자리표시자·반복 문장/도입구·방어문 누적·저자 문체 후보와 위치. 종료코드 `0=후보 없음`, `1=문맥 검토 필요`, `2=입력 오류`. **0도 사실·인용·논증·레이아웃 통과나 AI 판별 결과가 아니다.** 후보를 삭제할지는 원고 문맥으로 결정한다. 이미지 속 글자는 읽지 않는다. 로그에 원고 일부가 나오므로 비공개 원고를 공개 CI/커밋에 넣지 않는다.

## 참고와 이력

- [문헌 전문 비교 및 통합 근거](sources/CORE_RULES_EVIDENCE.md)
- [공개 자료 정책](sources/PUBLIC_SOURCE_POLICY.md)
- [변경 기록](CHANGELOG.md)
- `rules/`, `checklists/`, `PROJECT_KNOWLEDGE_*`, `cases/`: 필요할 때 찾아보는 과거 상세 자료. 전체 필수 적용 아님. 충돌 시 핵심 규칙 우선.

v0.9의 구체적인 결과 서술·근거 있는 해석·설명 깊이 원칙은 유지했다. 반복 검수·문헌 수 할당·모든 문서 재독·장문 완료보고를 필수 절차로 만들지 않는다.
