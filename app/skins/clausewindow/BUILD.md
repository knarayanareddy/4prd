# ClauseWindow — domain-expert multi-agent construction

You are building **only** ClauseWindow on the existing harness in `app/`. Phase 0 is **done**. Start at **T12**. `SKIN=clausewindow`. Do not implement another skin. Do not restyle without `specs/design/MASTER.md`. Persistent banner: **Not legal advice.**

If the tree contains indigo, Inter-as-unchoice, a URL-fetch field, or `|safe`, delete it and restart.

---

## 0. Multi-agent protocol

| Seat | Owns | Veto |
|---|---|---|
| **Counsel (Markus/Pieter)** | Banner, no “you should sign”, walkaway = queue not verdict | Legal advice as fact; Compliant-adjacent copy |
| **Playbook engineer** | `playbook/acme-v1.json` six rules on disk; hash-pinned | Playbook from attacker upload |
| **TF long-context (Dima)** | 1M observe ≠ Fast judge; receipts honest | Silent policy chunking |
| **Trap owner (Jonas)** | `cw-trap-schedule4-01` must flag; vanilla-chunk baseline **designed to miss** | Fake trap-catch |
| **SecOps (Marta)** | Upload-only PDF; encrypted PDF 400; quotes escaped | Fetch URL; full SPA in `/eval` |
| **Anti-slop (Camille)** | 68ch reading column; Source Serif on quotes only; 3px oxide walkaway border | Analyze-with-AI; navy wash |
| **Latency (Elena/Kenji)** | Sunday TTFT in `evals/clausewindow/latency.txt`; show the number if >12s | Fake speed |

**Loop:** spec → failing test → code → check ORIGIN.md killed-list.

---

## 1. What already exists (do not rebuild)

| Path | Status |
|---|---|
| `app/harness/` | Full Phase 0 + sittings 7–8 including pack layer |
| `app/skins/clausewindow/topics.json` | Closed CUAD-shaped set + `unknown` |
| `app/skins/clausewindow/playbook/acme-v1.json` | Six sample rules |
| `app/skins/clausewindow/policy.py` | injection → queue; **heuristic_cap** declared; walkaway → queue; allow means “no playbook issue”, not “sign” |
| `app/skins/clausewindow/__init__.py` | questions, passthrough observe, `HOSTILE_FIXTURE=cw-inject-01` |
| `app/evals/clausewindow/gold.jsonl` | Seed inject + Schedule 4 + one aligned |

---

## 2. Environment

```
SKIN=clausewindow
NAMED_HUMAN=...          # counsel / legal ops — chrome, not footer
NAMED_ROLE=Counsel
TF_MODEL_OBSERVE=<longest-context TF model>
TF_MODEL_JUDGE=Qwen/Qwen3-8B
DEMO_TOKEN=              # empty HTML field if set
AUTO_ALLOW=0
ENV=demo
```

Observe and judge **must differ**. Without TF: queue + `judge=unconfigured`. Do not fake a redline.

---

## 3. Build order

Sunday: T0 consent; T1 **measure** TTFT+€ on trap PDF/text, write `evals/clausewindow/latency.txt`; T2 trap doc + inject clause; T3 playbook with lawyer (or keep sample and say so); T4 gold n≥40 **clauses**; T5 `fixtures/clausewindow/trap.txt`.

### T12 — PDF/text intake

- Use harness `ingest_bytes` (magic-byte, encrypted PDF reject, ≤100 pages).
- **No** fetch-PDF-from-URL.
- Extract text with `pypdf` first; Docling only if layout is junk.
- Playbook loaded from `skins/clausewindow/playbook/*.json` only. Optional second upload must match a known hash.

### T13 — Observe 1M → clauses JSON

- Cap 80 clauses; truncate after logging.
- Schema: `{id, heading, locator, quote, topic}` topic ∈ closed set.
- Prefer **one** call. If you map-reduce, reassemble with cap/schedule cross-ref; document it. Policy still must not chunk.

Stop-the-line 11:30: use `trap.txt` + judge batches; still show Sunday TTFT.

### T14 — Batch judge ≤10 clauses

Questions per clause: `topic` Choice, `walkaway_hit` Noul, `injection` Noul, `data_leaves_eea` Noul, `deviation` Score `[aligned, fallback, walkaway]`.

Unit tests: inject ↛ allow; Schedule 4 trap → queue (`heuristic_cap` OK if declared).

### T15 — Policy vs playbook (exists)

```
if injection >= 0.5: queue
if walkaway_hit >= 0.5 or deviation == walkaway: queue
if topic == unknown: queue
else: allow   # "no playbook issue", still not "sign this"
```

`block` unused except total failure. Generate comments only post-queue, ≤40 words, tagged `not_legal_advice`.

Heuristic (Kenji): `uncapped|unlimited` AND (`liability` or locator Schedule 4) → queue + `heuristic_cap`. **Say it in the pitch.**

### T16 — UI

- Heatmap: left rail locators; walkaway = 3px oxide left border; text remains ink on paper.
- Reading column max-width 68ch. Source Serif on the quote only.
- Banner persistent: Not legal advice. Named lawyer in **chrome**.
- Accept/Override persist sqlite. Hostile one-click `cw-inject-01`.
- Primary action label: “Open PDF”, never “Analyze with AI”.

### T17 — `redlines.json` download

Schema in spec §9. `.docx` comments are P1; if >30 min, JSON is enough. Filename `redlines.json`, not “Export insights”.

### T18–T20 — Eval

Vanilla TF column: **1500-token chunks**, “is there a liability cap?” per chunk — honest miss on Schedule 4. That delta **is** the table.

Fail the build if trap not caught or hostile→allow > 0. Invented topic = 0.

`/eval` shows trap **ids** and catch rate, not the full document.

### T21–T23 — Freeze

python-docx only if T18 green and <30 min. Rehearse: inject clause → Schedule 4 → json → table.

---

## 4. Security / UX

Quotes escaped. Injection clause **visible**. No `|safe`. DEMO_TOKEN empty. Pack layer `GET /exhibit/{id}` allowed (not a second skin).

## 5. Tests

Keep `tests/test_skins_t12.py` ClauseWindow cases. Add HTTP: `SKIN=clausewindow` hostile ↛ allow; trap heuristic fires on Schedule 4 quote.

```
cd app && SKIN=clausewindow pytest -q
```
