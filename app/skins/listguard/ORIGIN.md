# ListGuard — how this idea was conceived, and what it survived

**This file is for an agent in a ListGuard-only session.** It is the memory of *why* this product exists. Do not reopen killed ideas. Do not turn this into ClauseWindow, MenuMind, or Exhibit. Do not ship a second skin.

Source of truth (read in this order before writing code):

1. `specs/constitution.md`
2. `specs/shared/harness.md`
3. `specs/design/MASTER.md`
4. `specs/security/owasp-threat-model.md`
5. `specs/listguard/spec.md` → `plan.md` → `tasks.md`
6. This file + `BUILD.md`

If code disagrees with a spec, the spec wins until you change the spec first (Article IX).

---

## 1. Conception

Marketplace moderators see listings **after** they are live. DSA notice-and-action duties are live. LLM classifiers invent policy buckets, miss the photo, and can be jailbroken from the description field. Auto-allowing the tail is how you get a lawsuit; auto-banning *people* is how you become high-risk.

**Job:** given a listing (title, description, price, photos), recommend `allow | queue | block` **the listing** (not the seller), with reason codes, at ingestion speed, 0 invented labels, EU-hosted Token Factory.

**Wedge:** EU illegal-goods + counterfeit. **Category:** ingestion control plane for marketplaces (global).

**Why now (honest):** DSA duties are live; open VL + JSON-judge on Token Factory is cheap enough to run on 100% of inventory; a calibrated queue is how you stop auto-allowing the 8% that becomes a lawsuit. Do not pitch “fines tomorrow.”

Conceived as Accel AI Innovate Amsterdam (23 Sep 2026) application-layer work. Token Factory is the **engine**. Jev/Tavily/Lovable/n8n/ElevenLabs are accelerators, never the title.

---

## 2. What the jury did to it

Same panel that killed HireSignal (“we make hiring legal”). ListGuard **survived** as rank 1 if the named human is T&S / marketplace.

| Seat | What they did |
|---|---|
| **Anika (Accel)** | Application-layer, not a harness company. Default if nobody consents. Four doors is indecision — this session already picked ListGuard. |
| **Dima (Token Factory)** | Two knobs: VL observe ≠ JSON judge. Closed set. Invented-label rate = 0. Honest `judge=unconfigured` if no TF key. |
| **Isabel (Prosus)** | No Prosus/OLX logo-jacking. Rhyme is allowed. Named consented human. |
| **Jonas (product)** | Hostile-first. Hold a card: QUEUE, bucket, Accept. One-click `lg-inject-01`. Override must change the stored action. |
| **Priya (form)** | Named human in chrome. Frozen eval n≥40 (Sunday). Three-column `/eval`. Accept persists on **sqlite**, not RAM. |
| **Markus (responsible design)** | Never ban/score a *person*. Limited-risk if fail-closed. Human Accept is a record. |
| **Elena (why-now)** | DSA is real. Seed fixtures must be **in the repo**. |
| **Marta / Dev (SecOps)** | Never fetch a user URL. Description is the injection surface. DEMO_TOKEN on POSTs, never prefilled. Uploads in `uploads/`, not `/tmp`. |
| **Camille (anti-slop)** | Paper `#F3EFE7` + ink `#1C1915`. Plex. Radius 2. No purple/gradient/shadow/Inter. ALLOW is a **word**. |

**Killed on this path (do not revive):** seller reputation scores, live Marktplaats scrape, “AI SOC” purple, auto-ban, HireSignal-style compliance claims, two skins in one binary.

---

## 3. Sittings that already happened (do not re-litigate)

| Sitting | Outcome for ListGuard |
|---|---|
| Judging-panel teardown | Harness is not the company. Policy in code. Hostile in-scope. |
| Security/UX | S-01…S-06 blockers written into harness + constitution. |
| Sitting 6 (Exhibit) | Exhibit is a **pack layer** on this harness, not a rival skin in this session. `GET /exhibit/{id}` still works. |
| Sitting 7 | Live harness: Accept/Override, hostile button, honest unconfigured judge, gold ids. |
| Sitting 8 | Persist actor in sqlite; Override → queue; DEMO_TOKEN on kill/accept/override; `/eval` offline gold; observe≠judge defaults. |
| Sitting 9 | This spec: seed `lg-inject-01` etc. in `app/evals/listguard/gold.jsonl`; Phase 0 **done**; Tuesday starts T12. |

---

## 4. Monday 18:00 rule (already resolved for *this* session)

This session **is** ListGuard. Do not build ClauseWindow, MenuMind, or an Exhibit *skin*. The evidence pack stays a harness export.

Named human: fill `NAMED_HUMAN` / `NAMED_ROLE` / `NAMED_ORG` from consent. If unset, chrome must show `for named human unset` — do not fake a customer.

---

## 5. Risk-tier sentence (footer, unchanged)

> Limited-risk decision support for listing *content*. We queue or block listings; we do not ban people; a human accepts every recommendation in the demo.
