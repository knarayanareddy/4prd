"""ACT — draft-assist composer + allowlist + caps. `drafted` is not `sent` (Art VII.2). No money tools exist (Art V.3)."""
from __future__ import annotations
from . import config


def round5(x: float) -> int:
    return int(max(config.OFFER_ROUND_TO, round(x / config.OFFER_ROUND_TO) * config.OFFER_ROUND_TO))


def draft_offer(item: dict, facts: dict, used_tonight: int) -> dict | None:
    """Capped T2 offer (<=80% of ask, H1 band). None = over cap or floor breach -> caller escalates."""
    if used_tonight >= config.MAX_COLD_OUTREACH:
        return None
    ask = item["price_eur"]
    offer = round5(ask * config.OFFER_RATIO)
    if offer < ask * config.OFFER_FLOOR_RATIO:
        return None
    sig = f" — {config.RESELLER}" if config.RESELLER and config.RESELLER != "unset" else ""
    return {
        "offer_eur": offer,
        "offer_ratio": round(offer / ask, 2),
        "counter_round": 0,
        "max_counter_rounds": config.MAX_COUNTER_ROUNDS,
        "action": "send_message",              # allowlist (Art XII.1)
        "action_state": "drafted",             # human must press Send -> then `pursued_assisted`
        # no "— unset" ever reaches a seller (audit C7: signature omitted until NAMED_RESELLER is filled)
        "text_nl": (f"Hoi! Ik zag je {item['title']} te koop staan. "
                    f"Zou je €{offer} willen accepteren? Ik kan het ophalen wanneer het uitkomt.{sig}"),
        "text_en": (f"Hi! Would you accept €{offer} for the {item['title']}? "
                    f"Happy to pick up whenever suits you.{sig}"),
    }


def reprice_own(item: dict) -> dict | None:
    """T1 own-account action (auto within tier): stale listing -> modest reprice. Allowlist: edit_own_price."""
    if not item.get("is_mine") or not item.get("stale_days"):
        return None
    new_price = round5(item["price_eur"] * 0.90)
    return {"action": "edit_own_price", "old_eur": item["price_eur"], "new_eur": new_price,
            "action_state": "pursued_auto", "reason": f"stale {item['stale_days']}d"}
