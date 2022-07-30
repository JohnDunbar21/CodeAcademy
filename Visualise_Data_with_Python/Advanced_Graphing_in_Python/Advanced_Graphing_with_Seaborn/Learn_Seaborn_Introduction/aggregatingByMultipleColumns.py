import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,8))
plt.title("Gender Satisfaction Survey Results")
df = pd.read_csv("Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Learn_Seaborn_Introduction\survey.csv")

# the hue keyword allows us to compare two factors at once: in this example it is Gender and Age Range. 

sns.barplot(data=df,x="Gender",y="Response",hue="Age Range")
plt.show()