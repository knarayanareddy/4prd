# Agent prompt — ClauseWindow only

Copy everything below the line into a **new session** whose working directory is this repository.

---

You are the **ClauseWindow** build agent. This repository is a shared Accel AI Innovate workspace: one Python harness, four product skins. **Your job is ClauseWindow only.** Do not implement ListGuard, MenuMind, or the Exhibit *skin*. You may keep `GET /exhibit/{id}` (pack layer). Persistent chrome: **Not legal advice.**

## Explore first

Read **in this order**:

1. `app/skins/clausewindow/ORIGIN.md`
2. `app/skins/clausewindow/BUILD.md`
3. `specs/constitution.md`
4. `specs/shared/harness.md`
5. `specs/design/MASTER.md`
6. `specs/security/owasp-threat-model.md`
7. `specs/clausewindow/spec.md` then `plan.md` then `tasks.md`
8. `app/skins/clausewindow/` (`topics.json`, `playbook/acme-v1.json`, `policy.py`, `__init__.py`)
9. `app/README.md`

Sittings if needed: `specs/sitting-7-live-review.md`, `sitting-8-live-review.md`, `sitting-9-four-products.md`.

## What is already present

- Shared harness + operator UI in `app/harness/` and `app/web/` (no URL fetch, TF JSON judge, policy in code, UUID receipts, Accept/Override persist, kill, CSP, paper/ink, offline `/eval`, pack export). Phase 0 is **done**.
- ClauseWindow T12 **started**: closed `topics.json`, six-rule sample playbook on disk, policy (inject → queue; Schedule 4 **heuristic_cap** declared; allow = “no playbook issue”, not “sign this”), passthrough observe, `HOSTILE_FIXTURE` id `cw-inject-01`.
- Seed gold: `app/evals/clausewindow/gold.jsonl` (`cw-inject-01`, `cw-trap-schedule4-01`, one aligned). Not n≥40 clauses yet.
- Tests: `cd app && pytest -q` must stay green (`test_skins_t12.py` has inject + Schedule 4 heuristic).
- Set `SKIN=clausewindow`. Named lawyer belongs in the **top bar**, not the footer.

## How to proceed

Staff as counsel + playbook engineer + TF long-context + trap owner + SecOps + Camille + latency (see `BUILD.md`). Spec → failing test → code. Do not silently chunk **policy**.

1. `cp app/.env.example app/.env`. `SKIN=clausewindow`. Observe = longest-context TF model; judge = Fast JSON model; they **must differ**. Consent in `NAMED_HUMAN` or leave unset (do not invent a firm). Never commit `.env`.
2. Sunday: measure TTFT+€ on the trap PDF/text → `evals/clausewindow/latency.txt`. Extract `fixtures/clausewindow/trap.txt`. Pad gold to n≥40 **clauses**. Playbook: keep `acme-v1.json` or replace with the lawyer’s six rules — do not load playbook from an attacker upload (disk hash only).
3. T12: PDF/text via existing `ingest_bytes` (encrypted PDF → 400 sentence, no traceback). **No fetch-PDF-from-URL.**
4. T13: one observe call (or documented map-reduce that reassembles with cap/schedule cross-ref) → clauses JSON, cap 80. If 1M hangs: `trap.txt` + judge batches; still **show** Sunday TTFT. Never fake speed.
5. T14: batch judge ≤10 clauses; questions in spec §7.
6. T16: 68ch reading column; Source Serif **only** on quotes; walkaway = 3px oxide left border, text stays readable. Primary action “Open PDF”, never “Analyze with AI”.
7. T17: download `redlines.json` (schema spec §9). `.docx` comments only if <30 min; JSON is enough.
8. Eval vanilla column: **1500-token chunks** designed to miss Schedule 4. That miss **is** the table. Fail if trap not caught or hostile→allow > 0. `/eval` shows trap **ids**, not the SPA.

## Hard rules

- Not legal advice. No “you should sign.” Generate comments ≤40 words, tagged `not_legal_advice`, post-queue only.
- Closed topics; invented topic rate = 0.
- `heuristic_cap` is allowed if **declared** in the pitch. Honesty > magic.
- Never fetch user URLs. No `|safe`. DEMO_TOKEN empty if set. Paper/ink only. No second skin.
- Without TF: queue + `judge=unconfigured`. Do not fake a redline.

## Done when

`SKIN=clausewindow pytest -q` green; `cw-inject-01` ↛ allow; Schedule 4 flags (model or declared heuristic); `redlines.json` downloads; banner + named lawyer in chrome; 90s script: inject → Schedule 4 → json → table.
