# SCI Author — Canonical Drafting Protocol v0.7

## 0. Trigger

사용자가 다음처럼 짧게 요청하면 이 프로토콜을 적용한다.

- "SCI-reviewer 기준으로 이 논문 작성해줘."
- "이 자료로 원고 초안 작성해줘. 목표 저널은 X."
- "이 분석결과로 Introduction/Discussion 작성해줘."
- "내 문체 기준으로 논문 작성해줘."

사용자는 reviewer 규칙을 다시 길게 입력할 필요가 없다.

---

## 1. 작성 전 설계

초안을 쓰기 전에 먼저 다음 7가지를 잠근다.

1. **Central contribution**  
   통계기법 이름 없이 한 문장으로 말할 수 있어야 한다.

2. **Target audience / journal**  
   목표 저널이 있으면 공식 가이드와 최근 동종 논문을 먼저 확인한다.

3. **Primary question / analysis**  
   main RQ/H와 main table/figure가 무엇인지 먼저 정한다.

4. **Secondary boundary**  
   secondary / exploratory / robustness 분석이 본문 중심을 침범하지 않게 범위를 정한다.

5. **Section functions**  
   Introduction, Method, Results, Discussion, Conclusion이 각각 어떤 질문에 답할지 정한다.

6. **Terminology plan**  
   자체 용어를 최소화하고, 꼭 필요한 용어는 평문 설명 후 도입한다.

7. **Word budget / depth target**  
   peer article의 section 비중을 참고해 분량을 설계한다. 고정 7–8천 단어를 목표로 하지 않는다.

---

## 2. Introduction 작성 규칙

권장 흐름:

1. 실제 substantive problem
2. 기존 연구가 무엇을 알고 있는가
3. 무엇을 아직 설명/구분하지 못하는가
4. 그 gap이 왜 중요한가
5. 현재 연구가 어떤 판단을 가능하게 하는가
6. RQ/H

금지:
- literature 나열만 하고 연결 논리를 생략
- "기존 연구가 이 분석을 안 했다"를 gap의 전부로 사용
- primary와 무관한 이론축 병렬 추가
- 뒤에서 정의할 개념을 먼저 사용
- 배경지식으로 word count를 채움

---

## 3. Method 작성 규칙

순서:
원자료 → 관측단위 → 포함/제외 → 중복/복수사건 처리 → 최종 표본 → 변수/코딩 → primary analysis.

원칙:
- 내부 분석 로그를 본문으로 옮기지 않는다.
- final/revised/retained/clarified 같은 revision-context 단어를 자동 사용하지 않는다.
- 복잡한 규칙에는 실제 예시를 둔다.
- 국내 제도/DB/표본단위는 해외 독자에게 설명한다.
- 정확성 방어용 caveat는 주 정의 위치에서 한 번 충분히 쓴다.

---

## 4. Results 작성 규칙

Results는 표를 읽어주는 절이 아니다.

각 핵심 결과는 가능하면:
1. 무엇을 비교했는가
2. 가장 중요한 패턴은 무엇인가
3. 예상과 일치/불일치하는가
4. secondary result가 primary conclusion을 바꾸는가
를 평문으로 설명한다.

표의 모든 숫자를 본문에서 반복하지 않는다.

---

## 5. Discussion 작성 규칙

각 primary finding에 대해 다음을 검토한다.

1. What was found?
2. Closest literature와 어떻게 같은가/다른가?
3. 가능한 설명 또는 alternative explanation은 무엇인가?
4. 어떤 해석은 데이터가 허용하지 않는가?
5. theory / measurement / research design / practice에서 무엇이 달라지는가?

Discussion이 짧아질 때 가장 먼저 literature comparison과 substantive interpretation이 빠지는지 확인한다.

---

## 6. Conclusion 작성 규칙

Conclusion은 abstract의 마지막 문장 복사가 아니다.

최소 기능:
- 연구가 해결한 문제
- 가장 중요한 empirical answer
- 기존 지식/측정/실무에서 달라지는 점
- 필요시 핵심 한계와 다음 연구 방향

---

## 7. AI-like style / author voice 방지

작성 중 다음을 자동 점검한다.

- 동일 sentence opener 반복
- This study / These findings / Taken together / Importantly / Notably 남발
- 동일 rhetorical template 반복
- 지나친 nominalization
- 추상 주어
- may/might/could/potentially 누적
- 모든 paragraph가 같은 길이·구조
- claim → caveat → implication의 기계적 반복
- generic importance language
- Abstract/Intro/Discussion/Conclusion 문장 재사용

가능하면 저자의 기존 출판 논문 1–3편을 author-voice baseline으로 사용한다.

수정 목표는 AI detection 회피가 아니라:
**구체적이고 자연스럽고 해당 저자와 학문분야에 맞는 문체**다.

---

## 8. 작성 중 과잉 방지

다음은 기본 금지:
- 분량을 채우기 위한 새 분석
- 분량을 채우기 위한 새 이론
- 모든 가능한 caveat 삽입
- 내부 QA detail의 publication prose 편입
- reviewer를 미리 방어하려는 과도한 문장
- Supplement에 모든 검증을 밀어넣기

---

## 9. Publication-Prose Clean Pass

초안이 완성되면 `rules/09_PUBLICATION_PROSE_CLEAN_PASS.md`와
`checklists/PUBLICATION_PROSE_CLEAN_PASS.md`를 적용한다.

특히:
- 연구 자체가 아니라 작성·검수 과정을 설명하는 meta prose를 제거한다.
- claim 뒤에는 필요한 boundary만 한 번 남긴다.
- 추상 주어를 실제 변수·집단·비교·결과로 구체화한다.
- 동일 opener/transition/claim→caveat→implication 구조가 반복되면 문단 기능에 맞게 다시 쓴다.
- final/revised/current/baseline 같은 단어는 blacklist로 삭제하지 않고 문맥상 revision trace인지 판단한다.

문체 문제를 고칠 때 의미·수치·인용·분석 범위를 바꾸지 않는다.

---

## 10. Draft Completion Gate

초안 완성 전 반드시 확인:

- contribution 한 문장 가능
- section alignment
- primary/secondary hierarchy
- reader-first terminology
- section depth
- author voice
- field norm
- publication-context independence
- publication-prose clean pass

하나라도 MAJOR이면 문장 polishing보다 구조 수정을 먼저 한다.
