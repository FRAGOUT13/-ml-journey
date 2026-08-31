players = [
    {"name": "FragKing", "level": 15, "kills": 342, "deaths": 120, "score": 8900},
    {"name": "ShadowX", "level": 8, "kills": 210, "deaths": 95, "score": 5400},
    {"name": "NullPtr", "level": 22, "kills": 580, "deaths": 200, "score": 14200},
    {"name": "ByteSlayer", "level": 5, "kills": 89, "deaths": 67, "score": 2100},
    {"name": "VoidRunner", "level": 12, "kills": 290, "deaths": 140, "score": 7300},
    {"name": "GlitchHunter", "level": 19, "kills": 430, "deaths": 160, "score": 11000},
    {"name": "PixelGhost", "level": 3, "kills": 45, "deaths": 80, "score": 900},
    {"name": "CoreDump", "level": 9, "kills": 175, "deaths": 88, "score": 4600},
    {"name": "StackOverflow", "level": 14, "kills": 320, "deaths": 130, "score": 8500},
    {"name": "SegFault", "level": 7, "kills": 150, "deaths": 70, "score": 4000},
    {"name": "NullByte", "level": 11, "kills": 260, "deaths": 110, "score": 6800},
    {"name": "BinaryBandit", "level": 16, "kills": 380, "deaths": 150, "score": 9500},
]

# WHERE — filter rows
def where(data, condition):
    return [row for row in data if condition(row)]

# SELECT — pick specific fields
def select(data, fields):
    return [{f: row[f] for f in fields} for row in data]

# ORDER BY — sort
def order_by(data, field, reverse=False):
    return sorted(data, key=lambda row: row[field], reverse=reverse)

# GROUP BY — group and count
def group_by(data, field):
    groups = {}
    for row in data:
        key = row[field]
        if key not in groups:
            groups[key] = []
        groups[key].append(row)
    return groups


# Players with level > 10
high = where(players, lambda p: p["level"] > 10)
print("High level players:")
for p in select(high, ["name", "level"]):
    print(p)

# Top 3 by score
print("\nTop 3 scores:")
for p in order_by(players, "score", reverse=True)[:3]:
    print(p["name"], p["score"])


# Group players by level tier
def level_tier(p):
    if p["level"] <= 5:
        return "Rookie"
    elif p["level"] <= 10:
        return "Veteran"
    else:
        return "Elite"

for p in players:
    p["tier"] = level_tier(p)

groups = group_by(players, "tier")
print("\nPlayers by tier:")
for tier, members in groups.items():
    print(f"  {tier}: {len(members)} players — {[p['name'] for p in members]}")