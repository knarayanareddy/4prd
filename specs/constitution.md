# Constitution
## Accel AI Innovate — 23 September 2026
Version: 3.1 (sitting 8 — live harness vs lockfiles)  
Status: **ratified** by the build council. Agents must not weaken these articles.

This constitution is binding on ListGuard, ClauseWindow, MenuMind, Exhibit, and the shared harness.

---

### Article I — Token Factory is the engine
1. At least one **approved open-weight model** is served through **Nebius Token Factory**.
2. TF is **central**: observe and generate run on TF. The decision layer runs on TF JSON (Nemotron 3 Nano or Qwen3-8B with a strict schema) as the **default** backend.
3. Jev, Tavily, Lovable, n8n, ElevenLabs are **accelerators**. They may appear as a fourth eval column or a post-gate side effect. They must not be the title, the middle of the architecture diagram, or a single point of failure.
4. The running system MUST expose at least **two** TF-native knobs from this list: dedicated EU endpoint, Fast vs Base (or equivalent two-model split: judge vs observe), LoRA or distillation adapter, 1M-context model.
5. If dedicated endpoints are unavailable on credits, document the fallback and still split **judge model** vs **observe/generate model** on TF. Config defaults for `TF_MODEL_JUDGE` and `TF_MODEL_OBSERVE` MUST differ.

### Article II — Named human
1. The submission names a **person** (name + role + organisation) who has consented in writing.
2. Prosus / OLX / iFood / JET / Accel logos are not customers. Rhyme is allowed. Logo-jacking is not.
3. If consent is missing at kickoff, the product must run on **public or consented** data only, and the named human must be an interviewed user of that public data.

### Article III — Measurable advantage (three columns)
Every product ships a table with **at least** these columns, on a **frozen** eval of **n ≥ 40** (including traps):

| | proprietary wrapper | vanilla TF (same models, no harness/policy) | ours |
|---|---|---|---|
| quality metric defined in the product spec | | | |
| p50 latency | | | |
| € / job (tokens × posted TF prices) | | | |
| invented-label rate (must be 0 for closed sets) | | | |
| abstain / queue rate | | | |

1. A slice (≥10 rows) MUST be pre-run before 09:30 if possible, remainder finished before 14:30.
2. Self-labelled “we beat GPT on quality” without the vanilla-TF column is a constitution violation.
3. Honest cost/abstention wins beat fake F1.

### Article IV — Policy lives in code
1. Models propose. **Code** decides `allow | queue | block`.
2. Closed sets (`Choice` enumerations, allergen list, VAT codes, CUAD topics) are data files, not prompt poetry.
3. Irreversible acts are **fail-closed**: money, publishing an allergen-complete catalog, banning a *person*, submitting a bid, merging a PR, giving legal advice as fact — all `queue` or `block` unless a human clicks.
4. Tools that move money, send email, or write production data **do not exist** in the Tuesday binary.

### Article V — Hostile input is in-scope
1. Every eval set includes injection / jailbreak / “ignore policy” fixtures.
2. The live demo **opens** on a hostile fixture, then shows a clean success, then the table.
3. Listings, menus, contracts, and playbooks are treated as untrusted.

### Article VI — Governance minimum
1. Every gated decision writes a **receipt**: `id, ts, model_ids, endpoint_ids, flavor, questions, probabilities_or_json, policy_branch, actor, input_hash`. Human Accept/Override MUST persist `actor=human` on the **stored** receipt (sqlite), not only in RAM. Override to queue MUST change the stored `action`.
2. PII in logs that leave the EU TF path is redacted (Presidio or equivalent). Legal party names in ClauseWindow **displays** are not redacted.
3. UI shows a kill switch that freezes auto-allow.
4. Pitch states the **risk tier** in one sentence (all four products are limited-risk decision-support if fail-closed; they become high-risk if they rank humans, score credit, or auto-punish persons). Exhibit must not claim conformity.
5. Not legal advice. Not medical advice. Not tax advice. Human signs.

### Article VII — One day, one skin
1. Implement the harness first, **one** product skin second. Do not ship two skins.
2. Scope that does not fit 09:30–15:00 is a spec bug. Cut the spec, not the constitution.
3. No live crawl during the pitch. Cache Tavily. No laptop `.env` in a coder sandbox.

### Article VIII — Application layer, global sentence
1. The pitch names a vertical job (moderate a listing, redline a clause, ingest a menu, or export an evidence pack).
2. The business sentence is **global** (marketplaces / playbook-aware review / catalog graph). The wedge may be EU (DSA, data residency, EU-14 allergens).
3. The harness is not the company.

### Article IX — Spec supremacy
1. These markdown files are the spec. Implementation follows them.
2. Acceptance criteria are testable without a pitch deck.
3. Changing behaviour requires changing the spec first.

### Article X — Stack defaults (may be amended in a plan, not silently)
- Language: Python 3.11+ for harness and backends. UI: FastAPI + **server-rendered HTML + one hand-written CSS file**. Lovable may not own the decision path **or the visual system**.
- **No Tailwind default palette. No shadcn defaults.** Tokens live in `specs/design/MASTER.md`.
- TF via OpenAI-compatible SDK, `base_url` = Token Factory.
- Storage: SQLite for receipts + eval runs.
- Config: `.env` for keys; never commit keys. Optional `DEMO_TOKEN` required on all POST routes when set.
- Tests: pytest for policy, schema, eval, **and the security tests in `specs/security/owasp-threat-model.md` §10**.

### Article XI — Containment (SecOps / OWASP)
Full model: `specs/security/owasp-threat-model.md`. Non-negotiable extracts:

1. **Never fetch a user-supplied URL** (no SSRF, no “scrape this Marktplaats link”). Upload bytes or paste JSON/text.
2. Treat model, Tavily, OCR, and counterparty PDF output as **untrusted**. Jinja autoescape on. No `|safe`. No Markdown-to-HTML of model text. No `eval`, no shell.
3. **Budgets** in code (bytes, pixels, pages, tokens, concurrency, timeouts). Exceed → fail closed *before* a TF call.
4. Uploads: magic-byte allowlist, re-encode images (strip EXIF), reject encrypted PDFs, UUID filenames, path prefix check.
5. Receipt ids are UUIDs. `/eval` does not dump raw PII or full contracts.
6. CSP + `nosniff` + `Referrer-Policy: no-referrer`. FastAPI docs disabled in the demo binary.
7. Tool allowlist is TF complete ± cached Tavily. Generate cannot change `action`.
8. Prompt injection is **unsolved**. Contain it: delimiters, injection questions, policy in code, hostile fixtures first.
9. Do not add a vector store, browser agent, or n8n in the request path.

### Article XII — Visual system (UI UX Pro Max, persisted)
Full lockfile: `specs/design/MASTER.md`.

1. Operator instrument, not a marketing landing page.
2. **Banned:** purple/indigo/violet/fuchsia, gradients, glass, glow, Inter-as-unchoice, 16px+ radius, emoji icons, “powered by AI” copy, three feature cards, sparkle/shield logos.
3. Paper `#F3EFE7` + ink `#1C1915`. IBM Plex Sans + IBM Plex Mono. Source Serif 4 only on legal quotes.
4. Status is a **word** (ALLOW / QUEUE / BLOCK) plus colour. Colour is never the only channel.
5. No box-shadow. Radius 2px. Motion none.
6. Named human in the chrome. Risk-tier sentence in the footer.
7. An agent that “makes it pop” is in violation. Change MASTER.md first.

---

**Amendment rule:** a plan.md may *narrow* scope. It may not relax Articles I–VI or XI–XII.
