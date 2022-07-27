import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Learn_Seaborn_Introduction\gradebook.csv")

# sns.barplot() will plot the data in a given dataframe and automatically aggregate the data. 

sns.barplot(data=gradebook, x="assignment_name", y="grade")
plt.show()