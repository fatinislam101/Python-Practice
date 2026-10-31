import pandas as pd
data = {
    "player": ["Messi", "Haaland", "Salah", "Saka"],
    "team": ["Inter Miami", "Man City", "Liverpool", "Arsenal"],
    "goals": [12, 15, 10, 8],
    "matches": [14, 16, 15, 17],
}
df=pd.DataFrame(data)

print(df[["player","goals"]])
print(df[df["goals"]>=10])
print(df.sort_values("goals", ascending=False)[["player", "goals"]])

games = {
    "team": ["Arsenal", "Man City", "Arsenal", "Man City", "Arsenal"],
    "goals": [2, 3, 1, 4, 0],
}
df=pd.DataFrame(games)
print(df.groupby("team")["goals"].sum())