import pandas as pd
from matplotlib import pyplot as plt

import seaborn as sns


df = pd.read_csv('Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Learn_Seaborn_Introduction\survey.csv') # csv file not provided in example
sns.barplot(x='Age Range', y='Response', hue='Gender', data=df)
plt.show()