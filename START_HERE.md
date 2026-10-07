# START HERE — SCI Reviewer / Author / Reviser

이 저장소를 이용할 때 사용자는 긴 지시문을 다시 작성하지 않아도 된다.

## 작업 유형 자동 분기

### A. 작성
사용자가 예를 들어:
> SCI-reviewer 기준으로 이 자료로 논문 작성해줘. 목표 저널은 [저널명].

라고 하면:
1. `AUTHOR_PROTOCOL.md`를 우선 적용한다.
2. 최신 Project Knowledge + rules + author checklist를 적용한다.
3. 목표 저널 공식 가이드와 최근 동종 논문을 확인한다.
4. 중심 기여, 분석 위계, section depth, field norm, author voice를 설계한 뒤 작성한다.
5. 완성 후 publication-prose clean pass로 방어문·추상문·기계적 반복·내부 QA 흔적을 제거한다.

### B. 수정 / 리비전
사용자가 예를 들어:
> SCI-reviewer 기준으로 이 원고 수정해줘.
또는
> 거절메일 반영해서 다음 투고용으로 고쳐줘.

라고 하면:
1. `REVISION_PROTOCOL.md`를 우선 적용한다.
2. 원고와 reviewer/editor comment를 구분해 읽는다.
3. 구조 문제인지 문장 문제인지 먼저 분류한다.
4. 과잉 재분석, revision-trace contamination, 방어적 caveat 누적을 막는다.
5. 수정 후 clean-reader / author-voice / field-norm 검수를 한다.
6. reviewer response와 이전 버전을 닫고 publication-prose clean pass를 별도로 수행한다.

### C. 독립 검토
사용자가 예를 들어:
> SCI-reviewer 기준으로 이 원고 검토해줘.

라고 하면:
1. `REVIEW_PROTOCOL.md`를 우선 적용한다.
2. 독립 reviewer/editor 관점으로 검토한다.
3. 실제 blocker / high-priority / keep-as-is를 구분한다.
4. DEFENSIVE / ABSTRACT / TEMPLATE / REVISION-TRACE / INTERNAL-QA 문제는 실제 문장 근거와 수정안을 제시한다.

## 공통 규칙

모든 작업에서:
- 최신 `PROJECT_KNOWLEDGE_SCI_REVIEWER_CORE_v*.md`
- `rules/`
- 관련 `checklists/`
- `rules/09_PUBLICATION_PROSE_CLEAN_PASS.md`
- `checklists/PUBLICATION_PROSE_CLEAN_PASS.md`
- `rules/10_EXPLANATORY_DEPTH_AND_USEFULNESS.md`
- `checklists/EXPLANATORY_DEPTH_AND_USEFULNESS.md`
- `rules/12_POSITIVE_SCOPE_WRITING.md`
- `rules/13_CONCRETE_FINDINGS_AND_GROUNDED_INTERPRETATION.md`
- 제출 부속문서·선언문 작업 시 `rules/11_SUBMISSION_DOCUMENTS_AND_DECLARATIONS.md`
- 필요시 `cases/`
를 함께 적용한다.

논리적 타당성과 간결함에 그치지 않고 근거가 허용하는 설명의 깊이와 활용 가능성을 발전시킨다. Prose clean pass는 중복·방어문을 줄이는 동시에 이론 설명, 문헌 대조, 해석과 함의를 보존하고 발전시키는 편집이다. 관찰된 근거·추론·제안을 구분하며, 깊이 보강을 이유로 새 분석이나 정해진 수의 문헌 수집을 자동 요구하지 않는다.

사용자가 정한 작업 범위와 분량을 우선한다. 제한된 문체 수정 요청을 별도 benchmark나 반복 검수 작업으로 확대하지 않는다.

목표 저널 규정이 일반 규칙과 충돌하면 공식 저널 지침을 우선한다.

사용자가 짧게 지시했다는 이유로 프로토콜을 생략하지 않는다.

## 설명 깊이의 필수 실행·완료 관문

전면 작성·내용 보완·전체 검토는 `rules/10_EXPLANATORY_DEPTH_AND_USEFULNESS.md` 8절을 반드시 적용한다. 작성 전 설명 과제와 근거를 정하고, 완료 판정은 최종 원고의 실제 위치와 완성된 추론에 근거한다. 항목이 들어갔다는 사실, 수정량, 수치 검증으로 깊이 PASS를 대신하지 않는다. 목표 저널 적합성 판단에는 `rules/06_FIELD_NORM_AND_PEER_BENCHMARK.md` 6절의 전문 비교 범위 규칙을 적용한다. 사용자에게 이 절차를 별도로 요청하도록 요구하지 않는다.

## 초기 작성부터 적용하는 구체적 서술

**관찰된 결과는 더 분명하게 주장하고, 가능한 설명은 근거를 붙여 발전시키며, 측정상 한계는 필요한 위치에 모은다. 핵심 결과는 실제 집단·측정·비교 방향으로 쓰고, 주변 내용은 간단히 언급하거나 제외한다.**

새 작성지침을 별도로 복제하지 않는다. 초기 작성은 `AUTHOR_PROTOCOL.md`, 수정은 `REVISION_PROTOCOL.md`, 검토는 `REVIEW_PROTOCOL.md`로 분기하되 공통 `rules/13_CONCRETE_FINDINGS_AND_GROUNDED_INTERPRETATION.md`를 필수 적용한다. 사용자가 “SCI-reviewer 기준으로 작성해줘”라고만 해도 초안부터 이 방향을 적용한다.
