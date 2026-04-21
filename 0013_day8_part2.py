# Nesting
players = {
    "player1": {
        "name": "Alice",
        "score": 1500,
        "inventory": ["sword", "shield"]
    },
    "player2": {
        "name": "Bob",
        "score": 1200,
        "inventory": ["bow", "health potion"]
    }
}

print(players)

# Access nested data
print(players["player1"]["name"])
print(players["player2"]["inventory"][0])

# Modification
# Level up Alice
players["player1"]["score"] += 100
print(players)

# Add an item to Bob's inventory
players["player2"]["inventory"].append("magic ring")
print(players)