import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Load results.csv here:
df = pd.read_csv('Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Learn_Seaborn_Introduction\surveyResults.csv')
print(df)

sns.barplot(data=df ,x='Gender' ,y='Mean Satisfaction')
plt.show()