# v2.1 — 2026-11-10: 의무 적용 명시

- START_HERE.md를 어떤 표현(‘읽고’, ‘참고해서’, ‘기준으로’)으로 가리키든 의무 기준으로 적용하도록 명시. 적용하지 못한 조항은 사용자에게 보고.
- 사용자의 명시적 지시와 충돌하는 항목만 사용자 지시를 따르고 나머지는 그대로 적용.

---

# v2.0 — 2026-11-10: 단일 파일 기준본

- 핵심 규칙과 세 절차(초기 작성 / 투고 전 리뷰 / R&R 대응)의 전문을 START_HERE.md 한 파일로 통합. 이 파일 하나만 읽으면 작업할 수 있음.
- CORE_RULES.md와 세 프로토콜 파일은 과거 링크 유지를 위한 안내 파일로 전환. 규칙 수정은 START_HERE.md에서만 함.
- 규칙 내용은 v1.2에서 바꾸지 않음. AGENTS, README, SHORT_PROMPTS의 안내를 맞춤.

---

# v1.2 — 2026-11-10: 이전 작업 잔여물 전면 금지

- CORE_RULES §1에 ‘이전 작업의 잔여물’ 금지를 추가하고 G3 관문에 반영. 요청 범위와 무관하게 원고 전체에 적용.
- R&R 대응 절차: 잔여물 제거를 범위 제한의 유일한 예외로 명시하고, 제거한 문장을 작업 보고에 적도록 함.
- 문헌 확인 수준과 게재논문 확인 여부는 사용자에게 하는 작업 보고에만 적고 원고·응답서에는 쓰지 않음을 명시.

---

# v1.1 — 2026-11-10: 상황별 절차 구분

- START_HERE의 진입 경로를 초기 작성 / 투고 전 자체 리뷰 / 심사의견(R&R) 대응으로 구분. 공통 금지와 완료 관문은 CORE_RULES 하나로 유지.
- REVISION_PROTOCOL을 R&R 대응 절차로 재작성: 심사위원이 언급한 부분만 수정, 문단 이동 전 중복 확인, 심사위원에게 답하는 문장은 응답서에만 작성, 추가 문단의 근거와 목표 저널 게재논문 확인, 응답서 작성 기준. 기존의 범위 통제·파일 보존·검증·종료 조항은 유지.
- 심사의견 없는 편집은 R&R 대응 절차를 사용. 리뷰 결과에 따른 수정도 R&R 대응 절차로 넘김.
- START_HERE에 핵심 금지 세 가지 요약과 별도 프로젝트 지침이 있을 때의 우선순위를 추가.
- AUTHOR·REVIEW 절차에 적용 범위 한 줄 추가. AGENTS, README, SHORT_PROMPTS의 명칭을 맞춤.

---

# v1.0 — 2026-11-10: 필수 규칙 단일화

- 기준 main: `15d6e81dec0df4d74c747489831ee4b12185ffb4` (2026-10-08, KST).
- 기존 작성·문체·설명 깊이 원칙을 CORE_RULES 하나로 통합. AGENTS 진입점과 작업별 짧은 절차로 적용.
- rules/checklists/과거 Project Knowledge는 참고·이력으로 명시. 전체 필수 재독 폐지.
- 내부 검수문구·불필요한 방어·기계적 반복 금지, 필수 한계·재현정보 보존, 실제 확인 범위에 맞는 완료 관문.
- 게재논문 3편 전문의 구조·측정·표·해석을 검토하고 관찰/프로젝트 선호/일반화 한계를 별도 기록.
- 로컬 후보 검사 도구와 합성 사례 테스트 추가. AI 탐지·원고 품질 인증 도구가 아님.
- 비공개 원고·심사서신·분석값·논문 PDF는 추가하지 않음.

---

# Changelog

## Concrete findings and grounded interpretation — 2026-10-08
- Required direct, specific statements of observed findings, evidence-grounded explanations, and functional placement of measurement limitations in initial drafting, revision, and review.
- Added rules/13 with concrete comparison guidance, safeguards for estimands and uncertainty, importance-based development/brief mention/deletion, and manuscript-level completion criteria.
- Strengthened the existing AUTHOR_PROTOCOL instead of creating a duplicate authoring manual; connected all three protocols, entry point, Core, README, prompts, and drafting/clean-pass checks.
- Clarified rules/12 so essential denominators and measurement definitions remain visible, limitations are not forced into one paragraph, and necessary standalone scope labels are allowed.
- Used only generalized writing examples; no unpublished manuscript results or confidential source text were added.

