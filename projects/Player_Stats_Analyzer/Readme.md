# Player Stats Analyzer

A pure Python project to analyze game player statistics — no libraries, just code.

Built to practice: Python data structures, manual statistics, probability, and SQL-style querying.

---

## What it does

- Stores player data using dicts and lists
- Calculates stats manually — mean, median, standard deviation
- Runs probability queries (e.g. % of players above a threshold)
- Filters, sorts, and groups data like SQL — in pure Python
- Prints a clean summary report

---

## Concepts covered

- Python: dicts, lists, sets, tuples, loops, functions, list comprehensions
- Linear algebra: vector ops on stat arrays
- Statistics: mean, median, std dev, variance
- Probability: frequency distributions
- SQL thinking: filter, group by, order by — implemented manually

---

## Run it

```bash
python main.py
```

---

## Project structure

```
player_stats_analyzer/
├── main.py        # entry point
├── stats.py       # manual stats functions
├── queries.py     # SQL-style filter/sort/group functions
└── README.md
```

---

## Sample output

```
=== PLAYER STATS REPORT ===

Total players: 12
Avg score: 6,825
Top player: NullPtr (14,200)
Lowest: PixelGhost (900)

High performers (level > 10): 5 players (41.6%)
KD Ratio leaders:
  1. NullPtr     — 2.90
  2. FragKing    — 2.85
  3. GlitchHunter — 2.69
```

---

*Part of [ml-journey](https://github.com/fragout/ml-journey) — building in public.*