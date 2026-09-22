# ListGuard — plan
How we build the spec on the shared harness. Tuesday 23 Sep 2026.

---

## 1. Architecture

```
browser → FastAPI (SKIN=listguard)
        → intake (hash, size)
        → observe  TF_MODEL_OBSERVE  (VL JSON)
        → judge    TF_MODEL_JUDGE    (JSON schema, 6 questions)
        → [optional cached Tavily]
        → policy   code (policy.yaml thresholds)
        → generate TF_MODEL_GENERATE (P1 rationale ≤80 tok)
        → sqlite receipt
        → HTML card UI
```

TF knobs (Article I): (1) VL observe ≠ JSON judge models (2) dedicated EU endpoint if credits allow.

Jev: `DECISION_BACKEND=tf_json` default.

---

## 2. Stack

| piece | choice | why |
|---|---|---|
| API/UI | FastAPI + Jinja2 + one CSS file | survives without Lovable |
| Models | GLM-5.3-Flash or Qwen3-VL ; Nemotron Nano or Qwen3-8B | TF shortlist |
| Images | stored under `fixtures/listguard/` ; uploads in `uploads/` | |
| Tavily | `fixtures/tavily/*.json` keyed by brand | no live pitch |
| Eval | `harness.eval_runner` | constitution |
| Tests | pytest, no network | |

---

## 3. Files this skin adds

```
app/skins/listguard/
  questions.py      # the 6 questions
  observe_schema.py
  policy.yaml
  policy_fn.py
  buckets.json
  router.py         # form fields
evals/listguard/gold.jsonl
fixtures/listguard/{inject,bike,rolex,weapon}.json + images
```

---

## 4. UI (one page)

- Left: drop zone + JSON paste
- Right: card stream (newest first)
- Card: thumb, title, price, bucket chip, action chip, reason codes, Accept / Override-to-queue
- Footer link: receipt JSON
- Top bar: kill switch, `/eval`

No seller profile. No ban button.

---

## 5. Tavily

`should_search(state) := brand and price_too_good>=0.5`  
If cache miss during dev, call Tavily once, save cache. Pitch: cache only.

Snippets appended to judge state as `web_evidence`, wrapped with prefix `UNTRUSTED_WEB:`.

---

## 6. Risks and cuts (Kenji)

| if this fails by | cut |
|---|---|
| VL endpoint 429 | text-only observe, still run judge |
| JSON schema unsupported | tool-call or `json` mode + pydantic repair |
| Tavily | skip P1 |
| generate rationale | skip P1 |
| UI pretty | unstyled HTML is legal |

---

## 7. Proprietary adapter

If `OPENAI_API_KEY` present: same listing → GPT vision “pick a bucket from this list”. Else column `n/a`.
