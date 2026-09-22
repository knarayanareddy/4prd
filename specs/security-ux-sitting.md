# Sitting 5 — SecOps, OWASP, UI UX Pro Max
Scaffold of `app/harness/` is **blocked** until this sitting is accepted.

| Seat | Job |
|---|---|
| **Marta Kruk** | SecOps / AppSec, OWASP Top 10:2025 |
| **Dev Patel** | OWASP LLM 2026 + Agentic ASI |
| **Camille Voss** | UI UX Pro Max, anti-slop, WCAG |

They read constitution v3, the harness, and the three specs. They did not ask permission to be kind.

---

## Marta (web)

> “You specified a control plane and then left `image_url` as a cultural possibility. That is SSRF. You specified Jinja and did not say autoescape. That is XSS the first time a listing contains `<script>`. You specified 20 MB uploads. That is a zip bomb and a Denial-of-Wallet on GLM-5.3-Flash. Receipts as `/receipts/1` is IDOR of a contract. FastAPI `/docs` on a public preview is a gift.
>
> I will sign the harness when: no user URL fetch, magic-byte uploads, UUID receipts, budgets before TF, CSP, DEMO_TOKEN, tests in §13. Not when someone writes ‘we take security seriously’ in the README.”

## Dev (LLM)

> “LLM01 is not a fixture, it is the architecture. You cannot prompt your way out. You *can* make sure the model never has a tool that matters. You were already close. The remaining sins: Tavily snippets as trusted evidence, generate text piped into HTML, `/eval` as a second exfil channel, 1M context as an unbounded bill.
>
> ASI09 will kill you on stage if ALLOW is a big green cookie. The human will click it. Make allow visually boring and the hostile card loud.”

## Camille (Pro Max)

> “If I unfocus my eyes and I still know it was an AI demo, you lost Jonas without a word. Purple hue, Inter, 16px radius, gradient, three cards, sparkle. That is the prior. These products are **desks**: newsroom intake, clerk’s paper, kitchen rail. Paper and ink. IBM Plex. Radius 2. No shadow. Status is a word.
>
> I persisted `specs/design/MASTER.md`. An agent that later ‘polishes’ it back to indigo has failed the skill. Industry rules: T&S is not cyber-neon. Legal is not glass. Food ops is not avocado Instagram.”

---

## Fights

**Kenji vs Marta on DEMO_TOKEN.** Kenji: “one more thing to forget on stage.” Marta: “the preview URL is public.” **Resolution:** token in `.env`, pre-filled in a hidden field on the operator machine, 15 minutes. If it costs the demo, print it on a sticky.

**Leo vs Camille on “wow.”** Leo: “MenuMind needs a gasp.” Camille: “The gasp is the yellow UNKNOWN on satay, not a gradient. If you need purple to be taken seriously you do not have a product.” **Resolution:** MASTER.md wins.

**Arjun vs Dev on Tavily.** Arjun: “brand evidence.” Dev: “indirect injection.” **Resolution:** already in ListGuard spec — snippets untrusted, policy does not read them, cache only.

**Jonas (absent) would ask:** does it look like a tool someone already uses at 07:00? If yes, Camille succeeded.

---

## Accepted amendments (already written)

- Constitution Articles **XI** (containment) and **XII** (visual system)
- Harness §§6, 12–16 (intake, budgets, HTTP, UI chrome, security tests)
- `specs/security/owasp-threat-model.md`
- `specs/design/MASTER.md`
- Security + UX acceptance criteria on all three product specs
- Phase 0 tasks now include CSP, DEMO_TOKEN, XSS tests, app.css

## Scaffold gate

`app/harness/` may be generated **only** from:

1. `constitution.md` (incl. XI–XII)
2. `shared/harness.md`
3. `design/MASTER.md`
4. `security/owasp-threat-model.md`

If the generator emits indigo, Inter, a URL field, or `|safe`, delete the tree and start again.
