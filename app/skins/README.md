# Skins — four packages, one process

Developed in parallel (T12). Boot still selects **one**:

```
SKIN=listguard|clausewindow|menumind|exhibit|stub
```

The Tuesday binary still ships one skin. These packages share `harness/` (policy in code, no URL fetch, paper/ink chrome, pack layer at `GET /exhibit/{id}`).

Each package has `ORIGIN.md` (conception + jury) and `BUILD.md` (domain-expert construction). Open a **separate session per folder**; that agent reads those two files first and builds only that skin.

| Package | Domain owner | Closed set | Hostile id |
|---|---|---|---|
| `listguard/` | T&S (listings, not people) | `buckets.json` | `lg-inject-01` |
| `clausewindow/` | Counsel (not legal advice) | `topics.json` + playbook | `cw-inject-01` |
| `menumind/` | Catalog safety (EU-14) | `allergens.json` | `mm-inject-01` |
| `exhibit/` | Platform / DPO-engineer | eval labels | `ex-inject-01` |

`stub/` remains the default until Monday 18:00 names a human.
