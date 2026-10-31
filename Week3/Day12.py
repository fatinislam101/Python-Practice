import pandas as pd
players = {
    "player": ["Messi", "Haaland", "Salah"],
    "team_id": [1, 2, 3],
}
teams = {
    "team_id": [1, 2, 3],
    "team": ["Inter Miami", "Man City", "Liverpool"],
}
df = pd.DataFrame(players).merge(pd.DataFrame(teams), on="team_id")
print(df[["player", "team"]])

players = {
    "player": ["Messi", "Haaland", "Salah", "Saka"],
    "team_id": [1, 2, 3, 4],
}
teams = {
    "team_id": [1, 2, 3],
    "team": ["Inter Miami", "Man City", "Liverpool"],
}
df=pd.DataFrame(players).merge(pd.DataFrame(teams),on="team_id")
print(df[["player","team"]])

players = {
    "player": ["Messi", "Haaland", "Salah", "Saka"],
    "team_id": [1, 2, 3, 4],
}
teams = {
    "team_id": [1, 2, 3],
    "team": ["Inter Miami", "Man City", "Liverpool"],
}
df=pd.DataFrame(players).merge(pd.DataFrame(teams),on="team_id",how="left")
print(df[["player","team"]])