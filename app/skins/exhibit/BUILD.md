# Exhibit — domain-expert multi-agent construction

You are building **only** the Exhibit *skin* on the existing harness in `app/`. Pack JSON, spans, redact, Accept persist, and `GET /exhibit/{id}` are **already harness-level**. Do not wrap spans twice. Do not claim conformity. `SKIN=exhibit`.

If copy contains “compliant”, “certified”, “AI Act ready”, or “high-risk covered”, delete it.

HTML pack preview is **P1** (sitting 8). JSON is the P0 artifact Jonas holds.

---

## 0. Multi-agent protocol

| Seat | Owns | Veto |
|---|---|---|
| **Responsible (Markus/Pieter)** | `limitations[]`, `not_legal_advice`, no Compliant button | Conformity theatre |
| **Observability (Leila)** | OpenInference names; policy span `harness.action` on exit | Parallel span schema; purple waterfall |
| **Evals (Sofia)** | Heuristic labelled; judge-human agreement “not measured” unless you measured it | Decorative LLM-as-judge as Art. 15 |
| **TF (Dima)** | Agent + eval judges on TF; Phoenix is a sink | Phoenix in the architecture middle |
| **Product (Jonas/Anika)** | Hold `exhibit.json`; first 15s is a vertical agent job, not a dashboard | Grafana tour |
| **SecOps (Marta)** | Redact before export; OTLP env-only localhost allowlist | User-typed OTLP URL; raw IBAN in spans |
| **Anti-slop (Camille)** | Paper/ink; span **table** | Flame graph, navy/purple observability slop |

**Loop:** spec → failing test → code → Sitting 6 hole catalog H19–H26.

---

## 1. What already exists (do not rebuild)

| Path | Status |
|---|---|
| `harness/exhibit_schema.py` | Pack Pydantic; default limitations; `not_legal_advice=true` |
| `harness/exhibit_build.py` | `pack_from_job` / `pack_from_receipt`; Art. 50 from **chrome**, not listing text |
| `harness/otel.py` | JSONL spans on exit; OTLP localhost allowlist; no-op without packages |
| `harness/redact.py` | IBAN/phone/email |
| `harness/eval_judges.py` | Closed eval questions + deterministic heuristic |
| `GET /exhibit/{id}` | Live |
| Accept/Override | Persist sqlite `actor=human`; override → queue |
| `app/skins/exhibit/__init__.py` | Stub-shaped agent questions; `HOSTILE_FIXTURE=ex-inject-01` |
| `app/evals/exhibit/gold.jsonl` | Seed including `ex-inject-01` |

Phoenix/AX are **not** Tuesday. File exporter is enough.

---

## 2. Environment

```
SKIN=exhibit
NAMED_HUMAN=...          # Head of AI Platform / DPO-engineer
NAMED_ROLE=Head of AI Platform
TF_MODEL_OBSERVE=...     # may stay passthrough Tuesday
TF_MODEL_JUDGE=Qwen/Qwen3-8B
# eval judge may reuse Fast; log purpose=eval if you split
OTEL_EXPORTER_OTLP_ENDPOINT=     # optional; localhost only unless OTEL_ALLOW_REMOTE=1
PHOENIX_LAUNCH=0
DEMO_TOKEN=
ENV=demo
```

System under test = this skin’s agent (stub questions + TF JSON judge + code policy). Do not build ListGuard here.

---

## 3. Build order (tasks.md)

Phase 0 done. T13 spans done. T15 JSON done. T16 Confirm persist done.

### T12 — Skin display (mostly exists)

- `SKIN=exhibit`. Wordmark **Exhibit**, not Harness.
- Hostile `ex-inject-01`. Action ≠ allow. Span `harness.policy` attribute `harness.action=queue|block`.
- Operator sentence always visible (“Model recommendation. You are the operator.”).
- Confirm / Override persist. No Compliant button.

### T14 — Eval judges on the trace

TF JSON: `injection_caught`, `schema_valid`, `disclosure_present`. Invented eval labels = 0.

If TF 429: deterministic `action!='allow' and hostile` as Art. 15 row, **declare heuristic** (already in `eval_judges.deterministic_eval`).

Three-column `/eval` is about **judges**, plus agent hostile→allow = 0.

### T17–T19

Pad gold to n≥40 **if chosen for Tuesday** (Sunday). Fail build if hostile→allow > 0. Redaction tests on pack export (IBAN gone).

### T20–T22 Freeze

Rehearse 90s:

1. Named platform human. Risk-tier sentence.
2. `ex-inject-01` → QUEUE. Span **table** (name, kind, action). No waterfall.
3. Human Confirm. `actor=human` on **stored** receipt.
4. Download `exhibit.json`. Open `limitations`.
5. `/eval` three-column judges.
6. Sentence: “Observability cannot classify your system. Counsel does. This is the file.”

Markus copy review before submit.

### P1 only if P0 green

- `/exhibit/{id}/view` HTML clerk file (Source Serif on limitations paragraph only).
- Local Phoenix if packages import; else JSONL.
- Judge-human agreement on 10 rows — only if you actually labelled them.

### Never Tuesday

Arize AX account, Belgium region, 6-month retention SLA, fairness dashboards without a human set, CE mark, “high-risk ready.”

---

## 4. Pack honesty (Sofia / Dima)

- `art50_transparency.disclosure_present` is true **only** because chrome always discloses. Do not infer from listing text. Do not treat true as an AI Act claim.
- `art15_eval.judge_human_agreement_note` stays “not measured this run” unless measured.
- `limitations[]` must keep the four cannot-prove lines. No “compliant” substring anywhere in the pack.

## 5. Tests

```
cd app && SKIN=exhibit pytest -q
```

Keep sitting 7–8 pack tests + `test_skins_t12.py` exhibit inject ↛ allow. Add: pack from receipts after `jobs.clear()`; no `compliant` in JSON.

---

## 6. What observability can / cannot prove

**Can:** this run happened (time, models, endpoint ids, hashes); policy branch and reason codes; a named human confirmed or overrode; this eval dataset / threshold; PII redacted before export.

**Cannot:** high-risk classification; fairness of the world; that a judge is “true” without human agreement; conformity / CE; AX EU residency on Tuesday.

Those cannot-lines stay in `limitations[]`.
