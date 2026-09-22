# Exhibit — Sitting 6
## Fourth product, same gauntlet. Phoenix/AX are sinks. Token Factory stays the engine.

**Charge:** The user proposed a fourth project from this brief:

> Shipping agents in the EU means connecting policy to artifacts: traces, evals, annotations, human review, release gates, monitoring, audit logs.  
> Walk through *How to turn agent traces and evals into EU AI Act evidence*: instrument in **Phoenix** (OTel + OpenInference), carry evidence into **Arize AX** for production monitoring, CI gates, retention, EU residency, audit history.

This sitting runs the **same** councils and jury as ListGuard / ClauseWindow / MenuMind. No participation trophy.

**Working name:** **Exhibit**  
**Skin:** `exhibit`  
**Job:** Turn a running agent’s traces, TF-native evals, and human review into an **evidence pack** mapped to AI Act *engineering* articles — without claiming conformity.

---

## 0. The panel and councils (same people)

Jury: Anika (Accel), Dima (Token Factory), Isabel (Prosus), Jonas (product), Priya (form), Markus (responsible design), Elena (why-now).  
Founders’ council + build council + Marta/Dev/Camille.

They have already killed HireSignal for “we make hiring legal.” They will try to kill this the same way.

---

## 1. Domain experts added for this skin only

| Seat | Domain |
|---|---|
| **Jitendra-proxy “Leila Okeke”** | AI observability engineer. Phoenix/OTel/OpenInference. Will not let us hand-roll spans. |
| **Pieter de Vries** | Already on the jury-adjacent counsel seat. Classification, Article 111, “not legal advice.” |
| **Sofia Park** | Evals. Judge-to-human agreement. Will fail decorative LLM-as-judge scores. |

Leila’s one-liner, from the actual Arize engineering mapping (Aug 2026, *not legal advice*):

| Obligation | Artifact |
|---|---|
| Art. 12 record-keeping | OpenInference traces of the whole trajectory + retention choice |
| Art. 14 human oversight | Annotations on spans, named reviewer, timestamp, queue |
| Art. 15 accuracy/robustness | Offline evals on datasets + CI gate |
| Art. 10 data governance | Redact **before** export |
| Art. 50 transparency | Evaluator that the disclosure actually happened |
| Art. 72 post-market | Same metrics after release (AX/monitors — stub Tuesday) |
| Art. 11 / Annex IV | Versioned prompts, dataset lineage, experiment results |

Plus the warning we **must** keep: an LLM-judge fairness score nobody calibrated against a human is *worse than no metric*.

---

## 2. Jury first (they speak before the council)

**Markus:**  
“If the pitch says ‘AI Act compliant’ or ‘high-risk ready,’ I score zero. HireSignal died for this. Observability is not a conformity assessment. You may map *engineering artifacts* to article numbers. You may not sell a CE mark.”

**Dima:**  
“If Phoenix is in the middle of the architecture and Token Factory is ‘the agent we watched,’ you failed criterion 4. The **evals** must run on TF JSON. The **agent under test** must run on TF. Phoenix is a span store. AX is a later sink. Same bucket as Tavily.”

**Anika:**  
“Langfuse, Phoenix, LangSmith, Arize AX already exist. ‘We installed OpenInference’ is not a company. Accel’s application-layer fund does not want another observability logo. The company is: **evidence pack + article-tagged schema + TF-native judges + release gate**, sold to EU teams *shipping agents*. If your slide is a dashboard, I check my phone.”

**Isabel:**  
“Not my house’s problem unless the agent is ours. Don’t logo-jack Prosus. A named Head of AI Platform is fine.”

**Jonas:**  
“I need to *hold* something. A JSON/HTML **Exhibit file** with three article sections and a human name on an annotation. Not a Grafana tour. Not a purple trace waterfall.”

**Priya:**  
“Named person. Frozen eval n≥40 on the *agent*. Three-column table on the *eval judges* (proprietary LLM-judge | vanilla TF | ours). If the table is ‘we have traces,’ incomplete.”

**Elena:**  
“Why-now is real *if* you tell the Omnibus truth: high-risk dates may slip; **Article 111** still punishes ‘significant modification’ of agents already on the market; sixteen months of policy memos will not create sixteen months of traces. Instrumentation now is the hour. ‘Fines tomorrow’ is a lie.”

**Panel hole catalog (new, on top of H1–H18)**

| ID | Hole |
|---|---|
| H19 | Phoenix/AX wrapper. Dima/Anika veto unless TF is engine of agent *and* judges. |
| H20 | Conformity theatre. Markus veto if copy overclaims. |
| H21 | Sleepy dashboard demo. Jonas veto unless the pack is the artifact. |
| H22 | LLM-as-judge as “Art. 15.” Sofia/Leila veto unless judge-human agreement is in the pack (even n=small, honest). |
| H23 | AX EU region / retention not actually on stage. Don’t fake Belgium. Phoenix **local**. AX = config + one paragraph. |
| H24 | Tracing PII to Phoenix (LLM02). Marta: redact before export. |
| H25 | Devtools TAM. Anika: only if wedge is “EU agent shipping,” global category “release evidence OS.” |
| H26 | Dogfooding nothing. The system-under-test must be a real TF agent (stub/ListGuard), not `print("hello")`. |

