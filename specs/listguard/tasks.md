# ListGuard — tasks
Execute in order. Phase 0 is the harness (shared). Check boxes.

Sunday night (before 09:30) is **not optional**: T0–T4.

Legend: `[P]` parallel-safe with the previous open task.

---

## Sunday (T0–T4)

- [ ] **T0** Fill named human in `spec.md`. Written consent in `consent.txt`.
- [ ] **T1** Confirm TF keys, list models, set `.env` observe/judge/generate. Hit one completion each.
- [ ] **T2** Author `evals/listguard/gold.jsonl` to n≥40 including `lg-inject-01`, `lg-ok-bike-01`, `lg-fake-rolex-01`, `lg-weapon-text-01`, `lg-pii-01`. Photos in `fixtures/listguard/`.
- [ ] **T3** `[P]` Cache Tavily for the fake-rolex brand into `fixtures/tavily/`.
- [ ] **T4** Pre-run 10 gold rows by hand against judge-only if harness not built; record anything that 429s.

---

## Phase 0 — harness (09:30–11:00)

**Done** in `app/` (sittings 7–9). Do not rebuild. Skip to T12.

- [x] **T5–T11** harness, receipts, pytest, kill, CSP, DEMO_TOKEN, paper/ink chrome.

Do not start the ListGuard UI before T8 works on a fixture. T8 already works on the stub fixture.

---

## Phase 1 — skin (11:00–12:30)

- [ ] **T12** `buckets.json` + `questions.py`.
- [ ] **T13** Observe VL JSON call + pydantic repair.
- [ ] **T14** `policy_fn.py` exactly as spec §6. Unit tests: inject ↛ allow; weapon → block; ok+not fake → allow.
- [ ] **T15** `POST /jobs` sync pipeline observe→judge→policy→receipt.
- [ ] **T16** HTML: drop zone, card, Accept, receipt link, kill switch.

---

## Phase 2 — eval + hostile (12:30–13:45)

- [ ] **T17** `eval_runner.py` three columns (proprietary adapter optional).
- [ ] **T18** Run full gold. Write `evals/listguard/last_report.md`. Fail the build if hostile→allow > 0.
- [ ] **T19** `/eval` page renders the report. **Leave it open.**
- [ ] **T20** `[P]` P1 rationale generate **only if T18 is green**.

---

## Phase 3 — demo freeze (13:45–15:00)

- [ ] **T21** Rehearse 90s script (inject → rolex → bike → table). Time it. Camille check: no purple in DevTools, ALLOW is a word, named human in chrome.
- [ ] **T22** Fill submission: named human, architecture (two TF knobs), screenshot of `/eval`, risk-tier sentence.
- [ ] **T23** Disable live Tavily. `AUTO_ALLOW` per constitution UI rule.
- [ ] **T24** Submit by 14:45. Do not start P2 DSA forms.

---

## Stretch after T18 green (do not steal T21 time)

- [ ] LoRA row on Qwen3-8B using public bucket labels (constitution: bonus row only).
- [ ] Jev backend flag, fourth column.
- [ ] n8n webhook on receipt.

---

## Stop-the-line

If T8 not working at 11:15: drop VL, text-only listings, still ship judge+policy+eval.  
If T18 hostile→allow > 0 at 13:30: **fix policy**, do not add UI chrome.
