# 핵심 규칙 v1.0의 통합 근거

검토·작성일: 2026-11-10 (Asia/Seoul). 이 문서는 근거 기록이며 추가 의무 목록이 아니다. 현행 규칙은 [CORE_RULES.md](../CORE_RULES.md)이다.

## 1. 기존 규칙과 수정 대화에서 승계한 내용

통합 전 main은 `15d6e81dec0df4d74c747489831ee4b12185ffb4`였다. 이미 문체·과잉 방어·내부 작업언어·설명 깊이·구체적 결과·범위 통제 규칙이 있었다. 문제는 내용의 부재보다 14개 상세 규칙, 8개 체크리스트, 여러 Core 버전을 연결한 필수 읽기 구조에 있었다. 자동 진입점인 AGENTS.md도 없었다.

| 검토한 자료 종류 | 승계한 원칙 | 통합 위치 |
|---|---|---|
| 프로젝트 핵심·국영문 문체 규칙, 기존 rules/08–13 | 추상어로 결과를 대체하지 않음, 구체적 논증과 고찰, 내부 문구·기계적 반복·불필요한 방어 제거 | 핵심 §1–4 |
| 문서 편집·투고 QA·APA·분석별 작성 지침 | 목표 저널 요구, 문항·분모·용어·표·그림 정합성, 실제 파일과 서식 보존 | 핵심 §2, §5–7 |
| 수치재현성·리비전 범위통제·과잉 재검증 방지 지침 | 실제 자료와 코드 근거, 국소 수정, 확인 범위 표시, 필요한 검증 후 종료 | 핵심 §5–7, 편집·검토 절차 |
| 수정 대화에서 반복된 문제 유형 | 측정한 행동과 일반 개념 구별, 사실과 설계 이유 구별, 필요한 한계의 위치, 결과 수치와 비교 범위의 명료화 | 핵심 §3–5 |
| 기존 보고 양식 | 확인 결과를 과장하지 않음 | 핵심 §7. 매번 장문 QA 표를 출력하는 방식은 승계하지 않음 |

원고·심사서신·대화 원문·분석값은 이 기록에 싣지 않았다. 출판용 원고의 내부 문구 금지, 문장 연결용 세미콜론·엠대시 제한, 단독저자 자기지칭 제한은 프로젝트 편집 선호이며 모든 SSCI 저널의 규정이 아니다.

## 2. 실제 게재논문 전문 비교

아래 3편의 전문에서 관련 절과 표·그림을 읽었다. 주제와 독자층이 가까운 사례를 선정했으며, 이 표본으로 SSCI 전체의 평균 분량·보편 양식을 추정하지 않았다. 게재 사실이 논문의 모든 방법·문장을 그대로 따를 이유가 되지는 않는다. 출판사 조판 양식과 투고 원고 양식도 구별한다.

