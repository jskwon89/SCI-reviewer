# 05. Defensive Writing and Revision-Trace Control

## 1. 방어적 정확성의 누적을 별도 위험으로 본다
Reviewer 대응 과정에서 생긴 caveat는 하나씩 보면 타당해도 누적되면 본문을 망칠 수 있다.

위험 신호:
- 한 핵심 주장 뒤에 not X / does not imply Y / should not be interpreted as Z가 연속됨
- 같은 한계가 Introduction, Method, Results, Discussion에서 반복됨
- 핵심 결과보다 오해 방지 문장이 더 길어짐
- reviewer에게 답하기 위한 문장이 일반 독자에게는 왜 필요한지 설명되지 않음

원칙: claim first, boundary second.
이 원칙은 해석과 함의를 짧게 끝내라는 뜻이 아니다. 필요한 경계를 명확히 한 뒤 문헌 대조, 가능한 설명, 연구·현장 함의를 발전시킨다. 반복 방어와 실질적 설명을 구분한다.

## 2. Caveat budget을 둔다
한 개념에 대한 동일한 방어 문구는 주된 정의 위치에서 한 번 충분히 설명한다. 이후에는 짧은 참조만 사용한다.

## 3. 내부 검증 언어를 publication-facing 언어와 분리한다
audit, reconciliation, final lock, write-back, harmonization, correction step, baseline, previous/original file, superseded, flagged records, validation pass, net increase/decrease, version number는 내부 QA/Response에는 필요할 수 있으나 본문에는 자동으로 넣지 않는다.

## 4. Publication-context independence test
게재본 독자는 이전 투고본, reviewer comment, response letter, 이전 변수명, 분석 로그, QA 패키지, 수정 전 denominator를 모른다고 가정한다. 문장 이해에 이 중 하나가 필요하면 FAIL이다.

## 5. 과거 버전의 흔적이 용어에 남지 않게 한다
finalized, clarified rules, revised classification, retained specification, current selected file, corrected denominator 등의 대비대상이 독자에게 불명확하면 다시 쓴다.

## 6. positive definition을 exclusion보다 우선한다
실제 무엇인지 먼저 설명하고 예시를 준 뒤 필요한 제외규칙을 붙인다.

## 7. 말로 설명 테스트를 통과해야 한다
Methods 핵심 절차를 비전문 동료에게 2분 안에 구두로 설명해 본다. 구두 표현이 더 명확하면 논문을 그쪽으로 다시 쓴다.

## 8. Reviewer 지적의 방향과 제안 문장을 분리한다
불명확함·과도한 기술어·논리 연결 부족이라는 지적은 수용하되, reviewer 제안문이 데이터 범위를 넘으면 그대로 쓰지 않는다.

## 9. 경고어를 blacklist처럼 사용하지 않는다
final, revised, retained, corrected, baseline, current, previous, original, validation, audit 같은 단어 자체가 문제인 것은 아니다.

다음과 같은 표준 학술표현은 현재 논문 안에서 의미가 자족적이면 허용한다.
- primary analysis
- sensitivity analysis
- final analytic sample
- current study
- original scale item
- baseline measurement (실제 종단설계의 baseline)
- revised instrument (공식적으로 개정된 도구)

판정 기준은 단어가 아니라 문맥이다.

> 이 표현이 이전 버전·내부 QA·reviewer response를 알아야만 이해되는 대비를 만드는가?

그렇다면 revision trace다. 그렇지 않으면 기계적으로 삭제하지 않는다.

## 10. Publication-Prose Clean Pass와 연동
최종 제출 전 `rules/09_PUBLICATION_PROSE_CLEAN_PASS.md`를 별도 pass로 적용한다.

특히 DEFENSIVE / REVISION-TRACE / INTERNAL-QA 문제를 지적할 때에는 가능하면 실제 문장 또는 위치를 제시하고,
- 왜 일반 독자에게 불필요한지
- DELETE / SHORTEN / MOVE / REWRITE 중 어떤 조치가 필요한지
- publication-facing 대체문이 무엇인지
를 구체적으로 제시한다.

"방어적이다", "내부 검수 문구가 있다"는 인상평만으로 끝내지 않는다.
