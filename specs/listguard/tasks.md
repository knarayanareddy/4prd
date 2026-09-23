# ListGuard — Tasks (Supercharged Edition)

Execute in sequential order. Phase 0 is already validated in `app/`.

---

## Phase 0: Base Harness & Constitutional Law (Completed)
- [x] **T01** Shared SQLite receipts store with `actor=human` sign-off.
- [x] **T02** OpenTelemetry span collector emitting to `spans.jsonl`.
- [x] **T03** Pricing engine calculating token costs in Euros (`prices.py`).
- [x] **T04** 71/71 passing unit tests in `app/tests/`.

---

## Phase 1: Ingestion, Compaction & Token Factory Engine
- [ ] **T05** Configure `app/.env` with live Nebius Token Factory credentials:
  - `TF_MODEL_OBSERVE=Qwen/Qwen3-VL-30B-A3B`
  - `TF_MODEL_JUDGE=Qwen/Qwen3-8B`
- [ ] **T06** Wire `WinnowCompactor` into `app/skins/listguard/__init__.py` inside `observe()` to compress listing descriptions.
- [ ] **T07** Implement Tavily brand/serial number lookup in `observe()` for high-value watches and electronics.
- [ ] **T08** Connect `Qwen3-8B` to score policy buckets via strict JSON schema questions (`questions()`).

---

## Phase 2: Decoupled Policy & FlowGraph DAG
- [ ] **T09** Enforce strict DSA rules in `app/skins/listguard/policy.py`:
  - `weapon`, `animal`, `other_illegal` $\rightarrow$ `Action.block` (listing only).
  - `injection_or_jailbreak` $\ge 0.5$ $\rightarrow$ `Action.queue`.
  - Disallow any automated mutation on seller accounts.
- [ ] **T10** Wire `FlowGraph` DAG state machine in `pipeline.py` to record transitions: `intake` $\rightarrow$ `vl_scan` $\rightarrow$ `tf_judge` $\rightarrow$ `policy_route` $\rightarrow$ `receipt_persisted`.
- [ ] **T11** Implement `infra_circuit_breaker.py` to automatically divert traffic to queue if inference latency exceeds 800ms.

---

## Phase 3: Lovable UI & Operator Console
- [ ] **T12** Update `app/web/templates/home.html` and Lovable React client:
  - Add dark slate moderator card with keyboard shortcuts (`A` = Accept, `O` = Override).
  - Display policy bucket badge (Red for `block`, Amber for `queue`, Green for `allow`).
  - Embed live Mermaid state diagram visualizer (`agent-flow --mermaid`).

---

## Phase 4: Comparative Benchmarks & Eval Table
- [ ] **T13** Run all gold fixtures in `app/evals/listguard/gold.jsonl` against Nebius Token Factory and GPT-4o.
- [ ] **T14** Verify that `lg-inject-01` produces 0% allow recommendations.
- [ ] **T15** Verify that `/eval` renders the 3-column comparative benchmark table proving 26× cost reduction and sub-80ms p50 latency.
