# Exhibit — Tasks (Supercharged Edition)

Execute in sequential order. Phase 0 is already validated in `app/`.

---

## Phase 0: Base Harness & Constitutional Law (Completed)
- [x] **T01** Shared SQLite receipts store with `actor=human` sign-off.
- [x] **T02** OpenTelemetry span collector emitting to `spans.jsonl`.
- [x] **T03** Pricing engine calculating token costs in Euros (`prices.py`).
- [x] **T04** 71/71 passing unit tests in `app/tests/`.

---

## Phase 1: Span Ingestion & TF Eval Judge
- [ ] **T05** Configure `app/.env` with live Nebius Token Factory credentials:
  - `TF_MODEL_JUDGE=Qwen/Qwen3-8B`
- [ ] **T06** Implement OpenInference trace parser in `observe()` reading directly from `spans.jsonl`.
- [ ] **T07** Implement Tavily harmonized standards lookup for EU AI Act Annex IV technical documentation templates.
- [ ] **T08** Connect `Qwen3-8B` to score trace robustness and disclosure compliance via strict JSON schema.

---

## Phase 2: Decoupled Policy & FlowGraph DAG
- [ ] **T09** Enforce strict governance rules in `app/skins/exhibit/policy.py`:
  - Disallow any automated "Compliant" certificate stamp.
  - Require signed human reviewer record before compiling the final pack.
- [ ] **T10** Wire `FlowGraph` DAG state machine in `pipeline.py` to record transitions: `span_ingest` $\rightarrow$ `tf_eval` $\rightarrow$ `human_signoff` $\rightarrow$ `pack_compiled`.
- [ ] **T11** Implement `exhibit_build.py` pack compiler to output statutory article sections (12, 14, 15).

---

## Phase 3: Lovable UI & Operator Console
- [ ] **T12** Update `app/web/templates/home.html` and Lovable React client:
  - Add dark slate compliance dashboard with Article 12, 14, and 15 readiness cards.
  - Display human reviewer verification drawer.
  - Implement 1-click download for `exhibit.json`.

---

## Phase 4: Comparative Benchmarks & Eval Table
- [ ] **T13** Run all fixtures in `app/evals/exhibit/gold.jsonl` against Nebius Token Factory.
- [ ] **T14** Verify that `ex-inject-01` produces a valid trace with `injection_caught=True`.
- [ ] **T15** Verify that `GET /exhibit/{job_id}` returns a fully validated JSON schema conforming to EU AI Act documentation rules.
