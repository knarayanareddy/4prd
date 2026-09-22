# Exhibit — how this idea was conceived, and what it survived

**This file is for an agent in an Exhibit-only session.** Do not reopen killed ideas. Do not turn this into ListGuard, ClauseWindow, or MenuMind. Do not ship a second skin. Do not claim conformity.

Source of truth (read in this order before writing code):

1. `specs/constitution.md`
2. `specs/shared/harness.md`
3. `specs/design/MASTER.md`
4. `specs/security/owasp-threat-model.md`
5. `specs/exhibit-sittings.md` (Sitting 6 — Exhibit’s own gauntlet)
6. `specs/exhibit/spec.md` → `plan.md` → `tasks.md`
7. This file + `BUILD.md`

If code disagrees with a spec, the spec wins until you change the spec first (Article IX).

---

## 1. Conception

European teams have a Responsible AI PDF and agents in production. Nothing connects them. The AI Act asks for a *history* (records, oversight, robustness, post-market). Observability products store spans. Counsel needs a **file** with article-shaped sections, a named human on reviews, and an honest limitations list.

The user proposed a fourth project from Phoenix / OpenInference / Arize AX. The **same** jury that killed HireSignal ran the same gauntlet.

**Verdict before salvage: OUT** as “AI Act compliance platform.”  
**SALVAGE:** Exhibit — evidence pack for a named Token Factory agent. Phoenix is a span store. AX is a later sink. Token Factory remains the engine of the **agent and the judges**.

**Job:** run the TF agent → traces + TF-native evals + human annotation → download `exhibit.json` mapped to Arts. 12, 14, 15 (stubs for 50, 72, 11).

**Wedge:** EU teams shipping agents. **Category:** agent release-evidence OS. **Not:** Phoenix reseller, ISO 42001 consultancy, CE-mark mill.

**Why now (honest):** OpenInference; Phoenix local; TF JSON judges cheap enough to score traces; Article 111 “significant modification” makes weekly agent changes a record-keeping problem even if Annex III dates slip. **Forbidden scare line:** “fines on 2 August 2026.”

---

## 2. What the jury did to it

Survived as rank 3 **only** if the named human is Head of AI Platform / DPO-engineer / “we ship agents in the EU.” Markus: overclaim and it scores worse than MenuMind.

| Seat | What they did |
|---|---|
| **Markus** | Pitch that says “AI Act compliant” or “high-risk ready” scores zero. Map *engineering artifacts* to article numbers. Do not sell a CE mark. |
| **Dima** | If Phoenix is in the middle and TF is “the agent we watched,” criterion 4 fails. Evals run on TF JSON. Agent runs on TF. Phoenix = Tavily bucket. |
| **Anika** | “We installed OpenInference” is not a company. Company = pack schema + TF-native judges + release gate. If the slide is a dashboard, she checks her phone. |
| **Jonas** | Hold `exhibit.json` with article sections and a human name on an annotation. Not a Grafana tour. Not a purple waterfall. HTML pack view is **P1** (sitting 8 cut it from Tuesday). |
| **Priya** | Named person. Frozen eval on the *agent*. Three-column table on the *eval judges*. |
| **Elena** | Omnibus may slip dates; Art. 111 still punishes significant modification. Instrumentation now is the hour. |
| **Leila** | OpenInference conventions. Do not invent a parallel span schema. Spans: `harness.job\|observe\|judge\|policy\|generate`. Policy span records `harness.action` **on exit**. |
| **Sofia** | LLM-judge without human agreement is worse than no metric. Heuristic fallback must be labelled `heuristic`. `disclosure_present` is chrome copy, never `or True` on listing text. |
| **Camille** | Observability slop (dark navy + electric purple + flame graphs) is banned. Same paper/ink desk. Trace = `<table>` of spans. |
| **Marta** | Redact IBAN/phone/email **before** export. No user-typed OTLP URL (SSRF). Env only, localhost allowlist. |

**Hole catalog (must stay killed):** H19 Phoenix/AX wrapper as product; H20 conformity theatre; H21 sleepy dashboard; H22 uncalibrated LLM-as-judge as Art. 15; H23 fake Belgium; H24 PII in spans; H25 pure devtools TAM; H26 dogfooding `print("hello")`.

---

## 3. Sittings that already happened (do not re-litigate)

| Sitting | Outcome for Exhibit |
|---|---|
| Sitting 6 | Salvage as pack, not compliance platform. Primitives listed. |
| Sitting 7 | Primitives landed: schema, otel JSONL, redact, eval_judges, `GET /exhibit/{id}`, Accept reviews. |
| Sitting 8 | Art. 50 from chrome; pack from receipts if RAM empty; policy span attributes; HTML view demoted to P1. |
| Sitting 9 | Tasks T13/T15/T16 JSON already done in harness. Do not wrap spans twice. Seed `evals/exhibit/gold.jsonl`. |

The **system under test** is the stub-shaped TF agent (observe passthrough until keyed + TF JSON judge + code policy). You are not building ListGuard in this session; you may dogfood the stub agent.

---

## 4. Monday 18:00 (resolved for this session)

This session **is** Exhibit. Fill `NAMED_HUMAN` as Head of AI / DPO-engineer. No Compliant / Certified / High-risk OK button, ever.

---

## 5. Risk-tier sentence (footer, unchanged)

> Limited-risk decision support for engineering evidence. Not legal advice. Not a conformity assessment. Counsel classifies. We produce artifacts.
