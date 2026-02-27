import json
import pandas as pd
import seaborn
import matplotlib.pyplot as plt


with open('games.json', 'r') as f:
    data = json.load(f)

processed_games = []
for game in data:
    # skip games that havent been played yet
    if game['score'] == "-:-":
        continue
    
    score_only = game['score'].split(' ')[0]
    home_goals, away_goals = map(int, score_only.split(':'))
    
    processed_games.append({
        'Home': game['home'],
        'Away': game['away'],
        'Away_Goals': away_goals,
        'Goal_Difference': away_goals - home_goals,
    })

#remember, df is dataframe.
df = pd.DataFrame(processed_games)

# negative = away loss, + means away win
graph = df.pivot_table(index='Away', columns='Home', values='Goal_Difference', aggfunc='mean')
graph_labels = df.pivot_table(index='Away', columns='Home', values='Goal_Difference', aggfunc=lambda x: f"+{x.mean():.1f}" if x.mean() >= 0 else f"{x.mean():.1f}")
# print(processed_games)

#heatmap
plt.figure(figsize=(12, 10))
seaborn.heatmap(graph, annot=graph_labels, fmt="", cmap='RdYlGn', center=0, cbar_kws={'label': 'Average Goal Differential (Away - Home)'})

plt.title('NIHL Away Team Goal Differential - If Away Team Wins, Positive; If Away Team Loses, Negative')
plt.xlabel('Destination (Home Rink)')
plt.ylabel('Traveling Team (Away)')
plt.show()