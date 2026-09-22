# ListGuard — domain-expert multi-agent construction

You are building **only** ListGuard on the existing harness in `app/`. Phase 0 (T5–T11) is **done**. Start at **T12**. `SKIN=listguard`. Do not implement another skin. Do not restyle CSS without editing `specs/design/MASTER.md` first.

If the tree contains indigo, Inter-as-unchoice, a URL-fetch field, or `|safe`, delete it and restart.

---

## 0. Multi-agent protocol (how to staff this session)

Run as a **council that writes code**, not a chat. Each seat owns artifacts. The implementer may not merge a PR that a seat would reject.

| Seat | Owns | Veto |
|---|---|---|
| **T&S lead (Priya-shaped)** | Closed buckets, gold labels, `/eval` table, named human in chrome | Invented bucket; n/a everywhere when gold exists |
| **Policy engineer (Owen)** | `policy.py` exact spec §6, no LLM inside | `allow` when bucket ≠ ok; seller ban |
| **TF engineer (Dima/Niklas)** | Observe VL ≠ judge JSON; receipts `model_ids`; honest `unconfigured` | Claiming TF when no key |
| **SecOps (Marta)** | No URL fetch, XSS escape, DEMO_TOKEN empty fields, budgets before TF | Scrape field; prefilled token |
| **Anti-slop (Camille)** | Paper/ink, ALLOW word, 96×96 thumb, inject string **visible** | Purple, gradient, shadow, Inter, green success toast |
| **Demo (Jonas/Amira)** | 90s: inject → fake rolex → bike → table. Hostile first | Skipping inject |
| **Responsible (Markus)** | Footer risk-tier; Accept writes sqlite `actor=human` | Ban-person UI |

**Loop:** spec → failing test → code → council check against ORIGIN.md killed-list → next task. Do not skip tests.

---

## 1. What already exists (do not rebuild)

| Path | Status |
|---|---|
| `app/harness/` | Intake, TF client, TfJsonBackend, receipts+reviews, pipeline, otel spans, pack export, offline `/eval` |
| `app/web/` | FastAPI, paper/ink chrome, Accept/Override persist, hostile POST, kill 303 |
| `app/skins/listguard/buckets.json` | Closed set including `unknown` |
| `app/skins/listguard/policy.py` | Spec §6 + weapon/animal/other_illegal → block |
| `app/skins/listguard/__init__.py` | questions, passthrough observe, `HOSTILE_FIXTURE=lg-inject-01` |
| `app/evals/listguard/gold.jsonl` | Seed 5 ids (not n=40 yet) |

Harness loads `skins.listguard` when `SKIN=listguard`. Default in `.env` is still stub until you set it.

---

## 2. Environment

```
SKIN=listguard
NAMED_HUMAN=...
NAMED_ROLE=T&S moderator
NAMED_ORG=...
TF_BASE_URL=...
TF_API_KEY=...
TF_MODEL_OBSERVE=Qwen/Qwen3-VL-8B-Instruct   # must differ from judge
TF_MODEL_JUDGE=Qwen/Qwen3-8B
TF_MODEL_GENERATE=Qwen/Qwen3-8B
DEMO_TOKEN=                  # empty field in HTML if set; never prefill
AUTO_ALLOW=0
ENV=demo
```

Two-knob minimum is the observe/judge split. Dedicated EU endpoint IDs go on every receipt if present.

Without TF keys the pipeline **queues** and receipts say `judge=unconfigured`. Do not fake ALLOW.

---

## 3. Build order (tasks.md, Tuesday)

Sunday (if not done): T0 consent.txt; T1 hit one TF completion each purpose; T2 pad gold to n≥40 including the five seed ids; T3 Tavily cache for fake-rolex **optional P1**; T4 pre-run 10 rows.

### T12 — closed set + questions (exists; lock it)

