# Sitting 8 — Judges on live specs + live harness (after sitting 7)

The jury was shown `app/` **as it exists after sitting 7** (42 tests, stub skin, Accept/Override, hostile button, `judge=unconfigured`) **and** the spec tree (`constitution.md` v3, `shared/harness.md`, MASTER, four product SDD folders).

They did not re-litigate the four-product board. They scored **Tuesday 16:00 if we demoed this**, and whether the specs still match the code (Article IX).

---

## Jury (verbatim)

**Priya:** “Accept exists. `/eval` still prints n=0 and n/a in every cell while `gold.jsonl` has twelve rows on disk. That is an incomplete form. Named human is a blank in the chrome. If `DEMO_TOKEN` is set, Accept 401s because the field is only on intake. You would not make the top eight.”

**Jonas:** “Override is a log line. The card still says the old action. `/jobs/{id}` has no Accept. Hostile is imported from `skins.stub`, so Tuesday T12 the one-click is the wrong fixture. Specs still talk like the company is three products.”

**Dima:** “`disclosure_present = (... description ...) or True` is the same class of lie as claiming `tf_model_judge` last sitting. The `or True` means you never measured it. Observe and judge default to the same Qwen3-8B — Article I two knobs are not in config. `euro_estimate=0` is honest without tokens; leave it. Do not invent proprietary column numbers.”

**Markus:** “Accept writes a reviews row. `GET /receipts/{id}` still says `actor=system`. Art. 14 is vapour until the stored receipt changes. Override that cannot change the action is not oversight.”

**Anika:** “Four doors. I will not pick for you. I will fail a submission that cannot say which door. Update the lockfiles so an agent cannot ‘discover’ a fifth. Do not ship two skins.”

**Elena:** “Hostile-first is clickable. Why-now is unchanged. The gold ids exist. Running them costs nothing without TF. Do that.”

**Marta:** “`DEMO_TOKEN` is required on all POSTs when set. Kill, Accept, Override HTML forms have no field. The operator who followed the README will freeze or accept and get 401. `/exhibit/{id}` 404s if RAM forgot the job. Receipts are the source of truth.”

**Camille:** “Chrome still not purple. Pass. Put the word ALLOW in the HTML, not only via CSS `text-transform`. Named human unset should be visible, not a missing node. Do not add Google Fonts.”

**Leila:** “Spans write on enter with empty attributes. `harness.policy` never records `harness.action`. Write on exit.”

**Sofia:** “A table of n/a is worse than an honest unconfigured run. Label it offline. Hostile→allow must be 0 on that run. Do not call it TF quality.”

**Kenji:** “`RedirectResponse` is still imported. Hostile fixture is a stub import. Reconstruct jobs from sqlite. Spec the new routes or Article IX is theatre.”

---

## Council vote — implement these, not more strategy

| # | Tweak | Who |
|---|---|---|
| 1 | Persist `actor` + policy on Accept/Override in sqlite | Markus, Priya |
| 2 | Override sets `action=queue` + `human_override`; card updates | Jonas, Markus |
| 3 | Empty `DEMO_TOKEN` fields on kill / accept / override (not prefilled) | Marta |
| 4 | `HOSTILE_FIXTURE` from the loaded skin; 501 if missing | Jonas, Kenji |
| 5 | `GET /exhibit/{id}` and Accept from receipts if RAM empty | Marta, Jonas |
| 6 | Art. 50 disclosure from chrome copy, never `or True` on listing text | Dima, Sofia |
| 7 | Default `TF_MODEL_OBSERVE` ≠ `TF_MODEL_JUDGE` | Dima |
| 8 | `/eval` runs gold offline through the pipeline; proprietary/vanilla stay n/a | Priya, Sofia, Elena |
| 9 | Spec lockfiles: harness routes, four products, MASTER Exhibit row, constitution 3.1 | Anika, Nora, Kenji |
| 10 | Policy span attributes on exit (`harness.action`) | Leila |
| 11 | `for named human unset` visible; ALLOW/QUEUE/BLOCK in the HTML | Camille, Priya |
| 12 | Drop unused `RedirectResponse` import | Kenji |
| 13 | `job.html` has Accept / Override + operator sentence | Jonas |

**Rejected (do not implement):** two skins, n≥40 tonight, fake euros, proprietary/vanilla numbers, Google Fonts, Phoenix/AX docker, HTML exhibit view, picking Monday’s product, Compliant button, prefilled token, fake ALLOW without a TF key.

Monday 18:00 table is unchanged. Default ListGuard. Pack export is a harness layer, not a second skin.

Implemented in this sitting in `app/` + spec one-liners.