## Concrete rationale, explanatory discussion, and contextual grounding — 2026-10-07
- Made three writing and review functions explicit in rules/10: constructing the study rationale, explaining findings in Discussion, and connecting contextual evidence to the question or interpretation.
- Added writing guidance, evidence-based completion criteria, and recognizable omissions; linked these criteria from both protocols and the explanatory-depth checklist.
- Preserved scope controls: no reference quotas, fixed paragraph templates, additional analyses, or defensive prose requirements.

## Positive scope writing — 2026-10-07
- Added `rules/12_POSITIVE_SCOPE_WRITING.md`: state the scope of findings positively (who, when, which measure) instead of negative boundary sentences, with section placement rules, conversion examples, and a post-draft search list.
- Replaced "which interpretations do the data not allow?" in the review and authoring protocols with a positive scope question.
- Rewrote the boundary column in `rules/10` section 4 as sentence-strength guidance so it is not copied into manuscripts as negation.
- Linked the rule from START_HERE, README, rules/05, and the drafting and clean-pass checklists.

## v0.9 — 2026-10-06
- Made explanatory-depth planning and evidence-based completion mandatory for full drafting, substantive revision, and whole-manuscript review.
- Required manuscript locations and completed reasoning, rather than mentions, additions, or successful numeric checks, to support depth judgments.
- Separated analytical correctness, explanatory development, and journal alignment; unresolved substantive gaps cannot receive a depth PASS.
- Required peer-comparison claims to match actual full-text access and comparable counting scope; prohibited journal-average claims from small examples and length-based completion decisions.
- Preserved scope limits and stopping rules: no fixed word targets, new analyses, paper quotas, or repeated review loops.
- Routed the gate through START_HERE, all three protocols, relevant checklists, README, and Core v0.9; retained earlier Core versions as history.

## Submission-document rules — 2026-09-26
- Defined concise title-page and cover-letter scope, excluding unnecessary internal QA, defensive explanations, and repeated declarations.
- Prohibited unapproved promises to share code/materials, deposit in repositories, or provide data upon request; secondary-data statements identify the original provider and actual access conditions.
- Added a factual AI-use template for submission-file preparation/checking, English translation, and language editing, without automatically expanding the declared role to drafting manuscript content.
- Linked `rules/11_SUBMISSION_DOCUMENTS_AND_DECLARATIONS.md` from the common entry point and rule index.

## v0.8 — 2026-09-24
- Added explanatory depth and usefulness as a positive authoring, revision, and review objective beyond logical validity and concise prose.
- Required theory and concept explanations, direct literature comparisons, interpretation, contribution, and research/community implications to develop the warranted meaning and use of findings.
- Distinguished observed evidence, theoretical inference, and proposed applications without adding repetitive labels or caveats to publication prose.
- Integrated explanatory-substance preservation into the prose clean pass: deleting repetition must not delete conceptual explanation, inferential links, examples, or substantive implications.
- Removed arbitrary word/section/paragraph targets and minimum-sufficiency framing from active depth guidance; actual journal limits and user scope still apply.
- Made peer comparison responsive to the task rather than a fixed paper quota; depth development does not require new analyses, additional theories, or repeated verification cycles.
- Added `rules/10_EXPLANATORY_DEPTH_AND_USEFULNESS.md`, its checklist, and Core v0.8; aligned the author, reviser, reviewer, and related checklists.

## v0.7 — 2026-09-24
- Added mandatory Publication-Prose Clean Pass for authoring, revision, and independent review.
- Added sentence-purpose test to separate research explanation from revision/QA/reviewer-response history.
- Added explicit distinction between necessary epistemic boundaries and pre-emptive defensive caveats.
- Added abstract-to-concrete and mechanical-template checks for vague subjects, nominalization, repeated rhetorical frames, and uniform paragraph skeletons.
- Added contextual exception rule so words such as final, current, primary, sensitivity, and baseline are not treated as automatic blacklist terms.
- Required sentence-level evidence and concrete DELETE / SHORTEN / MOVE / REWRITE actions when defensive, abstract, template-like, revision-trace, or internal-QA prose is flagged.
- Added `rules/09_PUBLICATION_PROSE_CLEAN_PASS.md`, `checklists/PUBLICATION_PROSE_CLEAN_PASS.md`, and Core v0.7.


## v0.3.1 — 2026-09-23
- Public repository baseline initialized.
- Added argument architecture, reader-first terminology, Methods clarity, analysis hierarchy, defensive-writing/revision-trace, and field-norm rules.
- Added pre-submission, naive-reader, and field-benchmark checklists.
- Added two public-safe generalized reviewer-failure case records.
- Added explicit policy not to commit raw unpublished manuscripts or confidential reviewer/editor correspondence to the public repository.
