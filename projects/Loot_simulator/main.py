import random

items = [
    {"name": "Common Sword",    "rarity": "Common",    "prob": 0.50},
    {"name": "Rare Shield",     "rarity": "Rare",      "prob": 0.30},
    {"name": "Epic Armor",      "rarity": "Epic",      "prob": 0.15},
    {"name": "Legendary Blade", "rarity": "Legendary", "prob": 0.05},
]

def open_loot_box():
    roll = random.random()  # 0.0 to 1.0
    cumulative = 0
    for item in items:
        cumulative += item["prob"]
        if roll < cumulative:
            return item


drop = open_loot_box()
print(f"You got: {drop['name']} ({drop['rarity']})")


# Simulate 1000 loot boxes
results = {}
simulations = 1000

for _ in range(simulations):
    drop = open_loot_box()
    rarity = drop["rarity"]
    results[rarity] = results.get(rarity, 0) + 1

print(f"\n=== LOOT BOX SIMULATION ({simulations} opens) ===")
for item in items:
    actual = results.get(item["rarity"], 0)
    actual_pct = actual / simulations * 100
    expected_pct = item["prob"] * 100
    print(f"{item['rarity']:10} | Expected: {expected_pct:.0f}% | Actual: {actual_pct:.1f}% | Drops: {actual}")


def simulate_until_legendary():
    attempts = 0
    while True:
        attempts += 1
        drop = open_loot_box()
        if drop["rarity"] == "Legendary":
            return attempts

# How many boxes on average to get a legendary?
trials = 1000
total_attempts = sum(simulate_until_legendary() for _ in range(trials))
avg = total_attempts / trials
print(f"\nAvg boxes to get Legendary: {avg:.1f}")
print(f"Expected (1/0.05): {1/0.05}")