**Verdict before salvage:** **OUT** as “AI Act compliance platform.” **SALVAGE** as Exhibit — evidence pack for a named TF agent.

---

## 3. Council answers (they do not get to keep the workshop title)

**Jules:** Jev is irrelevant here unless used as the agent’s judge. Default remains TF JSON.

**Niklas:** Two TF knobs: (1) agent observe/judge models (2) **eval** judge model, possibly the same Fast flavor, logged as a separate purpose=`eval`. That *is* Token Factory as engine of the evidence, not just the toy agent.

**Owen:** Exhibit is a **layer** on the harness, not a second runtime. Spans wrap observe → judge → policy → generate. Policy still has no LLM.

**Mira:** Company slide: “EU teams shipping agents need a file counsel can attach to a DPIA / risk committee, produced while they work.” Not “we replace Arize.” Arize/Phoenix are how traces move. You sell the **mapping, the pack, the gate, the TF judges.** Wedge EU. Category: agent release evidence. I will take a Monday meeting *if* a named platform lead exists. I will not lead a ‘compliance consultancy.’

**Amira:** Demo script is the hostile job we already have. Then the pack. Table on `/eval` stays.

**Kenji:** Phoenix in-process (`px.launch_app` or local OTLP) is 45 minutes. If it fails, **file exporter** (JSONL spans) is the fallback. Do not Docker-compose AX on Tuesday.

**Marta:** Span processor redacts IBAN/phone/email **before** export. No user-URL fetch (already). DEMO_TOKEN still on POST. Phoenix UI is localhost/preview — don’t dump playbooks into span attributes (LLM08).

**Camille:** Observability UIs are the *other* slop (dark navy + electric purple + flame graphs). Exhibit uses the **same paper/ink desk**. The pack is a document. The trace is a **table of spans**, not a neon waterfall.

**Leila:** Use OpenInference semantic conventions. Manual spans for `CHAIN` (job), `LLM` (observe/judge/generate), `GUARDRAIL` or custom `policy` as a CHAIN span with attributes `harness.action`, `harness.reason_codes`. Do not invent a parallel telemetry schema.

**Pieter:** Risk-tier sentence is mandatory:

> “This product is limited-risk decision support for *engineering evidence*. It is not a conformity assessment, not legal advice, and not a declaration that your agent is high-risk or not. Counsel classifies. We produce artifacts.”

**Sofia:** Eval table columns are about **judges scoring traces**, plus the agent quality metrics we already specified. Hostile→allow remains 0 on the agent. New metric: **schema-error rate of eval judges** (ours 0 by construction if Choice/Noul).

---

## 4. Recalibrated four-product board

Same jury, Exhibit included.

| Rank for *this* jury | Product | Survives if |
|---|---|---|
| 1 | **ListGuard** | Named human + public listings + injection-first |
| 2 | **ClauseWindow** | Named lawyer + 1M measured |
| 3 | **Exhibit** | Named platform/governance human + pack you can download + TF evals + **no compliance claim** |
| 4 | **MenuMind** | Platform onboarding human, fail-closed allergens |

**Anika’s note:** Exhibit can *overtake* ListGuard for Accel if the founder *is* a governance/platform person. Otherwise ListGuard is still the sharper application-layer wedge.

**Markus’s note:** Exhibit scores responsible-design **only if** the copy is humble. Overclaim and it scores worse than MenuMind.

**Dima’s note:** Exhibit is the only one that makes **evals on TF** the product. That can win criterion 3 if the three-column table is about judges.

**Default unchanged if no new named human:** ListGuard.  
**Pick Exhibit if** the human who replied is Head of AI / DPO-engineer / platform, not T&S or GC or restaurant.

---

## 5. Need of the hour (honest)

- **Yes, with a caveat.** European teams have RAI PDFs and agents, and nothing connecting them. The Act makes that operational. Omnibus may slip Annex III dates; **Article 111 significant modification** still makes “we’ll log later” a trap for agents that change weekly.
- **No:** “Fines on 2 August 2026” as a scare line. We already forbade that.
- Why-now chips that are *true this month:* OpenInference as the span dialect; Phoenix local in pip; TF JSON judges cheap enough to eval 100% of traces; our harness already has receipts/policy/human Accept — Exhibit is the **export and mapping**, not a new religion.

---

## 6. Startup capacity

