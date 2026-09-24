# 08. AI-Like Style Risk and Author-Voice Calibration

## 0. 목적과 한계

이 규칙은 원고가 AI로 작성되었는지를 판정하지 않는다.
현재의 AI-detection 도구나 문체만으로 authorship를 신뢰성 있게 판별할 수 없으므로,
검수 대상은 **출처가 아니라 문체적 위험**이다.

즉 다음을 찾는다.

- 반복적이고 공식적인 문장 틀
- 과도한 signposting
- 의미 중복
- 지나치게 균일한 문장 리듬
- 추상어·명사화·하이픈 결합어의 누적
- 모든 주장에 caveat와 균형문을 붙이는 과도한 방어성
- 저자의 기존 논문과 현저히 다른 voice
- 사회과학 peer article보다 비정상적으로 '완벽하게 정돈된' 문단 패턴

목표는 인간처럼 보이게 위장하는 것이 아니라,
**자연스럽고 구체적이며 연구자 자신의 학술적 목소리로 읽히는 원고**를 만드는 것이다.

---

## 1. 세 가지 기준을 동시에 사용한다

### A. Manuscript-internal baseline
원고 내부에서 반복되는 어휘·문장틀·문단구조를 찾는다.

### B. Author-voice baseline
가능하면 저자가 직접 작성했고 출판된 1–3편을 비교 기준으로 사용한다.

비교:
- 문장 길이와 변동
- 연결어 사용
- 단락 전개 방식
- 결과를 해석하는 강도
- hedging 정도
- abstract / discussion의 밀도
- 자주 쓰는 자연스러운 표현

목적은 과거 문장을 복사하는 것이 아니라 **voice drift**를 찾는 것이다.

### C. Field/target-journal baseline
목표 저널의 최근 동종 논문과 비교해
원고가 지나치게 정형적·추상적·장황하거나 과도하게 압축되어 있지 않은지 본다.

---

## 2. AI-like style risk의 주요 패턴

### 2.1 반복되는 문장 시작
예:
- These findings...
- This study...
- This distinction...
- Taken together...
- In this context...
- Importantly...
- Notably...
- Accordingly...
- More broadly...

같은 section에서 동일/유사 opener가 3회 이상 반복되면 점검한다.
전문용어의 필수 반복은 제외한다.

### 2.2 반복되는 수사 구조
예:
- X is important because...
- X does not imply Y. Rather, ...
- Although X, Y...
- While X, Y...
- Not only X but also Y...
- This suggests that...
- These results highlight the importance of...

문장 자체가 틀렸다는 뜻이 아니라,
같은 rhetorical template가 반복되면 기계적 인상이 강해진다.

### 2.3 과도한 signposting
다음이 실제 논리 연결을 대신하는지 점검한다.
- importantly
- notably
- specifically
- in particular
- more broadly
- taken together
- accordingly
- therefore
- thus
- in this context

연결어를 삭제했을 때 문단 논리가 무너지면,
연결어가 아니라 underlying logic을 다시 써야 한다.

### 2.4 추상 명사와 nominalization
예:
- interpretation
- consideration
- differentiation
- contextualization
- operationalization
- positioning
- classification
- conceptualization

동사의 의미를 추상명사로 계속 바꾸면 문장이 비인칭적이고 AI-like하게 읽힐 수 있다.
가능하면 실제 행위자와 동사를 사용한다.

### 2.5 의미 없는 균형성과 대칭
AI-generated prose에서 자주 나타나는 위험:
- 모든 문단이 비슷한 길이
- 모든 문단이 claim → caveat → implication의 동일 순서
- 세 가지 항목을 반복적으로 병렬 제시
- 긍정/부정을 지나치게 대칭적으로 배치
- 각 결과마다 동일한 수의 장점·한계를 붙임

학술문장은 내용에 따라 비대칭적이어도 된다.

### 2.6 과도한 완결성
모든 문장이 자기완결적으로 배경·주장·한계를 동시에 담으려 하면
문장이 길고 방어적으로 된다.

한 문장이 한 가지 주요 기능을 수행하도록 한다.

### 2.7 중복 의미의 재서술
같은 주장이나 해석이:
- Abstract
- Introduction
- Results
- Discussion
- Conclusion
에서 거의 같은 문장으로 반복되는지 점검한다.

각 section은 기능이 다르므로 같은 사실도 다른 질문에 답해야 한다.

### 2.8 과잉 hedge / caveat
may, might, could, potentially, possibly, appears to, seems to,
does not necessarily, should not be interpreted as 등이 한 문단에 누적되는지 본다.

