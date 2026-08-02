import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------
# 1. Load the data
# ------------------------------------------------------
df = pd.read_csv("ipl_matches.csv")

print("Total rows and columns:", df.shape)
print(df.head())

# ------------------------------------------------------
# 2. Total wins per team
# ------------------------------------------------------
wins_per_team = df["winner"].value_counts()
print("\nWins per team:\n", wins_per_team)

plt.figure(figsize=(8, 5))
wins_per_team.plot(kind="bar", color="blue")
plt.title("Total Wins per Team")
plt.xlabel("Team")
plt.ylabel("Wins")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("01_wins_per_team.png", dpi=500)
plt.show()

# ------------------------------------------------------
# 3. Matches played per season
# ------------------------------------------------------
matches_per_season = df["season"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.plot(matches_per_season.index, matches_per_season.values, marker="o")
plt.title("Matches Played per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")
plt.tight_layout()
plt.savefig("02_matches_per_season.png", dpi=500)
plt.show()

# ------------------------------------------------------
# 4. Toss decision: bat vs field
# ------------------------------------------------------
toss_counts = df["toss_decision"].value_counts()

plt.figure(figsize=(5, 5))
plt.pie(toss_counts.values, labels=toss_counts.index, autopct="%1.1f%%")
plt.title("Toss Decision: Bat vs Field")
plt.savefig("03_toss_decision.png", dpi=500)
plt.show()

# ------------------------------------------------------
# 5. Did the toss winner also win the match?
# ------------------------------------------------------
df["toss_winner_won"] = df["toss_winner"] == df["winner"]
toss_win_count = df["toss_winner_won"].value_counts()
print("\nDid toss winner also win match?\n", toss_win_count)

plt.figure(figsize=(5, 5))
toss_win_count.plot(kind="bar", color=["green", "red"])
plt.title("Toss Winner Also Match Winner?")
plt.xticks([0, 1], ["Yes", "No"], rotation=0)
plt.tight_layout()
plt.savefig("04_toss_impact.png", dpi=500)
plt.show()

# ------------------------------------------------------
# 6. Win margins (runs and wickets) using NumPy
# ------------------------------------------------------
runs_wins = df[df["win_by_runs"] > 0]["win_by_runs"]
wicket_wins = df[df["win_by_wickets"] > 0]["win_by_wickets"]

avg_runs = np.mean(runs_wins)
avg_wickets = np.mean(wicket_wins)

print("\nAverage win margin by runs:", round(avg_runs, 2))
print("Average win margin by wickets:", round(avg_wickets, 2))

plt.figure(figsize=(8, 5))
plt.hist(runs_wins, bins=15, color="purple", edgecolor="black")
plt.title("Win Margin Distribution (by Runs)")
plt.xlabel("Runs")
plt.ylabel("Number of Matches")
plt.tight_layout()
plt.savefig("05_win_margin_runs.png", dpi=500)
plt.show()

# ------------------------------------------------------
# 7. Top 10 Player of the Match winners
# ------------------------------------------------------
top_players = df["player_of_match"].value_counts().head(10)
print("\nTop 10 Player of the Match award winners:\n", top_players)

plt.figure(figsize=(8, 5))
top_players.plot(kind="bar", color="orange")
plt.title("Top 10 Player of the Match Winners")
plt.xlabel("Player")
plt.ylabel("Awards")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("06_top_players.png", dpi=500)
plt.show()

# ------------------------------------------------------
# 8. Final summary
# ------------------------------------------------------
print("\n--- Summary ---")
print("Total matches:", len(df))
print("Most successful team:", wins_per_team.idxmax(), "with", wins_per_team.max(), "wins")