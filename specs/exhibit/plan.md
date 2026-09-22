# Exhibit — plan

---

## 1. Architecture

```
POST /jobs  (stub agent on TF JSON)
    → existing pipeline
    → OpenInference spans (or JSONL fallback)
    → TF JSON eval judges on the trace
    → human confirm
    → exhibit.json pack
Phoenix (optional local) ← OTLP
Arize AX                 ← not Tuesday; env sink documented
```

TF knobs: (1) agent judge model Fast (2) eval judge model Fast (logged `purpose=eval`). Observe may be passthrough on Tuesday.

Phoenix = accelerator. If import fails, file exporter.

---

## 2. Stack

Existing FastAPI app. New modules:

- `harness/exhibit_schema.py`
- `harness/otel.py` (optional deps)
- `harness/redact.py`
- `harness/eval_judges.py`
- `skins/exhibit/` (agent = stub questions + pack UI). Pack JSON is a harness layer even if this skin is not chosen.

Optional deps (not required to boot):

```
arize-phoenix
arize-phoenix-otel
openinference-instrumentation-openai
opentelemetry-sdk
```

---

## 3. Cuts (Kenji)

| fail | cut |
|---|---|
| Phoenix import | JSONL spans, still pack |
| TF eval 429 | code eval: `action!='allow' and hostile` as deterministic Art.15 row, **declare heuristic** |
| HTML pack pretty | JSON only |
| AX | README 10 lines |

Do not cut `limitations[]` or the not-legal-advice banner.

---

## 4. SSRF

`OTEL_EXPORTER_OTLP_ENDPOINT` from env only. Allowlist host in `{localhost, 127.0.0.1, ::1}` unless `OTEL_ALLOW_REMOTE=1` (off by default).
