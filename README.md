# SCI-reviewer

> **새 검수 대화에서는 가장 먼저 [`START_HERE.md`](START_HERE.md)를 읽는다. 사용자는 긴 검수 지시를 반복할 필요가 없다.**

SSCI/SCI 원고 작성·수정 과정에서 실제 reviewer/editor가 반복적으로 지적한 실패 패턴을 일반화하여 보존하는 연구 글쓰기·리비전 QA 규칙 저장소입니다.

## 목적

특정 논문의 reviewer comment를 그대로 축적하는 것이 아니라, 다른 원고에서도 반복될 수 있는 실패를 사전에 차단합니다.

- 중심 기여가 분석 방법의 새로움에만 머무는 문제
- 제목·초록·이론·RQ/H·방법·결과·논의가 서로 다른 중심을 갖는 문제
- primary / secondary / exploratory 분석의 위계가 글의 위계와 불일치하는 문제
- 저자에게는 정확하지만 외부 독자에게는 해석 불가능한 내부 분석언어
- 개념·용어를 설명하기 전에 사용하는 문제
- 짧게 쓰려다 실제 의미가 사라지는 과도한 압축
- reviewer 대응용 caveat·내부 검수 흔적이 publication-facing prose에 누적되는 문제
- 동종 사회과학 논문보다 분석·용어·보충분석이 과도하게 복잡해지는 문제
- reviewer가 구조 문제를 지적했는데 문장 교정만 반복하는 문제

## 권위 순서

1. `START_HERE.md`
2. `REVIEW_PROTOCOL.md`
3. `PROJECT_KNOWLEDGE_SCI_REVIEWER_CORE_v0.4.md`
4. `rules/00_CORE_REVIEWER_RULES.md`
5. `rules/01_ARGUMENT_ARCHITECTURE.md`
6. `rules/02_READER_FIRST_TERMINOLOGY.md`
7. `rules/03_METHODS_CLARITY_AND_REPLICABILITY.md`
8. `rules/04_ANALYSIS_HIERARCHY.md`
9. `rules/05_DEFENSIVE_WRITING_AND_REVISION_TRACE.md`
10. `rules/06_FIELD_NORM_AND_PEER_BENCHMARK.md`
11. `rules/07_SECTION_DEPTH_AND_WORD_BUDGET.md`
12. `checklists/PRE_SUBMISSION_READER_CLARITY_CHECKLIST.md`
13. `checklists/NAIVE_READER_TEST.md`
14. `checklists/FIELD_BENCHMARK_AUDIT.md`
15. `cases/CASE_INDEX.md`

## 최종 제출 판정

다음 6개 항목을 모두 통과해야 `submission-ready`로 판정합니다.

- ANALYTICALLY CORRECT
- READER-INTERPRETABLE
- ARGUMENT-COHERENT
- CONTRIBUTION-VISIBLE
- PRIMARY/SECONDARY HIERARCHY ALIGNED
- FIELD-NORM ALIGNED

## Publication-context independence

게재본 독자는 이전 투고본, reviewer response, 분석 로그, 수정 이력, old variable name, 수정 전 denominator를 모른다고 가정합니다. 그 지식이 있어야 이해되는 문장·용어·숫자 흐름은 publication-facing 문서에서 금지합니다.

## Public repository source policy

이 저장소는 Public입니다. 따라서 미출판 원고 전문, 비공개 reviewer/editor correspondence, 계정정보 또는 개인정보가 포함된 원문은 커밋하지 않습니다. 실제 사례는 `cases/`에 일반화된 public-safe case record로 보존합니다. 원문이 필요한 검수에서는 사용자가 제공한 private Project/Conversation source를 별도로 대조합니다.

Version: v0.4.1
