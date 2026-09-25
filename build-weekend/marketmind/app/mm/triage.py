"""TRIAGE — visual card grid for escalated and reviewed listings (Darko improvement #2).
Generates app/out/triage.html for glanceable human-in-the-loop review.
Not an automated decider — presents receipts and facts cleanly for operator verification."""
from __future__ import annotations
import html
from pathlib import Path

CARD_CSS = """
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  background: #0f1117;
  color: #e6edf3;
  margin: 0;
  padding: 24px;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #30363d;
  padding-bottom: 16px;
  margin-bottom: 24px;
}
h1 {
  font-size: 1.4rem;
  margin: 0;
  font-weight: 600;
  color: #58a6ff;
  display: flex;
  align-items: center;
  gap: 8px;
}
.stats {
  font-size: 0.9rem;
  color: #8b949e;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}
.card {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.15s ease, border-color 0.15s ease;
}
.card:hover {
  transform: translateY(-2px);
  border-color: #58a6ff;
}
.card img {
  width: 100%;
  height: 190px;
  object-fit: cover;
  background: #21262d;
}
.no-photo {
  height: 190px;
  background: #21262d;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #8b949e;
  font-size: 0.9rem;
}
.card .body {
  padding: 14px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.card .title {
  font-weight: 600;
  font-size: 0.95rem;
  color: #f0f6fc;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.price-row {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
.price {
  font-size: 1.3rem;
  font-weight: 700;
  color: #3fb950;
}
.health-badge {
  font-size: 0.75rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 12px;
  background: #1f6feb26;
  color: #58a6ff;
  border: 1px solid #1f6feb;
}
.meta {
  font-size: 0.8rem;
  color: #8b949e;
  line-height: 1.4;
}
.badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 500;
  padding: 2px 6px;
  border-radius: 4px;
  margin-right: 4px;
  margin-top: 4px;
}
.badge-esc {
  background: #d2992226;
  color: #f2cc60;
  border: 1px solid #bb8009;
}
.badge-skip {
  background: #f8514926;
  color: #ff7b72;
  border: 1px solid #da3633;
}
.badge-drafted {
  background: #23863626;
  color: #3fb950;
  border: 1px solid #238636;
}
.bar-bg {
  height: 6px;
  background: #21262d;
  border-radius: 3px;
  overflow: hidden;
  margin-top: 4px;
}
.bar-fill {
  height: 100%;
  border-radius: 3px;
}
.bar-green { background: #3fb950; }
.bar-yellow { background: #d29922; }
.bar-red { background: #f85149; }
.actions {
  display: flex;
  border-top: 1px solid #30363d;
}
.actions button {
  flex: 1;
  padding: 10px;
  border: none;
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
  transition: background 0.15s ease;
}
.btn-pursue {
  background: #238636;
  color: #ffffff;
}
.btn-pursue:hover {
  background: #2ea043;
}
.btn-dismiss {
  background: #21262d;
  color: #ff7b72;
}
.btn-dismiss:hover {
  background: #b62324;
  color: #ffffff;
}
.toast {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #238636;
  color: white;
  padding: 10px 16px;
  border-radius: 6px;
  font-size: 0.85rem;
  display: none;
}
"""


def _bar_class(margin_z: float | None) -> str:
    if margin_z is None:
        return "bar-yellow"
    if margin_z > 2.5:
        return "bar-red"
    if margin_z > 0.5:
        return "bar-green"
    return "bar-yellow"


def _bar_width(margin_z: float | None) -> int:
    if margin_z is None:
        return 10
    return min(100, max(8, int(margin_z * 30)))


