"""Counsel policy. Not legal advice. Playbook is JSON, not prompt poetry."""

from __future__ import annotations

import re

from harness.policy import choice, noul, score_label
from harness.types import Action, Answer, PolicyResult

_UNCAP = re.compile(r"\b(uncapped|unlimited)\b", re.I)
_LIAB = re.compile(r"\b(liability|schedule\s*4)\b", re.I)


def policy_clausewindow(answers: dict[str, Answer], state: dict) -> PolicyResult:
    quote = str(state.get("quote") or "")
    locator = str(state.get("locator") or "")
    inj = noul(answers, "injection")
    walk = noul(answers, "walkaway_hit")
    topic = choice(answers, "topic")
    deviation = score_label(answers, "deviation")

    if inj >= 0.5:
        return PolicyResult(
            action=Action.queue,
            reason_codes=["injection_or_jailbreak"],
            human_required=True,
            notes="Not legal advice.",
        )

    # Kenji stop-the-line: declare the heuristic. Do not pretend the model caught Schedule 4.
    if _UNCAP.search(quote) and (_LIAB.search(quote) or "schedule 4" in locator.lower()):
        return PolicyResult(
            action=Action.queue,
            reason_codes=["playbook_walkaway", "heuristic_cap"],
            human_required=True,
            notes="Heuristic: uncapped/unlimited + liability/Schedule 4. Not legal advice.",
        )

    if walk >= 0.5 or deviation == "walkaway":
        return PolicyResult(
            action=Action.queue,
            reason_codes=["playbook_walkaway"],
            human_required=True,
            notes="Not legal advice.",
        )
    if topic == "unknown":
        return PolicyResult(
            action=Action.queue,
            reason_codes=["unknown"],
            human_required=True,
            notes="Not legal advice.",
        )
    return PolicyResult(
        action=Action.allow,
        reason_codes=["aligned"],
        human_required=False,
        notes="No playbook issue flagged. Not a recommendation to sign.",
    )
