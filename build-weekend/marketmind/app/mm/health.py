"""HEALTH — deterministic pre-filter from Apify metadata (no LLM).
Listings below HEALTH_FLOOR are auto-skipped before expensive vision/judge calls.
Art V.2: pure deterministic code, not a model question. Fail-closed: missing data = 0 points."""
from __future__ import annotations
import datetime

HEALTH_FLOOR = 25  # below this -> auto-skip (reason: low_health)

# Weights (total possible = 100)
W_SELLER_AGE = 20    # account age in years (capped at 5y = full points)
W_RATINGS = 20       # seller rating count (capped at 30 = full points)
W_PHOTOS = 15        # number of photos (capped at 4 = full points)
W_DESC_LEN = 15      # description length in chars (capped at 100 = full points)
W_PRICE_RATIO = 20   # price / category_median (0.3–0.9 = full; 0.2-0.3 or 0.9-1.5 = 10pts; else 0)
W_POSTING_AGE = 10   # freshness in hours (0–48h = full; >168h = 0)


def _clamp(val: float, lo: float, hi: float) -> float:
    return max(0.0, min(1.0, (val - lo) / (hi - lo))) if hi > lo else 0.0


def score(item: dict, category_median: float | None = None) -> int:
    """Returns 0–100 health score. Missing fields score 0 (fail-closed)."""
    s = 0.0

    # Seller age (years since registration)
    seller = item.get("seller") or {}
    try:
        since = int(str(seller.get("since", "2026"))[:4])
        age_years = 2026 - since
        s += W_SELLER_AGE * _clamp(age_years, 0, 5)
    except (ValueError, TypeError):
        pass  # missing = 0

    # Seller ratings
    try:
        ratings = int(seller.get("rating_count", 0))
        s += W_RATINGS * _clamp(ratings, 0, 30)
    except (ValueError, TypeError):
        pass

    # Photo count
    photos = len(item.get("images") or [])
    s += W_PHOTOS * _clamp(photos, 0, 4)

    # Description length
    desc_len = len(item.get("description") or "")
    s += W_DESC_LEN * _clamp(desc_len, 0, 100)

    # Price ratio vs category median (if comps available)
    if category_median and category_median > 0:
        price = float(item.get("price_eur") or 0)
        ratio = price / category_median
        if 0.3 <= ratio <= 0.9:
            s += W_PRICE_RATIO  # sweet spot: underpriced but not suspiciously cheap
        elif 0.2 <= ratio < 0.3 or 0.9 < ratio <= 1.5:
            s += W_PRICE_RATIO * 0.5  # partial credit
    elif len(item.get("description") or "") > 20 and len(item.get("images") or []) >= 1:
        # If no comps median given but listing has decent desc and photo, assign modest baseline
        s += 5.0

    # Posting age (prefer fresh listings)
    posted = item.get("posted_at")
    if posted:
        try:
            dt = datetime.datetime.fromisoformat(posted.replace("Z", "+00:00"))
            hours = (datetime.datetime.now(datetime.timezone.utc) - dt).total_seconds() / 3600
            if hours < 48:
                s += W_POSTING_AGE
            else:
                s += W_POSTING_AGE * _clamp(168 - hours, 0, 120)  # decays until 7 days
        except Exception:
            pass

    return int(round(s))
