# Shared harness
## Runtime that every skin sits on
Owner: Arjun Mehta + Nora Okonkwo  
Consumers: ListGuard, ClauseWindow, MenuMind, Exhibit (pack layer on any skin)

If this document and a product plan conflict on the **runtime**, this document wins. Product plans may add questions, policy functions, and UI.

---

## 1. Goal

A single Python package `harness/` that implements:

```
untrusted input → intake → observe(TF) → judge(TF JSON) → policy(code) → generate?(TF) → receipt
```

Skins supply: input schema, observe prompt, question set, policy function, UI.

---

## 2. Package layout

```
app/
  harness/
    intake.py          # mime, size, hash, optional PII
    tf_client.py       # OpenAI-compat, two endpoints
    observe.py         # text / vision / long-context
    decisions.py       # Choice | Score | Noul + DecisionBackend
    backends/
      tf_json.py       # DEFAULT — Nemotron/Qwen3-8B json_schema
      jev.py           # optional flag
    policy.py          # PolicyResult allow|queue|block
    receipts.py        # sqlite + append-only reviews
    eval_runner.py     # three-column table; offline gold if last_report missing
    exhibit_schema.py  # pack model (not a second skin)
    exhibit_build.py
    otel.py
    redact.py
    eval_judges.py
  skins/
    stub.py            # until T12
    listguard/
    clausewindow/
    menumind/
    exhibit/
  web/                 # FastAPI + templates
  fixtures/
  evals/
  pyproject.toml
```

Tuesday: create `skins/<one>/` only.

---

## 3. Types (canonical)

```python
from enum import Enum
from typing import Literal, Any
from pydantic import BaseModel, Field

class Action(str, Enum):
    allow = "allow"
    queue = "queue"
    block = "block"

class ChoiceQ(BaseModel):
    kind: Literal["choice"] = "choice"
    instructions: str
    criteria: dict[str, str]  # id -> definition; MUST include "other" or "unknown" if open-world risk

class ScoreQ(BaseModel):
    kind: Literal["score"] = "score"
    instructions: str
    criteria: list[str]       # ordered labels, mapped to 0..n-1

class NoulQ(BaseModel):
    kind: Literal["noul"] = "noul"
    instructions: str
    # true/false definitions optional

Question = ChoiceQ | ScoreQ | NoulQ

class ChoiceA(BaseModel):
    kind: Literal["choice"] = "choice"
    value: str
    probabilities: dict[str, float]

class ScoreA(BaseModel):
    kind: Literal["score"] = "score"
    value: float              # 0..len(criteria)-1
    label: str

class NoulA(BaseModel):
    kind: Literal["noul"] = "noul"
    p_true: float             # 0..1

Answer = ChoiceA | ScoreA | NoulA

class ObserveResult(BaseModel):
    state: dict[str, Any]     # structured, citations where possible
    raw_model: str
    tokens_in: int
    tokens_out: int
    latency_ms: int

class PolicyResult(BaseModel):
    action: Action
    reason_codes: list[str]
    human_required: bool
    notes: str = ""

class Receipt(BaseModel):
    id: str
    ts: str
    skin: str
    input_hash: str
    model_ids: dict[str, str]      # observe, judge, generate?
    endpoint_ids: dict[str, str]
    flavor: dict[str, str]         # fast|base|dedicated
    questions: dict[str, Question]
    answers: dict[str, Answer]
    policy: PolicyResult
    actor: str = "system"
    euro_estimate: float = 0.0
```

---

## 4. DecisionBackend

```python
class DecisionBackend(Protocol):
    name: str
    def decide(self, state: dict, questions: dict[str, Question]) -> dict[str, Answer]: ...
```

### 4.1 Default: `TfJsonBackend` (Article I)

- Model: `nemotron-3-nano` or `Qwen/Qwen3-8B` on Token Factory **Fast** (or the cheaper/faster available instruct model).
- Request: single chat completion, `response_format` = JSON schema derived from the question dict.
- The model MUST return only keys that exist in `questions`. Unknown keys dropped.
- Post-validate: Choice value ∈ criteria; Noul clipped to [0,1]; Score clipped to range.
- On schema fail: **retry once**, then return a synthetic `queue`-forcing answer (`unknown` / `p_true=0.5`) and reason_code `judge_schema_fail`. Never crash the request.

