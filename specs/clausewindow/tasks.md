# ClauseWindow — Tasks (Supercharged Edition)

Execute in sequential order. Phase 0 is already validated in `app/`.

---

## Phase 0: Base Harness & Constitutional Law (Completed)
- [x] **T01** Shared SQLite receipts store with `actor=human` sign-off.
- [x] **T02** OpenTelemetry span collector emitting to `spans.jsonl`.
- [x] **T03** Pricing engine calculating token costs in Euros (`prices.py`).
- [x] **T04** 71/71 passing unit tests in `app/tests/`.

---

## Phase 1: Ingestion & 1M-Context Engine
- [ ] **T05** Configure `app/.env` with live Nebius Token Factory credentials:
  - `TF_MODEL_OBSERVE=THUDM/glm-5.3-flash`
  - `TF_MODEL_JUDGE=Qwen/Qwen3-8B`
- [ ] **T06** Implement monolithic PDF ingestion in `observe()` using `pypdf` with zero text chunking.
- [ ] **T07** Implement Tavily EUR-Lex regulatory lookup for Standard Contractual Clauses (SCCs).
- [ ] **T08** Connect `Qwen3-8B` to score playbook deviations via strict JSON schema questions (`questions()`).

---

## Phase 2: Decoupled Policy & FlowGraph DAG
- [ ] **T09** Enforce strict playbook rules in `app/skins/clausewindow/policy.py`:
  - Uncapped liability or Schedule 4 breach $\rightarrow$ `Action.queue` with reason `playbook_walkaway`.
  - Disallow any automated "you should sign" recommendations.
- [ ] **T10** Wire `FlowGraph` DAG state machine in `pipeline.py` to record transitions: `pdf_intake` $\rightarrow$ `1m_pass` $\rightarrow$ `playbook_audit` $\rightarrow$ `redline_generated`.
- [ ] **T11** Implement `pattern_store.py` to cache approved corporate playbooks and past deviation limits.

---

## Phase 3: Lovable UI & Operator Console
- [ ] **T12** Update `app/web/templates/home.html` and Lovable React client:
  - Add dark slate contract heatmap viewer (Green for aligned, Amber for variance, Red for walk-away).
  - Anchor "Decision Support. Not Legal Advice" banner permanently in header chrome.
  - Implement 1-click download for `redlines.json`.

---

## Phase 4: Comparative Benchmarks & Eval Table
- [ ] **T13** Run all fixtures in `app/evals/clausewindow/gold.jsonl` against Nebius Token Factory and chunked GPT-4o RAG.
- [ ] **T14** Verify that `cw-trap-schedule4-01` produces 100% trap recall on Token Factory vs. <25% on chunked RAG.
- [ ] **T15** Verify that `/eval` renders the comparative benchmark table demonstrating whole-document accuracy advantage.
