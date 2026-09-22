# ClauseWindow — tasks

Sunday is mandatory.

---

## Sunday

- [ ] **T0** Named lawyer in spec + consent.
- [ ] **T1** TF keys; **measure TTFT + €** on the trap PDF / extracted text with observe model. Write numbers in `evals/clausewindow/latency.txt`.
- [ ] **T2** Trap document `cw-trap-schedule4-01` (cap only in Schedule 4) + `cw-inject-01` clause. Public/second PDF.
- [ ] **T3** Playbook `acme-v1.json` (6 rules) with the lawyer.
- [ ] **T4** Gold n≥40 **clauses** labelled.
- [ ] **T5** Extract trap text to `fixtures/clausewindow/trap.txt`.

---

## Phase 0 — harness (09:30–11:00)

**Done** in `app/` (sittings 7–9). Do not rebuild. Skip to T12.

---

## Phase 1 — skin (11:00–12:45)

- [ ] **T12** PDF/text intake (`pypdf`).
- [ ] **T13** Observe 1M → clauses JSON. Cap 80. Log TTFT.
- [ ] **T14** Batch judge ≤10 clauses; questions from spec §7.
- [ ] **T15** Policy vs playbook; unit test: inject ↛ allow; schedule-4 trap → queue.
- [ ] **T16** Heatmap UI + “not legal advice” banner + named user in footer.
- [ ] **T17** `redlines.json` download.

---

## Phase 2 — eval (12:45–13:45)

- [ ] **T18** Chunked vanilla baseline (1500-token chunks).
- [ ] **T19** Full gold run. Fail if trap not caught or hostile→allow > 0.
- [ ] **T20** `/eval` with €/doc and TTFT from Sunday + Tuesday.

---

## Phase 3 — freeze (13:45–15:00)

- [ ] **T21** `[P]` python-docx comments. If >30 min, stop. JSON is enough.
- [ ] **T22** Rehearse: inject clause → Schedule 4 → json download → table.
- [ ] **T23** Submission fields. Submit 14:45.

---

## Stop-the-line

If 1M observe hangs at 11:30: use `trap.txt` + judge batches; still show Sunday TTFT. Do not silently chunk the **policy**.  
If trap not caught at 13:15: add a **code** regex/heuristic for “liability”+“unlimited/uncapped” as a supplement, log `heuristic_cap`, do not pretend the model caught it — **say the heuristic in the pitch**. Honesty > magic.