def render(run_id: str, receipts: list[dict], items_by_id: dict[str, dict]) -> str:
    """Returns responsive HTML string for visual escalation and review triage."""
    escalated = [r for r in receipts if r.get("action_state") == "escalated"]
    drafted = [r for r in receipts if r.get("action_state") in ("drafted", "pursued_assisted")]
    skipped = [r for r in receipts if r.get("action_state") == "skipped"]

    cards_html = []
    # Display escalated first, then drafted for review
    display_rows = escalated + drafted

    for r in display_rows:
        item = items_by_id.get(r.get("listing_id"), {})
        imgs = item.get("images") or []
        img_url = imgs[0] if imgs else ""
        mz = r.get("scores", {}).get("margin_z")
        h_score = r.get("scores", {}).get("health", item.get("health", "—"))
        reasons = r.get("reason_codes", [])
        state = r.get("action_state", "escalated")

        badge_cls = "badge-drafted" if state in ("drafted", "pursued_assisted") else "badge-esc"
        badges = "".join(f'<span class="badge {badge_cls}">{html.escape(rc)}</span>' for rc in reasons)

        mz_display = f"{mz:.1f}σ margin" if mz is not None else "no comps"
        bar_cls = _bar_class(mz)
        bar_w = _bar_width(mz)

        seller = item.get("seller") or {}
        seller_name = seller.get("name", "private")
        ratings = seller.get("rating_count", 0)

        photo_markup = (f'<img src="{html.escape(img_url)}" alt="item photo" loading="lazy" '
                        f'onerror="this.onerror=null;this.parentElement.innerHTML=\'<div class=\\\'no-photo\\\'>Photo Unavailable</div>\';">'
                        if img_url else '<div class="no-photo">No Photo Available</div>')

        card = f"""
        <div class="card" data-listing-id="{html.escape(str(r.get('listing_id')))}">
          {photo_markup}
          <div class="body">
            <div class="price-row">
              <div class="price">€{item.get('price_eur', '?')}</div>
              <span class="health-badge">Health {h_score}/100</span>
            </div>
            <div class="title">{html.escape(str(item.get('title', r.get('listing_id'))))}</div>
            <div class="meta">
              Comps: {mz_display} · State: <strong>{state}</strong><br>
              Seller: {html.escape(str(seller_name))} ({ratings} reviews)
            </div>
            <div class="bar-bg"><div class="bar-fill {bar_cls}" style="width: {bar_w}%"></div></div>
            <div>{badges}</div>
          </div>
          <div class="actions">
            <button class="btn-pursue" onclick="handleAction('{html.escape(str(r.get('listing_id')))}', 'pursue')">✅ Pursue / Approve</button>
            <button class="btn-dismiss" onclick="handleAction('{html.escape(str(r.get('listing_id')))}', 'dismiss')">❌ Dismiss</button>
          </div>
        </div>"""
        cards_html.append(card)

    cards_joined = "\n".join(cards_html) if cards_html else '<p class="stats">No escalated listings this cycle — all items processed fail-closed or auto-drafted.</p>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MarketMind Triage — {html.escape(run_id)}</title>
  <style>{CARD_CSS}</style>
</head>
<body>
  <header>
    <h1>🏪 MarketMind Triage <span style="font-size:0.9rem;color:#8b949e;font-weight:400">[{html.escape(run_id)}]</span></h1>
    <div class="stats">
      <strong>{len(escalated)}</strong> escalated · <strong>{len(drafted)}</strong> drafted · <strong>{len(skipped)}</strong> skipped
    </div>
  </header>
  <div class="grid">
    {cards_joined}
  </div>
  <div id="toast" class="toast">Action recorded</div>
  <script>
    function handleAction(id, action) {{
      const card = document.querySelector('[data-listing-id="' + id + '"]');
      if (card) {{
        card.style.opacity = '0.35';
        card.style.filter = 'grayscale(80%)';
        card.style.pointerEvents = 'none';
      }}
      const toast = document.getElementById('toast');
      toast.textContent = (action === 'pursue' ? '✅ Pursue initiated for ' : '❌ Dismissed ') + id;
      toast.style.display = 'block';
      setTimeout(() => {{ toast.style.display = 'none'; }}, 2500);
      console.log('TRIAGE_ACTION:', id, action);
    }}
  </script>
</body>
</html>"""


def write(path: Path, run_id: str, receipts: list[dict],
          items_by_id: dict[str, dict]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(render(run_id, receipts, items_by_id), encoding="utf-8")