JSON schema sketch for a mixed batch:

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["<q1>", "<q2>"],
  "properties": {
    "<choice_q>": {
      "type": "object",
      "required": ["value"],
      "properties": {
        "value": {"type": "string", "enum": ["ok", "counterfeit", "other"]},
        "probabilities": {"type": "object"}
      }
    },
    "<noul_q>": {
      "type": "object",
      "required": ["p_true"],
      "properties": {"p_true": {"type": "number", "minimum": 0, "maximum": 1}}
    }
  }
}
```

### 4.2 Optional: `JevBackend`

- Only if `DECISION_BACKEND=jev` and credentials work Sunday night.
- Same `Question` objects mapped to TypeSafe Choice/Score/Noul.
- Eval table may add a fourth column. Product still functions with flag off.

---

## 5. Token Factory client

```python
class TFClient:
    def complete(self, *, purpose: Literal["observe","judge","generate"],
                 messages: list, json_schema: dict | None,
                 images: list[str] | None, max_tokens: int) -> TFResponse
```

Config (env):

| var | purpose |
|---|---|
| `TF_BASE_URL` | Token Factory OpenAI-compat |
| `TF_API_KEY` | |
| `TF_MODEL_OBSERVE` | GLM-5.3-Flash or Qwen3-VL |
| `TF_MODEL_JUDGE` | Nemotron Nano or Qwen3-8B |
| `TF_MODEL_GENERATE` | Qwen3-8B or GLM-5.1 |
| `TF_ENDPOINT_OBSERVE` | dedicated id if any |
| `TF_ENDPOINT_JUDGE` | dedicated id if any |

**Two-knob minimum:** different `TF_MODEL_JUDGE` vs `TF_MODEL_OBSERVE` (Fast vs VL/1M). If dedicated IDs exist, log them on every receipt.

Pricing table lives in `harness/prices.py` (edit Tuesday morning from the TF console). Eval uses this file so €/job is reproducible.

---

## 6. Intake (security-hard)

See `specs/security/owasp-threat-model.md` §6. This section **replaces** “accept a URL”.

- **Forbidden:** any server-side fetch of a user-supplied URL (`http(s)`, `file`, `gopher`, `169.254.169.254`). Listing URLs are display-only strings.
- Max upload **8 MB** read into memory first. Then magic-byte sniff. Allowed MIME: `image/jpeg, image/png, image/webp, application/pdf, text/plain, application/json`.
- Images: Pillow re-encode, max 4096×4096, EXIF stripped. PDF: ≤100 pages, reject encrypted. Save `uploads/{uuid}.{ext}` only after `realpath` stays under `uploads/`.
- SHA-256 of **original** bytes = `input_hash`.
- Optional Presidio on free-text that will be **logged** (not on legal party names in the ClauseWindow reading pane).
- Empty input → 400, no model call.
- `DEMO_TOKEN`: if env set, all POST routes require header `X-Demo-Token` or form/query `token` or fail 401. HTML fields are empty (never prefilled).

---

## 7. Policy engine

```python
def apply_policy(skin: str, answers: dict[str, Answer], state: dict) -> PolicyResult:
    ...
