import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Visualising_World_Cup_Data_with_Seaborn\worldCupMatches.csv')

#print(df.head())
df['Total Goals']= df['Home Team Goals'] + df['Away Team Goals']
#print(df.head())
sns.set_style('whitegrid')
sns.set_context('poster', font_scale = 0.6)
f, ax = plt.subplots(figsize=(12,7)) # apparently the figsize parameter can also be passed in the subplots() method. 
ax = sns.barplot(data=df,x='Year',y='Total Goals')
ax.set_title('Number of Goals Scored in Each World Cup Season')

df_goals = pd.read_csv('Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Visualising_World_Cup_Data_with_Seaborn\goals.csv')

sns.set_style('dark')
sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(data=df_goals,x='year',y='goals',palette='Spectral')
ax2.set_title('Number of Goals Scored by Home Teams in Each World Cup Season')

plt.show()