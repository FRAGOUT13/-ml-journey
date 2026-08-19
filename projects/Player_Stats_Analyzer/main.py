# Entry point — loads player data, runs manual stats, and prints a report.
from stats import mean, median, std_dev

# Raw player data: dicts inside a list (no DB, no libraries).
players = [
    {"name": "FragKing", "level": 15, "kills": 342, "deaths": 120, "score": 8900},
    {"name": "ShadowX", "level": 8, "kills": 210, "deaths": 95, "score": 5400},
    {"name": "NullPtr", "level": 22, "kills": 580, "deaths": 200, "score": 14200},
    {"name": "ByteSlayer", "level": 5, "kills": 89, "deaths": 67, "score": 2100},
    {"name": "VoidRunner", "level": 12, "kills": 290, "deaths": 140, "score": 7300},
    {"name": "GlitchHunter", "level": 19, "kills": 430, "deaths": 160, "score": 11000},
    {"name": "PixelGhost", "level": 3, "kills": 45, "deaths": 80, "score": 900},
    {"name": "CoreDump", "level": 9, "kills": 175, "deaths": 88, "score": 4600},
]

# Basic stats on scores (mean, median, std dev) via stats.py
scores = [p["score"] for p in players]
print(f"Mean score:   {mean(scores):.2f}")
print(f"Median score: {median(scores):.2f}")
print(f"Std dev:      {std_dev(scores):.2f}")

# KD ratio per player, added as a new field on each dict
for p in players:
    p["kd"] = round(p["kills"] / p["deaths"], 2)

# SQL-style filter: players above level 10, and their share of the roster
high_level = [p for p in players if p["level"] > 10]
pct_high = len(high_level) / len(players) * 100

# SQL-style order by KD descending, limit 3
top_kd = sorted(players, key=lambda p: p["kd"], reverse=True)[:3]
print("\nTop 3 KD Ratios:")
for i, p in enumerate(top_kd, 1):
    print(f"  {i}. {p['name']} — {p['kd']}")

# Summary report pulling everything together
print("\n=== PLAYER STATS REPORT ===")
print(f"Total players : {len(players)}")
print(f"Avg score     : {mean(scores):,.0f}")
print(f"Top player    : {max(players, key=lambda p: p['score'])['name']} ({max(scores):,})")
print(f"Lowest        : {min(players, key=lambda p: p['score'])['name']} ({min(scores):,})")
print(f"High level    : {len(high_level)}/{len(players)} ({pct_high:.1f}%)")