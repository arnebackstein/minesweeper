import os

LEADERBOARD_FILE = "leaderboard.txt"

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        lines = f.readlines()
    entries = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 2:
            entries.append((parts[0], float(parts[1])))
    return sorted(entries, key=lambda x: x[1])

def save_leaderboard(name, seconds):
    entries = load_leaderboard()
    entries.append((name, seconds))
    entries = sorted(entries, key=lambda x: x[1])[:10]
    with open(LEADERBOARD_FILE, "w") as f:
        for n, s in entries:
            f.write(f"{n},{s:.2f}\n")