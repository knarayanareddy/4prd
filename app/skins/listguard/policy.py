"""T&S policy. Models propose. Code decides. Never ban a person."""

from __future__ import annotations

from harness.policy import choice, noul, score_label
from harness.types import Action, Answer, PolicyResult

BLOCK_BUCKETS = {"other_illegal", "weapon", "animal"}


def policy_listguard(answers: dict[str, Answer], state: dict) -> PolicyResult:
    bucket = choice(answers, "policy_bucket")
    inj = noul(answers, "injection_or_jailbreak")
    needs = noul(answers, "needs_human")
    fake = score_label(answers, "counterfeit_risk")

    if bucket in BLOCK_BUCKETS:
        return PolicyResult(
            action=Action.block,
            reason_codes=[bucket],
            human_required=True,
            notes="Listing content only. We do not ban sellers.",
        )
    if inj >= 0.5:
        return PolicyResult(
            action=Action.queue,
            reason_codes=["injection_or_jailbreak"],
            human_required=True,
        )
    if bucket == "unknown" or needs >= 0.6:
        return PolicyResult(action=Action.queue, reason_codes=["unknown"], human_required=True)
    if bucket == "ok" and fake == "obvious_fake":
        return PolicyResult(action=Action.queue, reason_codes=["counterfeit"], human_required=True)
    if bucket == "ok":
        return PolicyResult(action=Action.allow, reason_codes=["ok"], human_required=False)
    return PolicyResult(action=Action.queue, reason_codes=[bucket or "unknown"], human_required=True)
