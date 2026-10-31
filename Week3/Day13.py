import pandas as pd
df=pd.read_csv("matches.csv")
# print(df.head(3))
# print(df.shape)
# result=df.loc[df["goals"]>10].sort_values("goals",ascending=False)[["player","goals"]]
# print(result)
# df["goals_per_match"]=(df["goals"]/df["matches"]).round(2)
# sorted_df=df.sort_values("goals_per_match",ascending=False)
# result=sorted_df.loc[:,["player","goals_per_match"]]
# print(result)
print(df["player"].value_counts())
print(df["goals"].mean().round(2))