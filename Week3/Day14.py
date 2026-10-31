import pandas as pd
teams = {
    "team": ["Inter Miami", "Man City", "Liverpool", "Arsenal", "Bayern"],
    "league": ["MLS", "EPL", "EPL", "EPL", "Bundesliga"],
}
df=pd.read_csv("matches.csv")
print(df.shape)
lowest_goals=df.loc[df["goals"]>=12].sort_values("goals",ascending=True)[["player","goals"]]
print(lowest_goals)
teams_df = pd.DataFrame(teams)

merged_df = df.merge(teams_df, on="team", how="left")

print(merged_df.loc[:, ["player", "team", "league"]])
df["goals_per_match"]=(df["goals"]/df["matches"]).round(2)
sorted_df=df.sort_values("goals_per_match",ascending=False)
print(sorted_df)
print(df.loc[df["goals_per_match"].idxmax(), "player"])

league_goals = merged_df.groupby("league", dropna=False)["goals"].sum()

print(league_goals)
