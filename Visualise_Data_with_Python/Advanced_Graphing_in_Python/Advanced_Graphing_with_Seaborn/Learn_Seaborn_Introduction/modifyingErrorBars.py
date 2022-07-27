import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Learn_Seaborn_Introduction\gradebook.csv")

# By default, Seaborn uses 'bootstrapped confidence interval' which has a 95% confidence interval. 
# you can pass ci="sd" in the barplot() function to get the error bars to represent one standard deviation, rather than 95% confidence intervals.  

sns.barplot(data=gradebook, x="student", y="grade", ci="sd")
plt.show()