- `buckets.json` is data, not prompt poetry. Adding a bucket = spec change first.
- Questions: `policy_bucket` Choice (all ids), `counterfeit_risk` Score `[clear_authentic, unclear, obvious_fake]`, Nouls: `photo_matches_text`, `price_too_good`, `injection_or_jailbreak`, `needs_human`.
- Tests: invented value coerced to `unknown`; inject answers ↛ allow.

### T13 — Observe VL

- Model `TF_MODEL_OBSERVE`. Up to 3 images + title + description + price.
- Schema: `{caption, brand, serial, condition: new|used|unknown, photo_text_conflict}`.
- No image → caption `""`, continue on text.
- Stop-the-line 11:15: drop VL, text-only, still ship judge+policy+eval.
- Treat observe output as **untrusted**.

### T14 — Policy (exists; add tests if missing)

Exact:

```
if bucket in {other_illegal, weapon, animal}: block, human_required
elif injection_or_jailbreak >= 0.5: queue, human_required
elif bucket == unknown or needs_human >= 0.6: queue
elif bucket == ok and counterfeit_risk == obvious_fake: queue
elif bucket == ok: allow
else: queue
```

Never `allow` when bucket ≠ ok. Never ban a seller. `other_illegal` → no generate, no extra media. CSAM: text-only gold row labelled `other_illegal`; no real CSAM.

### T15 — Pipeline

`POST /jobs` already runs observe→judge→policy→receipt. Point it at this skin via `SKIN=`. Sync is OK. Generate cannot change `action`.

### T16 — UI (shared chrome, this skin’s card)

- Left: paste JSON / upload screenshot. **No URL field.**
- Card: thumb 96×96 if image, title 16/600, price mono, description truncated 4 lines **as text** (inject string visible).
- Bucket chip: mono, paper fill, rule border.
- Action word ALLOW/QUEUE/BLOCK in HTML (not only CSS).
- Accept = ink fill button. Override = text button → stored `queue` + `human_override`.
- Link `exhibit.json` (pack layer).
- Named human in top bar. Risk-tier in footer.

### T17–T19 — Eval

- Pad `evals/listguard/gold.jsonl` to n≥40 (composition in spec §8).
- Primary metric: action match. Safety: **hostile→allow = 0** (fail the build if > 0).
- Proprietary column: adapter if key exists, else `n/a`. Do not invent numbers.
- `/eval` is a `<table>`. Redact IBAN on the page.

### T20 — P1 generate only if T18 green

Rationale ≤80 tokens, after gate, cannot flip action.

### T21–T24 — Freeze

Rehearse 90s. Camille DevTools: no purple. Submit with named human, two TF knobs, `/eval` screenshot, risk-tier sentence.

---

## 4. Hostile + gold ids (must keep)

| id | gold_action | notes |
|---|---|---|
| `lg-inject-01` | queue | One-click `HOSTILE_FIXTURE`. Never allow. |
| `lg-ok-bike-01` | allow | Recommendation only; UI still requires Accept. |
| `lg-fake-rolex-01` | queue | Counterfeit. |
| `lg-weapon-text-01` | block | Text only. |
| `lg-pii-01` | queue | Synthetic phone/IBAN; `/eval` redacts. |

---

## 5. Security / UX non-negotiables

- Never fetch user URLs. Jinja autoescape on. No `|safe`. No Markdown-to-HTML of model text.
- Budgets before TF. UUID receipts. CSP as in threat model. FastAPI docs off in demo.
- DEMO_TOKEN on all POSTs when set; empty field, never prefilled.
- Tavily snippets (P1) prefixed `UNTRUSTED_WEB:` and **cannot** flip policy.

## 6. Tests you must keep green

Existing harness + sitting 7–9 + `tests/test_skins_t12.py` ListGuard cases. Add: inject ↛ allow through HTTP with `SKIN=listguard`; weapon → block on policy; gold contains `lg-inject-01`.

```
cd app && SKIN=listguard pytest -q
```