```

- Each skin registers `policy_<skin>(answers, state) -> PolicyResult`.
- **No LLM inside policy.** Thresholds in `skins/<skin>/policy.yaml`.
- Default deny: if judge failed, `queue` + `human_required=True`.

---

## 8. Generate (optional, post-gate)

Only if `action != block` and the skin asks for a rationale/redline/upsell.

- Model: `TF_MODEL_GENERATE`.
- Prompt includes **only** state slices the policy allowed.
- Max tokens capped per skin (ListGuard rationale ≤ 80 tokens).
- Generate MUST NOT change `action`.

---

## 9. Receipts

SQLite table `receipts` with the `Receipt` JSON.  
UI: `/receipts/{id}` raw JSON. Demo shows this panel.

Kill switch: env `AUTO_ALLOW=0` (default 0). When 0, all `allow` become `queue` except in eval runner. **Demo sets AUTO_ALLOW=1 for the clean-success card only if the operator toggles the switch on screen.** Default for live traffic in the demo is: show what *would* allow, still require toggle.

Simpler Tuesday rule: **never auto-allow in the UI**; show recommended action; human clicks “accept recommendation.” Eval runner may simulate auto.

Accept persists `actor=human` on the sqlite receipt. Override sets stored `action=queue` with reason_code `human_override`. Reviews are append-only. Reconstruct jobs from sqlite if RAM is empty.

---

## 10. Eval runner

```
python -m harness.eval_runner --skin listguard --split gold
```

Reads `evals/<skin>/gold.jsonl`.  
For each row: run vanilla_tf (observe+judge, policy **identity allow**) and ours (full). Proprietary column is a **scripted adapter** (`adapters/proprietary.py`) that calls OpenAI/Anthropic if keys exist; if not, skip column and mark `n/a` — do not invent numbers.

Writes `evals/<skin>/last_report.md` + `last_report.json`.  
The demo page `/eval` renders that file. **This is the table on screen.**

If `last_report.json` is missing, `/eval` runs gold through the live pipeline with `eval_mode=True` (no TF required). Proprietary and vanilla TF stay `n/a`. Notes MUST say the run is offline/unconfigured. Do not invent numbers. Hostile→allow on that run must be 0.

---

## 11. FastAPI surface (all skins)

| method | path | |
|---|---|---|
| GET | `/` | skin home (upload / paste) |
| POST | `/jobs` | create job, sync is OK for Tuesday |
| POST | `/jobs/hostile` | one-click skin `HOSTILE_FIXTURE` |
| GET | `/jobs/{id}` | result + receipt |
| POST | `/jobs/{id}/accept` | persist `actor=human` |
| POST | `/jobs/{id}/override` | persist queue + `human_override` |
| GET | `/eval` | three-column table |
| GET | `/receipts/{id}` | |
| GET | `/exhibit/{id}` | evidence pack (layer, not a second skin) |
| POST | `/kill` | set freeze (303 Location `/`, not RedirectResponse) |

One process. `SKIN=stub` until T12, then `listguard|clausewindow|menumind|exhibit`. Do not ship two skins.

---

## 12. Non-goals (harness)

- Multi-tenant auth, SSO, billing (optional `DEMO_TOKEN` only).
- Streaming unless a skin’s demo dies without it.
- Fine-tune jobs inside the request path.
- MCP, LangGraph, n8n, vector stores, browser agents in the critical path.
- Fetching user URLs. Markdown-to-HTML of model text. Tailwind/shadcn default themes.

---

## 13. Test contract (pytest, no network)

| test | asserts |
|---|---|
| `test_choice_unknown_forced_queue` | missing/invalid choice → queue |
| `test_policy_no_llm` | monkeypatch judge; policy still deterministic |
| `test_receipt_fields` | all Article VI fields present |
| `test_generate_cannot_flip_action` | |
| `test_injection_fixture_not_allow` | each skin’s hostile id ↛ allow |
| `test_rejects_url_fetch` | body `{"url":"http://127.0.0.1"}` → 400 |
| `test_upload_rejects_html_polyglot` | |
| `test_upload_rejects_oversize` | |
| `test_jinja_escapes_script_in_description` | |
| `test_receipt_id_is_uuid` | |
| `test_csp_header_present` | |
| `test_demo_token_required_when_set` | |
| `test_budgets_short_circuit_before_tf` | |
| `test_accept_persists_actor_on_receipt` | sqlite `actor=human` after Accept |
| `test_override_sets_queue` | stored action becomes queue |
| `test_exhibit_from_receipt_without_ram` | pack 200 after jobs.clear() |
| `test_eval_offline_hostile_not_allow` | ours hostile→allow = 0, n>0 |
| `test_observe_judge_defaults_differ` | Article I two knobs |

Skins add domain tests on top.

---

## 14. Budgets (`harness/budgets.py`)

| Budget | Value |
|---|---|
| Upload bytes | 8 MB |
| Image pixels | 4096 × 4096 |
| PDF pages | 100 |
| Observe max_tokens | 2048 (ClauseWindow 4096) |
| Judge max_tokens | 1024 |
| Generate max_tokens | skin cap (ListGuard 80) |
| Jobs / token / min | 10 |
| Concurrent TF | 2 |
| TF timeout | 45s observe / 15s judge |
| Retries | 1 |

Exceed → HTTP 413/429, **no** TF call.

---

## 15. HTTP hard-ening

- FastAPI `docs_url=None`, `redoc_url=None` when `ENV=demo`.
- Headers: CSP as in the threat model, `X-Content-Type-Options: nosniff`, `Referrer-Policy: no-referrer`, `X-Frame-Options: DENY`.
- Jinja `autoescape=True`. Templates never `|safe` on user/model fields.
- `/eval` renders metrics + fixture ids, not raw IBAN/contract bodies.
- Reason codes are **enums we emit**, not free-form model strings, when used as chips.

---

## 16. UI chrome (MASTER.md)

Templates use `app/web/static/app.css` only. Tokens, type, layout, and bans are in `specs/design/MASTER.md`. The harness serves:

- Top bar: wordmark, skin name, **named human**, kill switch, `/eval`
- Left intake, right work surface
- Footer: risk-tier sentence
- Receipt strip in IBM Plex Mono

Skins do not ship a second stylesheet.
