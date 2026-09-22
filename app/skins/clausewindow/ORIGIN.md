# ClauseWindow — how this idea was conceived, and what it survived

**This file is for an agent in a ClauseWindow-only session.** Do not reopen killed ideas. Do not turn this into ListGuard, MenuMind, or Exhibit. Do not ship a second skin.

Source of truth (read in this order before writing code):

1. `specs/constitution.md`
2. `specs/shared/harness.md`
3. `specs/design/MASTER.md`
4. `specs/security/owasp-threat-model.md`
5. `specs/clausewindow/spec.md` → `plan.md` → `tasks.md`
6. This file + `BUILD.md`

If code disagrees with a spec, the spec wins until you change the spec first (Article IX).

---

## 1. Conception

First pass on an 80-page SPA/MSA/DPA is hours. Chunked tools miss the liability cap in Schedule 4. US endpoints are a non-starter for many NL/EU firms. Chat-over-PDF is not a deliverable a GC sends.

**Job:** drop a PDF + a playbook JSON; get a heatmap of clauses vs playbook, a list of “would not sign,” and `redlines.json`.

**Wedge:** EU data residency + whole-document context. **Category:** playbook-aware first-pass redline (global).

**Why now (honest):** long-context open models on Token Factory (1M-class), EU zero-retention. The playbook is **control**, not a prompt vibe. Do not pitch “AI lawyer.”

Conceived as Accel AI Innovate Amsterdam (23 Sep 2026). Token Factory is the engine. Whole document, **no policy chunking**.

---

## 2. What the jury did to it

Survived as rank 2 if the named human is a lawyer / GC (or a friend-lawyer plus a public filing).

| Seat | What they did |
|---|---|
| **Anika** | Application layer: a vertical job (redline a clause). Not a legaltech dashboard company. This session already picked ClauseWindow. |
| **Dima** | 1M observe ≠ Fast JSON judge. Invented **topic** rate = 0 (closed CUAD-shaped set). |
| **Jonas** | Hold `redlines.json`. Hostile `cw-inject-01` first. Then Schedule 4 trap. Banner “Not legal advice” is chrome, not a toast. |
| **Priya** | Named lawyer in the **top bar** (MASTER), not the footer. n≥40 **clause** rows. Three-column table including trap-catch. |
| **Markus** | Not legal advice. A human signs. No “you should sign” generate. Walkaway is a queue, not a verdict. |
| **Elena** | Trap document must exist in-repo. Latency honesty: if p50 > 12s, **show the number**. |
| **Kenji** | If 1M hangs: pre-extracted `trap.txt` + judge batches. **Do not silently chunk policy.** Heuristic cap must be **declared**. |
| **Marta** | No fetch-PDF-from-URL. Encrypted PDF → 400 sentence, no traceback. Playbook from disk hash, not attacker upload. |
| **Camille** | Reading column ≤68ch. Source Serif **only** on quotes. Walkaway = 3px oxide left border, text stays readable. No “Analyze with AI.” |

**Killed:** legal advice as fact, jurisdiction opinions, negotiation chatbot, data rooms, live case-law Tavily, “AI lawyer” robot, glass cards.

---

## 3. Sittings that already happened (do not re-litigate)

| Sitting | Outcome for ClauseWindow |
|---|---|
| Judging-panel teardown | Playbook is JSON. Irreversible legal advice → queue. |
| Security/UX | Counterparty PDF is untrusted. Quotes escaped. `/eval` shows trap **ids**, not the SPA. |
| Sitting 6 | Pack layer exists on the harness. You may emit `GET /exhibit/{id}` from a clause job. You may not build the Exhibit *skin*. |
| Sitting 7–8 | Harness Phase 0 is **done**. Accept persists sqlite. Override queues. Honest unconfigured judge. |
| Sitting 9 | Named human in chrome; `cw-inject-01` + `cw-trap-schedule4-01` seeded; skip rebuilding T5–T11. |

---

## 4. Monday 18:00 (resolved for this session)

This session **is** ClauseWindow. Fill `NAMED_HUMAN` as counsel / legal ops. Playbook `acme-v1.json` is the sample until the lawyer writes six rules — do not invent a client.

---

## 5. Risk-tier sentence (footer, unchanged)

> Limited-risk decision support for lawyers. Not legal advice. We flag playbook walk-aways; a human signs.
