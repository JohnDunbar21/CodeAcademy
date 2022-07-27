import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Learn_Seaborn_Introduction\survey.csv")
print(df)
sns.barplot(data=df,x="Gender",y="Response",estimator=np.median) # estimator can also be len. 
plt.show()