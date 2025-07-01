import pandas as pd
from io import StringIO

# Sample CSV data as a string
data = """
player_name,team,goals,assists,matches,minutes
Messi,PSG,20,15,30,2700
Haaland,MCI,28,5,29,2600
Saka,ARS,14,11,30,2550
Mbappe,PSG,25,7,30,2700
De Bruyne,MCI,8,18,28,2500
Vinicius,RMA,17,9,29,2600
Salah,LIV,19,12,31,2800
Martinelli,ARS,13,6,29,2500
Osimhen,NAP,21,4,26,2300
Rashford,MUN,17,5,30,2600
"""

# Load the CSV string into a DataFrame
df = pd.read_csv(StringIO(data))

# View the data
print(df.head())

# Add total goal contributions
df['goal_contributions'] = df['goals'] + df['assists']

# Goals per match
df['goals_per_match'] = df['goals'] / df['matches']

# Show top 5 contributors
top_contributors = df[['player_name', 'team', 'goals', 'assists', 'goal_contributions']].sort_values(by='goal_contributions', ascending=False)
print(top_contributors.head())