SSCI 수록 여부는 출판사의 공식 색인 목록에서 확인했다: [Sage의 JIV 소개](https://us.sagepub.com/hi/nam/journal/journal-interpersonal-violence), [APA의 American Psychologist 소개](https://www.apa.org/pubs/journals/amp/about). 개별 작업의 투고요건은 그때의 공식 지침으로 별도 확인한다.

### Storey, Pina, and Williams (2023)

Storey, J. E., Pina, A., & Williams, C. S. (2023). The impact of stalking and its predictors: Characterizing the needs of stalking victims. *Journal of Interpersonal Violence, 38*(21–22), 11569–11594. [DOI](https://doi.org/10.1177/08862605231185303) · [전문](https://pmc.ncbi.nlm.nih.gov/articles/PMC10515444/)

- 읽은 위치: Current Study, Method의 사례·자료·변수 구성, Results, Discussion과 임상적 함의.
- 관찰: 기존 지식의 측정·표본 공백에서 질문을 도출하고, 실제 포함 기준과 코딩을 기술한다. 결과의 선택적 수치 보고가 구체적 해석·한계·활용으로 이어진다.
- 반영: 서론의 질문 근거, Methods의 실제 처리, 결과와 고찰의 역할 구분. 이 논문에는 모형 진단이 상세히 보고되므로 ‘기술적 진단은 원고에서 없앤다’는 규칙을 도출하지 않았다.

### Taylor, Banyard, Grych, and Hamby (2019)

Taylor, E., Banyard, V., Grych, J., & Hamby, S. (2019). Not all behind closed doors: Examining bystander involvement in intimate partner violence. *Journal of Interpersonal Violence, 34*(18), 3915–3935. [DOI](https://doi.org/10.1177/0886260516673629) · [전문](https://lifepathsresearch.org/wp-content/uploads/2021/10/Not-all-behind-closed-doors-Taylor-Banyard-Hamby-Grych-2019.pdf)

- 읽은 위치: PDF 1–4쪽 서론·Current Study, 8–13쪽 결과·표 2–6, 12–16쪽 고찰·한계·함의(절이 같은 페이지에서 이어짐).
- 관찰: 주변인의 존재, 실제 개입, 도움·위해에 관한 평가를 구별한다. 표의 조건부 분석대상을 주에 밝히고, 고찰에서는 가능한 설명을 입증된 원인과 구별한다.
- 반영: 측정대상·행동·분모를 일관되게 유지하고, 설명을 늘리되 자료가 뒷받침하지 않는 기제로 단정하지 않는 원칙.

### Philpot, Liebst, Levine, Bernasco, and Lindegaard (2020)

Philpot, R., Liebst, L. S., Levine, M., Bernasco, W., & Lindegaard, M. R. (2020). Would I be helped? Cross-national CCTV footage shows that intervention is the norm in public conflicts. *American Psychologist, 75*(1), 66–75. [DOI](https://doi.org/10.1037/amp0000469) · [전문](https://research.vu.nl/ws/files/259918031/Would_I_Be_Helped_Cross_National_CCTV_Footage_Shows_That_Intervention_Is_the_Norm_in_Public_Conflicts.pdf)

- 읽은 위치: 저장소 표지 포함 PDF 2–4쪽 서론, 6쪽 결과·그림 2, 6–8쪽 고찰·한계.
- 관찰: 개인의 도움 확률과 사건에서 도움을 받을 확률의 차이를 질문에서 해석까지 유지한다. 그림 주는 모형·표본·구간·통제를 설명하며 본문은 핵심 결과를 중심으로 전개한다.
- 반영: 분석 단위와 추정 대상을 고정하고, 표·그림이 독립적으로 읽힐 만큼 설명하는 원칙. 이 논문에는 심사 중 추가된 분석을 밝히는 주도 있다. 따라서 ‘게재논문에는 심사 과정 언급이 전혀 없다’고 일반화하지 않았다.

전문을 확보하지 못한 문헌은 전문 비교 편수에 넣지 않았다. 문헌을 근거로 단어 수·인용 수·문단 수의 임의 통과선을 만들지 않았다.

## 3. 적용 구조와 검증 범위

- 현행 필수 읽기: CORE_RULES와 작업별 프로토콜 하나. 과거 상세 규칙·체크리스트·Project Knowledge는 참고·이력으로 전환했다.
- 실행상 통제: 실제 위반을 남기고 완료라고 보고하지 않는 G1–G5 관문. 국소 수정에 전체 재분석·전면 검수를 붙이지 않는다.
- 후보 검사 도구: 내부 문구, 반복, 자리표시자 등을 읽기 전용으로 찾는다. 정상 연구용어·필수 한계·독립적인 표 주를 자동 삭제하지 않는다. 합성 사례로 DOCX의 분할 run·표 읽기, 오탐 경계, 저자 옵션을 확인한다.
- 적용 한계: 규칙 문서나 AGENTS 진입점만으로 모든 AI의 준수를 보장할 수 없다. 도구가 규칙을 읽었는지와 실제 수정 결과를 확인해야 하며, 후보가 없다는 사실은 내용·인용·파일의 검증 완료가 아니다.
