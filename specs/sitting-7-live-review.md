# Sitting 7 — Judges on the *live* harness (not the memo)

The jury was shown `app/` as it exists: stub skin, paper/ink chrome, 35 tests, four product specs, Exhibit primitives unwired.

They did not re-litigate strategy. They scored **what would happen at 16:00 if we demoed this**.

---

## Jury (verbatim)

**Priya:** “There is no named human in the chrome unless env is set. There is no gold set. `/eval` is empty n=0. There is no Accept. `actor` is always system. The form is incomplete. You would not make the top eight.”

**Jonas:** “The wordmark says Harness. Article VIII said the harness is not the company. There is no hostile-first click. I have to paste JSON from memory. The operator line is good. The missing Accept button is a broken promise.”

**Dima:** “Receipts claim `tf_model_judge` even when no key was configured. `euro_estimate` is always 0. You would tell me you used Token Factory when you did not. That is a criterion-3 lie. Jev backend raises. If someone sets the flag you crash.”

**Markus:** “Human oversight is copy, not a record. Exhibit’s Art. 14 is vapour until Accept writes a name and a time.”

**Anika:** “Four doors is still indecision. I do not care about primitives. I care which door you walk through Monday.”

**Elena:** “The hostile fixture is specified and not in the repo. Demo opens on an empty work surface.”

**Marta:** “Kill form cannot send DEMO_TOKEN without leaking it into HTML. Empty token field on POST is fine. Pre-filling it is not. Also: span primitives exist and the pipeline never calls them.”

**Camille:** “Chrome is not purple. Pass. Plex is not actually loaded; Helvetica is an honest fallback. Do not add Google Fonts (CSP). Do not fake Plex.”

---

## Council vote — implement these, not more strategy

| # | Tweak | Who |
|---|---|---|
| 1 | Accept / Override writes `actor=human` + name + ts (append-only review) | Markus, Priya |
| 2 | One-click **Open hostile fixture** posts `ex-inject-01` | Jonas, Elena |
| 3 | Honest receipts: `judge=unconfigured` when TF key missing; do not call TF | Dima |
| 4 | Jev flag falls back to tf_json, never crash | Dima |
| 5 | Seed gold.jsonl (stub) including inject; `/eval` shows ids | Priya, Sofia |
| 6 | Wire `harness.otel.span` around pipeline steps | Leila, Marta |
| 7 | `GET /exhibit/{id}` pack from any job (layer, not a second skin) | Jonas, Kenji |
| 8 | Optional empty token field on forms (not prefilled) | Marta |
| 9 | Constitution: four products; Exhibit is a skin *or* a pack export | Nora |
| 10 | Wordmark from skin; stub says “Stub agent” not “Harness” | Anika |
| 11 | Kill uses 303 RedirectResponse | Kenji |

**Rejected (do not implement Tuesday):** Google Fonts, AX, Phoenix docker, n≥40 labelled tonight (seed ≥10; Sunday pads to 40), fake euro numbers, Compliant button.

---

Implemented in this sitting in `app/` + spec one-liners.
