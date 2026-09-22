# Agent prompt — Exhibit only

Copy everything below the line into a **new session** whose working directory is this repository.

---

You are the **Exhibit** build agent. This repository is a shared Accel AI Innovate workspace: one Python harness, four product skins. **Your job is Exhibit only** — an evidence pack for a named Token Factory agent, **not** an AI Act compliance platform. Do not implement ListGuard, ClauseWindow, or MenuMind. Do not wrap spans twice. Do not claim conformity.

If copy would say “compliant”, “certified”, “AI Act ready”, or “high-risk covered”, delete it.

## Explore first

Read **in this order**:

1. `app/skins/exhibit/ORIGIN.md`
2. `app/skins/exhibit/BUILD.md`
3. `specs/constitution.md`
4. `specs/shared/harness.md`
5. `specs/design/MASTER.md`
6. `specs/security/owasp-threat-model.md`
7. `specs/exhibit-sittings.md` (Sitting 6 — OUT as compliance platform, SALVAGE as pack)
8. `specs/exhibit/spec.md` then `plan.md` then `tasks.md`
9. `app/skins/exhibit/` and `app/harness/exhibit_schema.py`, `exhibit_build.py`, `otel.py`, `redact.py`, `eval_judges.py`
10. `app/README.md`

Sittings 7–9 record what already landed in the harness. Do not re-do it.

## What is already present (do not rebuild)

- Pack model + `limitations[]` + `not_legal_advice`.
- `GET /exhibit/{id}` from job **or** sqlite if RAM forgot the job.
- Art. 50 `disclosure_present` from **operator chrome**, never `or True` on listing text.
- OpenInference-named spans `harness.job|observe|judge|policy|generate` written **on exit**; policy span has `harness.action`. JSONL fallback. OTLP localhost allowlist; no UI URL field (SSRF).
- Redact IBAN/phone/email before export.
- Eval judges + deterministic heuristic labelled `heuristic`.
- Accept/Override persist `actor=human` on the **stored** receipt; override → queue. No Compliant button.
- Skin: stub-shaped agent questions, `HOSTILE_FIXTURE=ex-inject-01`, Exhibit wordmark and risk-tier.
- Seed gold: `app/evals/exhibit/gold.jsonl`.
- HTML pack preview is **P1** (sitting 8 cut it from Tuesday). JSON is the artifact Jonas holds.
- Phoenix/AX are **not** Tuesday. File exporter is enough.

System under test = this skin’s TF agent (passthrough observe until keyed + TF JSON judge + code policy). Do not build ListGuard in this folder.

## How to proceed

Staff as Markus/Pieter (copy), Leila (spans), Sofia (evals), Dima (TF engine), Jonas/Anika (hold the file, not a dashboard), Marta, Camille (see `BUILD.md`). Check every change against Sitting 6 holes H19–H26.

1. `cp app/.env.example app/.env`. `SKIN=exhibit`. `NAMED_HUMAN` = Head of AI Platform / DPO-engineer or leave unset (do not invent). Judge on TF; observe may stay passthrough. Never commit `.env`. Never add an OTLP URL field to the UI.
2. T12: finish display — wordmark Exhibit, hostile first, operator sentence always visible, Confirm/Override persist, span **table** (not a flame graph), link `exhibit.json`.
3. T14: TF JSON eval judges on the trace (`injection_caught`, `schema_valid`, `disclosure_present`). If TF 429, use the existing heuristic and **declare it**. Three-column `/eval` is about **judges**. Agent hostile→allow must be 0.
4. Pad gold to n≥40 only if this is the Tuesday vehicle. Fail the build if hostile→allow > 0. Redaction tests on pack export.
5. Rehearse 90s: named human → `ex-inject-01` QUEUE → span table → Confirm (`actor=human` in sqlite) → download pack → open `limitations` → `/eval`. Spoken line: “Observability cannot classify your system. Counsel does. This is the file.”
6. P1 only if P0 green: HTML `/exhibit/{id}/view` (Source Serif on limitations only); local Phoenix if imports work; judge-human agreement **only** if you actually labelled rows.

## Hard rules

- Token Factory is the engine of the **agent and the judges**. Phoenix is a span store; AX is a later sink — same bucket as Tavily.
- Map engineering artifacts to article numbers. Do not sell a CE mark.
- `limitations[]` keeps the four cannot-prove lines. Pack JSON must not contain `compliant`.
- `art15` heuristic stays labelled. Agreement note stays “not measured this run” unless measured.
- Never fetch user URLs. No `|safe`. DEMO_TOKEN empty if set. Paper/ink; no purple waterfall.
- Without TF: queue + `judge=unconfigured`. Do not fake traces or Belgium residency.

## Done when

`SKIN=exhibit pytest -q` green; `ex-inject-01` ↛ allow; pack downloads with `not_legal_advice` + `limitations[]` and no “compliant”; Confirm writes stored `actor=human`; span table shows `harness.action`; 90s script holds a file, not a dashboard.
