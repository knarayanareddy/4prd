# ClauseWindow — plan

---

## 1. Architecture

```
PDF → Docling or pypdf (text)
    → observe TF 1M  (clause map JSON)
    → batches of ≤10 clauses → judge TF JSON
    → policy vs playbook.yaml
    → redlines.json
    → optional python-docx
    → heatmap UI
```

TF knobs: (1) 1M observe model (2) dedicated EU endpoint and/or separate judge model.

---

## 2. Stack

| piece | choice |
|---|---|
| PDF | `pypdf` first (fast); Docling if layout is junk |
| Observe | GLM-5.3-Flash 1M |
| Judge | Nemotron/Qwen3-8B JSON |
| Docx | `python-docx` comments on a generated doc (not true OOXML tracked changes if too hard — comments are enough) |
| UI | FastAPI: left outline, right clause, heatmap color = aligned/fallback/walkaway |

---

## 3. Pre-warm

Sunday: extract text of trap PDF, store `fixtures/clausewindow/trap.txt`.  
Tuesday observe can take `text` or `pdf`. Demo may upload PDF; if TTFT>12s Sunday, demo uploads **and** shows the measured number; fallback to pre-extracted text mid-demo if it hangs.

---

## 4. Playbook

`skins/clausewindow/playbook/acme-v1.json` — 6 rules, written with the named lawyer Monday. If no lawyer, use the sample in the spec (liability, EEA transfer, etc.) and name a lawyer who reviewed the *sample* playbook.

---

## 5. Chunked baseline (vanilla / proprietary)

Vanilla TF column: split text every 1500 tokens, ask the **judge model** “is there a liability cap?” per chunk — designed to miss Schedule 4 if the cap is not in that chunk.  
This is the honest “chunking is the bug” comparison.

---

## 6. Cuts

| fail | cut |
|---|---|
| 1M model unavailable | Qwen long-context; still no *policy* chunking |
| python-docx | JSON only |
| >80 clauses | first 80 + warning |
| generate comments | reason_codes only |
