# MenuMind — tasks

Sunday is mandatory (photos).

---

## Sunday

- [ ] **T0** Named **platform onboarding / multi-site** human + consent. If the only human is a single café owner, **do not build this skin** — switch to ListGuard public listings.
- [ ] **T1** TF VL + judge models live.
- [ ] **T2** Photograph ≥5 menus. Include satay/peanut-sauce item with **no** allergen print (`mm-satay-01`).
- [ ] **T3** Gold n≥40 items. Label peanuts FN risk rows in a `safety` tag.
- [ ] **T4** `allergens.json` EU-14 copied from spec. Do not paraphrase ids.

---

## Phase 0 — harness (09:30–11:00)

**Done** in `app/` (sittings 7–9). Do not rebuild. Skip to T12.

---

## Phase 1 — skin (11:00–12:30)

- [ ] **T12** Observe VL items JSON. Prompt forbids inferred allergens.
- [ ] **T13** 14 Nouls + diet + injection. If too slow by 12:00, amend spec to peanuts/milk/gluten Nouls + `unknown` (write the amendment in `plan.md`).
- [ ] **T14** Policy: satay heuristic, vegan guard, publish disabled. Tests: satay ↛ empty allergens; inject ↛ publishable; vegan+milk rewritten.
- [ ] **T15** Grid UI, red `unknown` chips, **Publish disabled**, export JSON.

---

## Phase 2 — eval (12:30–13:45)

- [ ] **T16** Full gold. Fail if peanut FN > 0 on labelled rows OR any `publishable=true` on unknown.
- [ ] **T17** `/eval` page.

---

## Phase 3 — freeze (13:45–15:00)

- [ ] **T18** Rehearse: satay photo → unknown → export → table. First 15s category sentence (platforms, not OCR).
- [ ] **T19** Submission. Submit 14:45.
- [ ] **T20** Do not enable Publish. Do not add upsell if T16 is red.

---

## Stop-the-line

Peanut FN > 0 → force `unknown` on any item whose name matches a small `danger_foods.txt` (satay, pesto, tiramisu, gomae) and **declare the heuristic**. Do not ship empty allergen sets.
