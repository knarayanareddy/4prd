from __future__ import annotations

from harness.decisions import queue_forcing_answers
from harness.types import Answer, Question


class JevBackend:
    """Optional. Default is TfJsonBackend. Flag only — product must run without this."""

    name = "jev"

    def decide(self, state: dict, questions: dict[str, Question]) -> dict[str, Answer]:
        raise RuntimeError("jev backend is not wired; use DECISION_BACKEND=tf_json")