불확실성은 필요한 위치에서 한 번 명확히 표현한다.

### 2.9 과도한 generic praise/importance language
- important
- meaningful
- valuable
- critical
- significant contribution
- novel insight
- important implication

이런 표현 대신 무엇이 왜 중요한지 구체적으로 쓴다.

### 2.10 동어반복형 결론
예:
- These findings have important implications.
- These results underscore the importance of...
- Taken together, the findings suggest...
- Future research should further explore...

구체적 결과와 직접 연결되지 않으면 삭제 또는 구체화한다.

---

## 3. 정량적 보조 점검

정량값은 AI 판정 점수가 아니라 **문체 이상치 탐색용**이다.

가능하면 다음을 계산한다.

- 전체 및 section별 word count
- 평균 문장 길이와 표준편차
- 동일 sentence opener 빈도
- 3–6 word repeated phrase 빈도
- transition marker 빈도
- hedge marker 빈도
- abstract noun / nominalization 후보 빈도
- paragraph length 분포
- 동일한 paragraph skeleton의 연속 반복
- Abstract / Introduction / Discussion / Conclusion 간 문장 유사도

판정은 항상 author baseline과 peer baseline에 상대적으로 한다.

---

## 4. 수정 절차

### Pass 1 — Delete
먼저 삭제한다.
- 의미 중복
- generic signposting
- reviewer-response caveat
- 과도한 meta prose
- 결과 반복

### Pass 2 — Concretize
추상 주어를 실제 대상으로 바꾼다.

예:
`These findings demonstrate...`
→ 실제 관찰된 결과를 주어로 다시 쓴다.

### Pass 3 — De-template
같은 rhetorical frame이 반복되면
문장의 실제 기능에 따라 구조를 달리한다.
억지로 동의어를 바꾸지 않는다.

### Pass 4 — Restore author voice
저자의 기존 published writing과 비교하여
- 평소보다 지나치게 장황한가
- 지나치게 polished/abstract한가
- 평소보다 transition이 많은가
- 평소보다 hedge가 과한가
를 확인하고 자연스러운 수준으로 되돌린다.

### Pass 5 — Field calibration
최근 목표 저널 논문과 비교하여
문장 밀도와 section rhythm이 지나치게 이질적이지 않은지 확인한다.

---

## 5. 금지사항

AI-like style을 줄인다는 이유로:
- 일부러 문법을 어색하게 만들지 않는다.
- 비표준 영어를 삽입하지 않는다.
- 사실관계를 흐리지 않는다.
- citation을 삭제하지 않는다.
- 전문용어를 무조건 쉬운 말로 바꾸지 않는다.
- 문장을 랜덤하게 짧고 길게 섞지 않는다.
- detector를 속이기 위한 paraphrasing을 하지 않는다.

목표는 탐지 회피가 아니라 **좋은 사회과학 문체**다.

---

## 6. 최종 판정

다음을 각각 PASS / MINOR / MAJOR로 본다.

- REPETITION
- TEMPLATE-LIKE RHETORIC
- OVER-SIGNPOSTING
- ABSTRACT/NOMINAL STYLE
- DEFENSIVE/HEDGED STYLE
- AUTHOR-VOICE DRIFT
- FIELD-STYLE MISALIGNMENT

한 항목이 MAJOR이면 line editing 전에 해당 section의 구조를 먼저 점검한다.

---

## 7. Publication-prose contamination을 별도로 점검한다

기계적 문체 검수는 sentence opener 빈도나 hedge 수를 세는 데서 끝나지 않는다.

특히 다음을 별도 확인한다.
- reviewer comment에 답하려고 삽입한 문장이 본문에서 맥락 없이 튀는가
- "during revision", "to address this concern", "we additionally checked"처럼 수정 행위 자체가 주어가 되는가
- 추상 주어가 실제 변수·집단·결과를 숨기는가
- 모든 문단이 claim → caveat → implication의 같은 골격으로 정리되어 있는가
- 동의어만 바꿔 같은 rhetorical template를 반복하는가

판정은 반드시 실제 문장·문단과 연결한다.
단순 빈도는 이상치 탐색용일 뿐, DEFENSIVE / ABSTRACT / TEMPLATE 판정의 충분조건이 아니다.

최종 교정에서는 `rules/09_PUBLICATION_PROSE_CLEAN_PASS.md`와
`checklists/PUBLICATION_PROSE_CLEAN_PASS.md`를 함께 적용한다.

