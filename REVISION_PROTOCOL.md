# SCI Reviser — Canonical Revision Protocol v0.8

## 0. Trigger

사용자가 다음처럼 요청하면 적용한다.

- "SCI-reviewer 기준으로 이 원고 수정해줘."
- "거절메일 반영해서 다음 투고용으로 고쳐줘."
- "R&R 의견 반영해줘."
- "이 버전 수정하되 과잉 재분석은 하지 마."

---

## 1. 수정 전: reviewer comment를 먼저 분류한다

각 comment를 다음 중 하나로 분류한다.

- STRUCTURE / CONTRIBUTION
- THEORY / RQ-H ALIGNMENT
- METHOD CLARITY
- ANALYSIS VALIDITY
- RESULTS INTERPRETATION
- WRITING / TERMINOLOGY
- REPORTING / FORMAT
- OPTIONAL / PREFERENCE

구조 문제를 wording 문제로 처리하지 않는다.

---

## 2. 수정 범위 잠금

각 comment마다:
1. 실제 문제
2. reviewer가 제안한 해결책
3. 데이터가 지지하는 해결책
4. 필요한 수정 범위
를 분리한다.

reviewer 제안 문장을 그대로 복사하지 않는다.

새 분석은 다음 경우에만:
- 핵심 결론의 타당성에 필요
- editor/reviewer가 명시적으로 요구
- 현재 주장에 필수

"확인 차원"의 재분석은 기본 금지한다.

---

## 3. Revision architecture

수정 전에 먼저:
- 중심 contribution
- primary RQ/H
- main analysis
- secondary boundary
- section outline
을 다시 확인한다.

중심 분석이 바뀌었으면 옛 theory/H/terminology를 제거한다.
새 구조 위에 옛 구조를 덧붙이지 않는다.

---

## 4. Revision-trace contamination 방지

수정자는 이전 버전과 QA history를 알고 있기 때문에 다음 표현을 자연스럽게 느낄 수 있다.

- final
- revised
- clarified
- retained
- corrected
- baseline
- harmonized
- current
- previous
- original
- validation/audit

그러나 publication-facing manuscript 독자는 그 역사를 모른다.

따라서 수정 후 모든 문장은:
**현재 연구 자체만으로 자족적으로 이해되는가?**
를 다시 점검한다.

Response letter에 필요한 revision history를 manuscript에 옮기지 않는다.

---

## 5. Defensive-writing contamination 방지

Reviewer 대응 중 가장 흔한 실패:

claim
→ not X
→ does not imply Y
→ should not be interpreted as Z
→ however...

이 패턴이 누적되면 manuscript가 response letter처럼 읽힌다.

원칙:
- CLAIM FIRST
- 필요한 boundary 한 번
- 반복 caveat 삭제
- 같은 한계를 여러 section에서 재설명하지 않음

---

## 6. Terminology migration check

수정 전/후 용어가 섞이지 않게 한다.

특히:
- old label + new label 혼재
- 분석코드 변수명 + publication term 혼재
- reviewer가 사용한 용어 + 저자 기존 용어 혼재
- 과거 denominator/범주 이름 흔적
을 점검한다.

하나의 개념에는 가능한 한 하나의 publication term만 쓴다.

---

## 7. Explanatory-depth development

Revision에서 단순히 문장을 추가하지 않는다.

구조 지적을 받았으면:
- 불필요한 theory/analysis를 삭제
- 확보한 공간을 conceptual bridge와 Discussion interpretation에 재배분
한다.

공간을 확보한 만큼만 설명을 보강한다는 뜻은 아니다. `rules/10_EXPLANATORY_DEPTH_AND_USEFULNESS.md`에 따라 이론·개념, 결과 해석, 문헌 대조, 기여와 연구·현장 함의를 근거가 허용하는 깊이까지 발전시킨다. 논리적으로 맞지만 설명이 덜 발전된 문단도 수정 대상이다.

임의의 단어 수·절 비율·최소 충족선을 적용하지 않는다. Methods의 내부 검수 설명이 논증을 밀어내지 않게 하되 재현성과 이해에 필요한 설명은 보존한다. 관찰된 근거·추론·제안을 구분하고 새 분석을 깊이의 대용물로 삼지 않는다.

---

## 8. AI-like revision style 방지

리비전은 특히 기계적 문체를 만들기 쉽다.

주의:
- reviewer comment마다 동일한 문장틀로 한 문장씩 추가
- 문단 끝마다 "These findings..." 추가
- caveat를 매 comment마다 삽입
- 같은 transition을 반복
- 동의어 치환으로만 수정 흔적을 가림

수정 후 반드시 전체 문서를 한 번에 읽고
문장별 수정 흔적이 아니라 **하나의 원고처럼 읽히는지** 확인한다.

---

## 9. Clean-reader test

최종 수정본은 이전 버전을 보지 않은 독자 기준으로 읽는다.

독자가 다음을 알아야 한다.
- 문제
- gap
- primary question
- sample
- method
- result
- contribution

이때 "왜 갑자기 이 말을 하지?"라는 문장이 있으면
revision history contamination 가능성을 우선 의심한다.

---

## 10. Publication-Prose Clean Pass

수정이 끝난 뒤 reviewer response와 이전 버전을 닫고 현재 manuscript만 다시 읽는다.
`rules/09_PUBLICATION_PROSE_CLEAN_PASS.md`와 `checklists/PUBLICATION_PROSE_CLEAN_PASS.md`를 적용한다.

반드시 다음을 확인한다.
- 문장이 연구 자체가 아니라 수정·검증 행위를 설명하지 않는가
- 필요한 boundary와 reviewer 선제 방어를 구분했는가
- 추상 주어가 실제 변수·집단·결과를 숨기지 않는가
- 동일한 rhetorical template가 여러 문단에 반복되지 않는가
- revision/QA 경고어를 기계적으로 삭제하지 않고 문맥으로 판정했는가

수정 순서:
DELETE redundancy/meta prose → CONCRETIZE subjects/results → DE-TEMPLATE rhetoric → DE-CONTAMINATE revision/QA history → BOUNDARY CHECK → AUTHOR VOICE/FIELD CALIBRATION.

이 pass에서 새 theory·새 robustness·새 분석을 방어 목적으로 추가하지 않는다.
DELETE는 설명의 실체까지 삭제하라는 뜻이 아니다. 개념 설명·문헌 대조·추론 연결·구체적 함의가 약해졌다면 복원하거나 더 명확하게 전개한다.

---

## 11. Final revision gate

제출 전:
- reviewer comment 대응 여부
- structure alignment
- terminology consistency
- no revision trace
- no excessive caveat
- explanatory depth / usefulness
- field norm
- author voice
- publication-prose clean pass
- numeric/reference consistency
를 확인한다.

이미 명료하고 해석과 함의가 풍부한 부분은 유지한다. 오류가 없다는 이유만으로 덜 발전된 설명을 완성된 것으로 판단하지 않는다.
