# SCI Author — Canonical Drafting Protocol v0.9

## 초안부터 적용하는 필수 서술 원칙

**관찰된 결과는 더 분명하게 주장하고, 가능한 설명은 근거를 붙여 발전시키며, 측정상 한계는 필요한 위치에 모은다. 핵심 결과는 실제 집단·측정·비교 방향으로 쓰고, 주변 내용은 간단히 언급하거나 제외한다.**

초안 전에 핵심 결과·설명 근거·한계 위치를 정하고 작성 중 바로 적용한다. 사후 검수로 미루지 않는다. `rules/13_CONCRETE_FINDINGS_AND_GROUNDED_INTERPRETATION.md`를 반드시 적용한다. “일치하지 않는다”, “복잡한 양상이다” 같은 추상 요약으로 직접 서술 가능한 결과를 대체하지 않는다. 명료한 주장과 근거 없는 과장을 구분한다. 중요도에 따른 설명 배분과 완료 판정은 해당 규칙 5–7절을 따른다.

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

7. **Explanatory depth / usefulness**
   이론·개념, 결과 해석, 문헌 대조, 기여와 활용 가능성을 어떻게 발전시킬지 설계한다. 임의의 단어 수·절 비율·최소 충족선으로 설명을 제한하지 않는다. 실제 저널 제한과 사용자 범위는 지킨다.

---

## 2. Introduction 작성 규칙

권장 흐름:

1. 실제 substantive problem
2. 기존 연구가 무엇을 알고 있는가
3. 무엇을 아직 설명/구분하지 못하는가
4. 그 gap이 왜 중요한가
5. 현재 연구가 어떤 판단을 가능하게 하는가
6. RQ/H

`rules/10` 2.1절에 따라 기존 문헌이 밝힌 내용과 남은 질문을 연결하여 연구의 필요성을 구체화한다. 맥락 설명은 3.2절에 따라 그 질문을 이해하는 데 어떤 역할을 하는지 드러낸다.

이론과 개념은 이름을 소개하는 데 그치지 않고 어떤 관계를 예상하게 하며 현재 측정·분석과 어떻게 연결되는지 설명한다. 독자가 결과를 해석할 기반을 마련하되 연구질문과 무관한 이론축을 늘리지 않는다.

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
4. 결과가 적용되는 대상·시점·측정 범위를 긍정문으로 어디에 한 번 쓰는가? (`rules/12`)
5. theory / measurement / research design / practice에서 무엇이 달라지는가?

`rules/10` 3.1–3.2절에 따라 문헌 대조와 맥락을 사용해 결과가 뜻하는 현상과 가능한 과정을 설명한다. 결과 요약에 인용을 붙이는 것으로 이 기능을 대신하지 않는다.

Discussion이 짧아질 때 가장 먼저 literature comparison과 substantive interpretation이 빠지는지 확인한다.

논리적으로 맞는 결과 요약에서 멈추지 않는다. `rules/10_EXPLANATORY_DEPTH_AND_USEFULNESS.md`에 따라 결과의 의미, 가까운 문헌과 다른 이유, 가능한 설명과 대안, 기존 지식에서 달라지는 점을 풍부하게 발전시킨다. 후속 연구의 질문·측정·설계와 현장·지역사회의 판단에 무엇을 제안할 수 있는지 구체화한다. 관찰된 근거, 이론적 추론, 적용 제안은 구분하며 문단마다 동일한 설명 틀을 강제하지 않는다.

---

## 6. Conclusion 작성 규칙

Conclusion은 abstract의 마지막 문장 복사가 아니다.

전개할 기능:
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
중복을 줄이면서 개념 설명, 추론의 연결 고리, 문헌 대조, 예시, 함의를 삭제하지 않았는지 확인한다. 압축 때문에 결과의 의미나 활용을 독자가 메워야 한다면 설명을 복원하거나 발전시킨다.

---

## 10. Draft Completion Gate

초안 완성 전 반드시 확인:

- contribution 한 문장 가능
- section alignment
- primary/secondary hierarchy
- reader-first terminology
- explanatory depth / usefulness
- author voice
- field norm
- publication-context independence
- publication-prose clean pass

하나라도 MAJOR이면 문장 polishing보다 구조 수정을 먼저 한다.

## 필수 설명 완성도 판정 (v0.9)

`rules/10_EXPLANATORY_DEPTH_AND_USEFULNESS.md` 8절을 적용한다. 전체 작성·내용 보완·전체 검토에서는 먼저 중요한 설명 과제와 근거를 식별하고, 완료 시 최종 원고 위치와 실제로 완성된 추론을 제시한다. 항목 언급·문장 추가·수치 검증만으로 깊이를 PASS 처리하지 않는다. 승인된 내용 보완 범위의 중요한 설명 생략은 해결하고, 확인 불가·범위 밖은 구분한다.

목표 저널 적합성을 판단할 때는 `rules/06_FIELD_NORM_AND_PEER_BENCHMARK.md` 6절에 따라 실제 전문 비교 범위와 결론을 맞춘다. 분량 목표로 완성을 대체하지 않는다. 제한 교정이나 R&R 범위를 자동 확대하지 않는다.
