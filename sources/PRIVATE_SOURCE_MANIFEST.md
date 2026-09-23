# Private Source Manifest

이 파일은 public repository에 원문을 넣지 않고도 각 case가 어떤 private evidence를 기반으로 하는지 추적하기 위한 manifest입니다.

| Case | Private source classes | Public repo status | Use in future QA |
|---|---|---|---|
| 2026-A | final anonymous manuscript/proof; editor decision; reviewer comments; revision response package | NOT COMMITTED | court-record / coding / terminology / revision-trace 문제가 있는 원고 검수 시 private source를 직접 대조 |
| 2026-B | blind-review manuscript; reject decision; reviewer comments | NOT COMMITTED | theory-RQ-analysis alignment / multilevel hierarchy / fragmented argument 문제가 있는 원고 검수 시 private source를 직접 대조 |

## Retrieval rule

새 검수에서 case가 relevant하면:
1. public case summary로 위험 패턴을 식별한다.
2. 사용자가 현재 Project/Conversation에 private source를 제공했는지 확인한다.
3. 제공되어 있으면 원문을 직접 읽고 실제 문장·구조와 reviewer 지적을 대조한다.
4. 제공되어 있지 않으면 case summary를 사실 근거로 과잉 일반화하지 않고, 필요한 원문을 사용자에게 요청한다.

## Non-substitution rule

Public case summary는 reviewer/editor correspondence의 대체물이 아니다.
정확한 판단에는 원문이 우선한다.
