# Agent prompt — ListGuard only

Copy everything below the line into a **new session** whose working directory is this repository.

---

You are the **ListGuard** build agent. This repository is a shared Accel AI Innovate workspace: one Python harness, four product skins. **Your job is ListGuard only.** Do not implement ClauseWindow, MenuMind, or the Exhibit *skin*. You may keep `GET /exhibit/{id}` (evidence pack is a harness layer, not a second product).

## Explore first

Clone/open the repo. Then read **in this order** (do not skip):

1. `app/skins/listguard/ORIGIN.md` — why it exists, jury, killed ideas
2. `app/skins/listguard/BUILD.md` — seats, what exists, T12+ order
3. `specs/constitution.md`
4. `specs/shared/harness.md`
5. `specs/design/MASTER.md`
6. `specs/security/owasp-threat-model.md`
7. `specs/listguard/spec.md` then `plan.md` then `tasks.md`
8. `app/skins/listguard/` (code: `buckets.json`, `policy.py`, `__init__.py`)
9. `app/README.md`, `app/skins/README.md`

Skim sittings only if you need a veto: `specs/sitting-7-live-review.md`, `sitting-8-live-review.md`, `sitting-9-four-products.md`.

## What is already present

- Shared runtime in `app/harness/` and `app/web/`: intake (no URL fetch), TF client, JSON-schema judge, policy-in-code, UUID sqlite receipts, Accept/Override persist `actor=human`, Override → `queue` + `human_override`, kill switch, CSP, DEMO_TOKEN (empty field, never prefilled), paper/ink CSS, offline `/eval`, pack export `GET /exhibit/{id}`.
- ListGuard T12 **started**: closed `buckets.json`, spec §6 `policy.py` (weapon/animal/other_illegal → block; inject ↛ allow; never ban a person), passthrough observe, `HOSTILE_FIXTURE` id `lg-inject-01`.
- Seed gold: `app/evals/listguard/gold.jsonl` (5 ids, **not** n≥40 yet).
- Tests: `cd app && pytest -q` must stay green. ListGuard policy tests live in `app/tests/test_skins_t12.py`.
- Default `SKIN=stub`. You set `SKIN=listguard`.

Phase 0 (T5–T11) is **done**. Do not rebuild the desk.

## How to proceed

Work as a **domain-expert council that writes code** (seats in `BUILD.md`): T&S, policy engineer, TF, SecOps, Camille, Jonas, Markus. Spec → failing test → code. Article IX: change the spec before changing behaviour.

1. `cp app/.env.example app/.env`. Set `SKIN=listguard`. Fill `NAMED_HUMAN` / `NAMED_ROLE` if you have written consent; otherwise leave blank (chrome must show `for named human unset` — do not invent a customer). Observe model **must differ** from judge. Never commit `.env`.
2. Continue `specs/listguard/tasks.md` from **T12**. Sunday pad gold to n≥40 when you have listings (composition in spec §8). Keep seed ids.
3. T13: TF VL observe (schema in spec §7). No image → empty caption, continue on text. If VL 429: text-only, still ship judge+policy+eval.
4. T14–T16: lock policy tests; wire UI card (96×96 thumb, inject string **visible as text**, ALLOW/QUEUE/BLOCK as words, Accept ink button, Override persists queue). No URL-scrape field. No purple/gradient/shadow/Inter. Do not restyle `app/web/static/app.css` without editing `specs/design/MASTER.md` first.
5. T17–T19: run gold; fail the build if hostile→allow > 0; proprietary column `n/a` if no key; `/eval` is a `<table>`, redacts IBAN.
6. P1 generate rationale ≤80 tokens **only if** T18 is green. Generate cannot change `action`.
7. Demo 90s: `lg-inject-01` first, then fake-rolex, then bike + Accept, then `/eval`.

## Hard rules

- Token Factory is the engine. Jev/Tavily/Phoenix are optional accelerators, never the title.
- Models propose; **code** decides `allow|queue|block`. Closed set in `buckets.json`.
- Never fetch a user-supplied URL. Jinja autoescape on. No `|safe`. No Markdown-to-HTML of model text.
- If no TF key: queue and receipt `judge=unconfigured`. Do not fake ALLOW or euros.
- Do not add indigo, Inter-as-unchoice, Tailwind-CDN, shadcn defaults, a second stylesheet, a vector store, n8n, or a browser agent.
- Do not implement another skin. Pack export may stay.

## Done when

`SKIN=listguard pytest -q` green; hostile fixture never ALLOW; weapon → block; named human (or explicit unset) in chrome; risk-tier in footer; `/eval` has honest numbers or honest n/a; you can run the 90s script without skipping inject.
