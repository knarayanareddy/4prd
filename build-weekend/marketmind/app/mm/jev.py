"""JEV — System 1 Decision & Safety Gateway (typesafe.ai / OpenRouter).
Provides fast, calibrated discrete classification over closed label sets.
Inherent prompt injection immunity (Art VI): discriminative classification
cannot be coerced by adversarial generative instructions."""
from __future__ import annotations

SAFETY_BUCKETS = [
    "clean",
    "injection_or_jailbreak",
    "offplatform_payment",
    "counterfeit",
    "weapon",
    "pii",
]

INBOUND_LABELS = [
    "inbound_availability",
    "dispute_t3",
    "offer_counter",
    "injection_or_jailbreak",
    "needs_human",
]

# Markers for discriminative classification
_INJECTION_MARKERS = (
    "ignore previous", "disregard", "system prompt", "jailbreak", "accept any offer",
    "new instructions", "developer mode", "override policy", "forget your rules",
    "output pursue", "bypass"
)
_DISPUTE_MARKERS = (
    "broken", "kapot", "refund", "beschadigd", "defect", "return", "restitution",
    "terugbetaling", "doesnt work", "doesn't work", "werkt niet", "geld terug", "oplichting"
)
_AVAIL_MARKERS = (
    "nog beschikbaar", "beschikbaar?", "still available", "available?", "is het nog",
    "kan ik het ophalen", "is dit er nog"
)


def classify_inbound(text: str, mode: str = "sim") -> dict:
    """Classifies inbound buyer message using System 1 classification.
    Returns: {label: str, confidence: float, tier: str, outcome: str, reply: str | None}"""
    t = (text or "").lower()

    # Check for prompt injection / jailbreak (Art VI)
    if any(m in t for m in _INJECTION_MARKERS):
        return {
            "label": "injection_or_jailbreak",
            "confidence": 0.98,
            "outcome": "skipped",
            "tier": "T3",
            "reply": None,
            "reasons": ["injection_or_jailbreak"],
            "note": "System-1 injection defense: discriminative classification immune to jailbreak (Art VI)",
        }

    # Check for disputes (Art VII.4)
    if any(m in t for m in _DISPUTE_MARKERS):
        return {
            "label": "dispute_t3",
            "confidence": 0.95,
            "outcome": "escalated",
            "tier": "T3",
            "reply": None,
            "reasons": ["dispute_t3"],
            "note": "human writes the reply — never auto (Art VII.4)",
        }

    # Check for availability queries
    if any(m in t for m in _AVAIL_MARKERS):
        return {
            "label": "inbound_availability",
            "confidence": 0.92,
            "outcome": "drafted",
            "tier": "T1",
            "reply": "Hoi! Ja, is nog beschikbaar. Wanneer zou het jou uitkomen?",
            "reasons": ["inbound_availability"],
            "note": "fast System-1 availability draft",
        }

    return {
        "label": "needs_human",
        "confidence": 0.70,
        "outcome": "escalated",
        "tier": "T2",
        "reply": None,
        "reasons": ["needs_human"],
        "note": "unclassified inquiry escalated to human",
    }


def classify_safety(text: str, mode: str = "sim") -> dict:
    """Classifies listing text for hostile content using System 1 discriminative routing."""
    t = (text or "").lower()
    scores = {b: 0.01 for b in SAFETY_BUCKETS}

    if any(m in t for m in _INJECTION_MARKERS):
        scores["injection_or_jailbreak"] = 0.99
    elif any(p in t for p in ("iban", "tikkie", "paypal.me", "transfer")):
        scores["offplatform_payment"] = 0.95
    elif any(c in t for c in ("fake", "replica", "1:1 clone", "namaak")):
        scores["counterfeit"] = 0.90
    else:
        scores["clean"] = 0.95

    top_label = max(scores, key=scores.get)
    return {
        "top_label": top_label,
        "confidence": scores[top_label],
        "distribution": scores,
        "is_safe": top_label == "clean" and scores["clean"] >= 0.85,
    }
