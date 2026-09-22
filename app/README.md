# Harness (Phase 0 + sittings 7–8)

Shared runtime for ListGuard / ClauseWindow / MenuMind / Exhibit (pack layer).

Spec sources of truth (do not contradict):

- `../specs/constitution.md`
- `../specs/shared/harness.md`
- `../specs/design/MASTER.md`
- `../specs/security/owasp-threat-model.md`

Skins are **not** implemented. `SKIN=stub` until T12. Do not ship two skins.

## Run

```bash
cd app
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # add DEMO_TOKEN and TF keys when you have them
uvicorn web.app:app --host 0.0.0.0 --port 8000
```

`GET /health` → `ok`  
`GET /` → operator chrome (paper/ink, no purple)  
`POST /jobs` JSON `{"title":"…","description":"…"}` — **no URL fetch**

## Tests

```bash
cd app && pytest -q
```

## Tuesday

Implement **one** skin from `specs/<skin>/tasks.md` starting at T12. Do not restyle `web/static/app.css` without editing `specs/design/MASTER.md` first.
