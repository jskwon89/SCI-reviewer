# 05. Defensive Writing and Revision-Trace Control

## 1. 방어적 정확성의 누적을 별도 위험으로 본다
Reviewer 대응 과정에서 생긴 caveat는 하나씩 보면 타당해도 누적되면 본문을 망칠 수 있다.

위험 신호:
- 한 핵심 주장 뒤에 not X / does not imply Y / should not be interpreted as Z가 연속됨
- 같은 한계가 Introduction, Method, Results, Discussion에서 반복됨
- 핵심 결과보다 오해 방지 문장이 더 길어짐
- reviewer에게 답하기 위한 문장이 일반 독자에게는 왜 필요한지 설명되지 않음

원칙: claim first, boundary second.

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
