import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Learn_Seaborn_Introduction\survey2.csv")
plt.figure(figsize=(10,8))
sns.barplot(data=df, x="Gender", y="Patient ID", hue="Age Range")

#sns.barplot(data=survey, x="Age Range", y="Patient ID", hue="Gender")

plt.show()