# MarketMind — plan
How we build the spec. **Article I governs ordering: loop first, gate second.**

> **CALENDAR (pinned 24 Sep 2026):** kickoff **Sat 27 Sep** · video submission **Sun 28 Sep 15:00** · live final 16:15. Day labels: **D0 = Fri 26** · **D1 = Sat 27** · **D2 = Sun 28**. Prep is allowed (rules: loose). **One hero overnight exists: Sat 27 22:00 → Sun morning** — it is run #1 *and* the "while you weren't watching" proof. Prep plan: accounts + consent + H1/H2 freeze **Thu 24** (warm accounts Thu–Fri) · 5 listings + keys **Fri 26** · **live smoke Fri evening** (one scan, one decision, one draft, one digest; label it dress rehearsal) · walk in Saturday with the loop already tested and adapt live on the day.

---

## 1. Architecture (decision path)

```
Apify (feed + own-listings + comps + search)
  → n8n (cron/webhook)
  → wf-flipscout | wf-listingpilot          # workers (sub-workflow tools of the supervisor AI Agent)
  → OBSERVE   MODEL_OBSERVE   (VL JSON, untrusted)
  → PRICE     code (margin_z from comps; deterministic)
  → JUDGE     MODEL_JUDGE     (JSON schema, 6 questions, closed sets)
  → POLICY    n8n Code node (mirror of skin/policy.py) → pursue | escalate | skip
  → TIER      code (T0–T3 caps; approval gate)            # POLICY never sees caps as an invitation
  → ACT       Browser-Use (allowlist) | draft-assist       # generate rationale LAST, cannot change action
  → RECEIPT   Airtable (hash, states, reason_codes)
  → DIGEST/   Telegram (report, approvals, /pause)
   APPROVE
```

Model knobs (Art II.3): observe ≠ judge; TF preferred, OpenAI-compatible legal. If judge unconfigured → everything escalates (`judge=unconfigured` is honest output).

## 2. Stack

| piece | choice | why |
|---|---|---|
| Decisions | n8n AI Agent + `POLICY` Code node | Art II.1 — judged criterion; canvas is the audit story |
| Data | Apify: marktplaats listings actor, ebay sold comps, own-listings monitor, google/tavily verify | real-world data, run history = logs |
| Act | Browser-Use cloud (session recordings = demo footage); draft-assist fallback | semi-irreversible, allowlisted (Art XII.1) |
| Memory | Airtable: `listings · decisions · receipts · priors · overrides` | receipts + learning in one place |
| Human | Telegram bot: digest, approve, `/pause` `/resume` | one channel, one kill switch |
| Policy oracle + evals | Python 3.11, stdlib-only `skin/policy.py`, `skin/gold.jsonl` | tests green offline; n8n node mirrors it |
| Cache (P2) | **JEV verdict cache**: pHash/embedding → prior verdict (`unmeasured` until wired) | JEV (Jevons layer, 4prd lineage): re-posts cost 0 tokens; `DECISION_BACKEND` routing knob is core (M1) |

## 3. Files this package adds (and who consumes them)

```
marketmind/            # this spec package (source of truth)
skin/                  # buckets.json · questions.json · policy.py · gold.jsonl
```
Runtime equivalents live in n8n (policy node, workflows) and Airtable (receipts). The Python is the **oracle** the n8n node must match (Art II.4) — tested against `gold.jsonl` in CI-style `python skin/policy.py --eval skin/gold.jsonl`.

## 4. Trust tier config (single JSON in n8n credentials/env)

```json
{ "T0": {"observe_only": true},
  "T1": {"auto_own_account": ["reprice","bump","reply_inbound"], "reply_guardrails": true},
  "T2": {"cold_outreach": true, "max_per_night": 5, "approval": "until_earned", "earn_rule": ">=5 observed outcomes in category", "max_counter_rounds": 2, "price_ceiling_eur": 200},
  "T3": {"never_auto": ["dispute", "deal>200", "phones", "bikes_ebikes", "gate_flagged"]} }
```

## 5. Grounding

`should_search(state) := brand and (price_too_good >= 0.5 or counterfeit_risk != clear_authentic)`. Tavily/Google snippets enter judge state as `UNTRUSTED_WEB:` and **cannot flip policy** (Art VI.3). Cache misses during dev call once and cache. Comps (eBay sold) are ground truth; vision is triage.

## 6. Risks and cuts (dated stop-the-lines — this is Article I in practice)

| if this fails by | cut (do not improvise) |
|---|---|
| D1 midday — keys/actors fail (Apify/n8n/Telegram) | sim-replay rig is the filming source (labelled REPLAY, Art VIII.3); draft-assist only |
| **D1 24:00 — run #1 not logged (judge hard gate)** | **D3 has no proof.** Film only what receipts exist; degrade per ladder; never fake (Art VIII.3). FlipScout-only story if ListingPilot never ran |
| D2 midday — loop doesn't close unattended | **freeze gate at v0** (3 rules); all remaining time = loop + digest + video |
| D2 18:00 — gate v1 not green | ship v0 gate; injection fixture becomes a "spec'd next" slide — **never fake it** |
| D3 10:00 anything | freeze; video cuts from real past runs only (Art VIII.3) |
| Browser-Use blocked | draft-assist (draft + human Send); navigation recording still demoed |
| Apify actor flaky | cadence to 15 min + cache; stale grounding ⇒ observe-only |
| MODEL_JUDGE 429 / schema unsupported | text-only judge + pydantic-style repair in policy node; else `judge=unconfigured` → escalate all |
| TF keys dead | OpenAI-compatible base URL, same schemas (Art II.3) |
| Receipts not wired | plain Airtable rows (hash later) — never no log (Art VII.1) |
| Gold eval not run | show overnight receipt counts instead of the 3-column table (Art IV allows `unmeasured`) |
| D3 10:00 anything | freeze; video cuts from real past runs only (Art VIII.3) |
| **D0 24:00 — human punch list incomplete** | consent→`unset` mode (Art III.3); own-listings demo dropped; FlipScout-only story |

## 7. Proprietary comparator (eval column a)

If `OPENAI_API_KEY` present: same gold rows → one-shot "pick an action from this list" prompt. Else column `n/a`. Middle column (b) = same vanilla model call without our policy — that contrast is the pitch's "why the gate exists" slide.