| | |
|---|---|
| **Wedge** | EU team shipping one agent (T&S, support, catalog, legal) needs a pack for counsel / risk committee |
| **Category** | Agent release-evidence OS (global) |
| **Not** | Phoenix reseller, ISO 42001 consultancy, CE-mark mill |
| **Who pays** | Head of AI Platform + Legal/DPO as economic buyer of *time* (not of a fine they don’t understand) |
| **Moat if any** | Article-tagged pack schema + TF-native judges + harness policy-in-code (closed sets). Weak moat; distribution and honesty are the play |
| **Accel fit** | Borderline. Better than HireSignal. Worse than ListGuard unless founder-market is governance |

---

## 7. Demo (Jonas / Priya)

90 seconds, hostile first.

1. Named human in chrome: `for {{NAME}}, Head of AI Platform`.
2. Run `lg-inject-01` (or stub equivalent) through the TF agent.
3. Spans table: observe / judge / policy (action QUEUE). No purple waterfall.
4. Eval row: `injection_caught = true` (TF JSON). Proprietary judge column may be n/a.
5. Human annotation: operator clicks **Confirm queue** — receipt `actor=human`.
6. Download `exhibit.json` (and HTML). Show keys `art12_trace_ids`, `art14_review`, `art15_eval`, `limitations`.
7. Sentence: “Observability cannot classify your system. Counsel does. This is the file.”

---

## 8. What observability can prove vs what it cannot

**Can (if we actually built it):**
- This run happened (time, models, endpoint ids, hashes).
- Policy branch and reason codes (code, not a vibe).
- A named human saw this span and confirmed or overrode.
- This eval dataset, this threshold, this CI exit code.
- PII was redacted before export (process).

**Cannot:**
- Whether the system is high-risk, prohibited, or GPAI.
- Fairness of the world.
- That a judge is “true” without human agreement.
- Conformity, CE, notified body.
- AX EU residency on Tuesday (we did not turn on Belgium).

Those “cannot” lines go in the pack under `limitations[]`. Markus will look.

---

## 9. OSS / partners (Owen)

| Steal | Role |
|---|---|
| OpenTelemetry + OpenInference | Span dialect |
| arize-phoenix / phoenix.otel | Dev collector (accelerator) |
| Our harness | Agent + policy + receipts |
| TF JSON judges | Art. 15 evals (engine) |
| Presidio/regex redact | Art. 10 before export |
| **Do not** | Hand-rolled span JSON as a parallel standard |
| **Do not** | Require Arize AX account Tuesday |
| **Do not** | LangGraph, vector DB |

n8n out of path. Lovable out of path.

---

## 10. SecOps deltas (Marta / Dev)

On top of Articles XI:

- Span attributes: **no raw description** in export if it contains PII; store hash + redacted preview.
- Phoenix exporter is localhost/OTLP. No user-defined OTLP URL in the UI (SSRF). Env `OTEL_EXPORTER_OTLP_ENDPOINT` only, allowlist `127.0.0.1` / `localhost` / configured host.
- Eval judges never get tools.
- Exhibit JSON cells: same `=+@-` escape if opened in sheets.
- Don’t log TF keys in span attributes.

---

## 11. UX (Camille)

Same MASTER.md. Additional:

- Trace view = `<table>` of spans (name, kind, ms, tokens, action). Not a flame graph.
- Pack preview = document (Source Serif for the “limitations” paragraph only).
- Copy banned: “compliant,” “certified,” “AI Act ready,” “high-risk covered,” purple “insights.”
- Copy required: “Not legal advice.” “Counsel classifies.”

---

## 12. Primitives to land now (so any of the four can reuse them)

These go into `app/harness/` without implementing the full Exhibit UI:

1. `exhibit_schema.py` — pack Pydantic model (art12/14/15/72/50/11 + limitations)
2. `otel.py` — optional OpenInference spans; no-op if packages missing
3. `redact.py` — shared IBAN/phone/email (already started in eval_runner)
4. `eval_judges.py` — TF JSON questions for `injection_caught`, `disclosure_present`, `schema_valid`
5. Span names locked: `harness.job`, `harness.observe`, `harness.judge`, `harness.policy`, `harness.generate`, `harness.eval`

Full Exhibit skin remains T12+ **if chosen**.

---

## 13. Decision rule (Monday 18:00)

| Named human is… | Build |
|---|---|
| T&S / marketplace | ListGuard |
| Lawyer / GC | ClauseWindow |
| Platform onboarding / multi-site food | MenuMind |
| Head of AI / DPO-engineer / “we ship agents in the EU” | **Exhibit** |
| Nobody | ListGuard (unchanged default) |

Do not combine Exhibit *and* ListGuard as two skins on Tuesday. If you pick ListGuard, the exhibit **primitives** still emit a pack from receipts (stretch after T18). If you pick Exhibit, the system-under-test is the stub agent (or ListGuard if already built — it won’t be).
