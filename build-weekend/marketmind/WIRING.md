# WIRING.md — turn the walking skeleton from `sim` to `live` (30–60 min with keys)

The pipeline is done and self-tested in **sim** mode (`app/run_walking_skeleton.py`). Live mode swaps four HTTP surfaces. Nothing else changes.

## 0) Human punch list (T04 — cannot be automated)
- [ ] `kickoff/consent.txt` signed by `NAMED_RESELLER` (else set `unset`, Art III.3)
- [ ] Dedicated demo Marktplaats account (NOT personal) + second account + 1 consented friend
- [ ] Post the 5 items per `kickoff/LISTING-PLAN.md`
- [ ] Freeze `kickoff/PREREGISTRATION.md` (fill date + name)
- [ ] `cp app/env.example app/.env` and fill as keys arrive

## 1) Apify (T05 — real data)
1. Create token at apify.com → account settings → API tokens → `APFY_TOKEN`.
2. Note actor ids (start with one, Marktplaats listings actor, e.g. `haketa/marktplaats-scraper` — verify availability Fri; fallback: any listing scraper with `{search, category, maxItems}` input):
   - `APIFY_ACTOR_LISTINGS` — new listings, niche keywords
   - `APIFY_ACTOR_COMPS` — eBay sold comps (e.g. `apify/ebay-scraper` w/ sold filter)
   - `APIFY_ACTOR_OWN` — your 5 listings (generic scraper on your profile page) *(M1, T12)*
   - `APIFY_ACTOR_VERIFY` — brand/model verification *(M2)*
3. Smoke: `python3 app/run_walking_skeleton.py --mode live --only scan` → prints items + **measured actor cycle time** (kills the 60s myth, T05).
4. Dataset item shape (the parser expects): `{id, url, title, description, price_eur, category, images[], seller{name, since, rating_count}, posted_at}` — map once in `app/mm/notice.py:_normalize`.

## 2) n8n (T06 — decisions on the canvas)
1. Import `app/n8n/wf-m0-scan-decide.json` (n8n → Workflows → Import).
2. Credentials: HTTP Bearer = Apify token; Telegram node = bot token; Airtable = PAT (§4).
3. The POLICY Code node runs `app/n8n/policy_v0_node.js` (inline in the workflow). **Oracle parity rule (Art II.4):** node code must match `skin/policy.py::gate_v0` — run `python3 app/run_walking_skeleton.py --selftest` after any edit to either.

## 3) Telegram (T08 — report + approvals)
1. BotFather → `/newbot` → `TELEGRAM_BOT_TOKEN`. Message the bot once. Get `TELEGRAM_CHAT_ID` via `https://api.telegram.org/bot<TOKEN>/getUpdates`.
2. Smoke: `--only report` sends one digest.

## 4) Airtable (receipts, Art VII)
1. PAT with `receipts` table. Columns: `receipt_id (text), ts (date), input_hash (text), action_state (single), reason_codes (text), policy_branch (text), tier (text), payload (long text), actor (text)`.
2. Or skip Airtable at M0: receipts land in `app/out/receipts.jsonl` (Art VII.1 degradation: rows acceptable, hash included).

## 5) Browser-Use (T07 — acting)
- **M0 default = draft-assist** (no key needed): the offer is composed, written to `app/out/drafts/`, and pushed to Telegram with [approve] — human presses Send. `action_state: drafted → pursued_assisted` on confirm. (`drafted ≠ sent`, Art VII.2.)
- Optional live path later: `BROWSER_USE_KEY` + allowlist (send message · edit own price · bump own listing — nothing else, Art XII.1).

## 6) First live run (Fri evening, before the 22:00 overnight)
```
python3 app/run_walking_skeleton.py --mode live            # full loop, 7 fixtures → real feed
python3 app/run_walking_skeleton.py --mode live --only scan --measure   # T05 cycle-time proof
python3 skin/policy.py --eval skin/gold.jsonl               # kill-switch metric still PASS
```
Then flip `wf-m0-scan-decide` schedule to the ~5-min cadence and arm `checklists.md` §3 (overnight run #1 — **hard gate: Friday midnight**).
