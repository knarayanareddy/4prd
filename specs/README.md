# Spec-driven development — Accel AI Innovate (23 Sep 2026)

These files are the **source of truth**. Code that disagrees with a spec is a bug, unless the spec is updated first.

Four products survived the same gauntlet. **Ship one.**

## How to use this (Spec Kit loop)

```
constitution.md     ← non-negotiables (never break)
shared/harness.md   ← the runtime every skin sits on
<product>/spec.md   ← WHAT
<product>/plan.md   ← HOW
<product>/tasks.md  ← TODO 09:30–15:00
```

1. Read `constitution.md` once.
2. Harness Phase 0 is already in `app/`.
3. Pick **one** product using the Monday 18:00 table.
4. Execute that skin’s `tasks.md` from T12.
5. Do not combine two skins.

## Which product to implement

| Named human by Monday 18:00 | Build |
|---|---|
| T&S / marketplace (written consent) + public listings | **ListGuard** |
| Lawyer / GC + playbook or public filing | **ClauseWindow** |
| Platform onboarding / multi-site restaurant (not a café) | **MenuMind** |
| Head of AI Platform / DPO-engineer / “we ship agents in the EU” | **Exhibit** |
| Nobody | **ListGuard** (default) |

Do not invent a fifth. Accountant/BD leads are still second-string on the original three, not new specs.

## Layout

```
specs/
  constitution.md
  shared/harness.md
  security/owasp-threat-model.md
  design/MASTER.md
  exhibit-sittings.md          ← jury + council on the 4th product
  sitting-9-four-products.md   ← same jury on all four SDD trees
  listguard/ clausewindow/ menumind/ exhibit/
app/                           ← Phase 0 harness + exhibit primitives
```

Sittings: `sitting-7-live-review.md`, `sitting-8-live-review.md`, `sitting-9-four-products.md`, `exhibit-sittings.md`.

Harness tests: `cd app && pytest -q`. Do not restyle without editing `design/MASTER.md`.
