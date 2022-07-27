from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns

df = pd.read_csv('Visualise_Data_with_Python\Advanced_Graphing_in_Python\Seaborn_Cumilative_Project\kiva_data.csv')
#print(df.head())
f, ax = plt.subplots(figsize=(10,8))
sns.barplot(data=df,x='country',y='loan_amount',hue='gender')
fmt = "${x:,.0f}"
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

# Reflection:
# 1. Based on this data, Males are more likely to receive larger loans from Kiva. 
# 2. El Salvador has the least disparity in loan amounts awarded by gender. 
# 3. Recommendation-wise, Kiva could decrease the loan amounts awarded to male borrowers
# and increase the loan amounts awarded to female borrowers: this would lessen disparity. 
# 4. See above for implementations. 

sns.despine(left=True,bottom=True)
sns.set_palette("Pastel2")
sns.set_style("white")
ax.set_title("Loan Amounts Awarded to Male and Female Borrowers From Kiva")

f, ax2 = plt.subplots(figsize=(10,8))
sns.boxplot(data=df,x='country',y='loan_amount',hue='gender')
ax2.yaxis.set_major_formatter(tick)
ax2.set_title("Distribution of Loan Amounts Between Male and Female Borrowers From Kiva")

# Reflection 2:
# 1. Kenya has the widest distribution, this is in the Male category. 
# 2. You are more likely to receive a larger loan amount in Cambodia. 

sns.set_palette("Set3")
sns.set_style("dark")

f, ax3 = plt.subplots(figsize=(10,8))
sns.boxplot(data=df,x='activity',y='loan_amount',hue='gender')
ax3.yaxis.set_major_formatter(tick)
ax3.set_title("Loan Amounts Awarded vs. Loan Activity")

# Reflection 3:
# 1. This visualisation shows that most of the loans being taken out are mainly used for farming purposes. 

f, ax4 = plt.subplots(figsize=(10,8))
sns.violinplot(data=df,x='activity',y='loan_amount')
ax4.yaxis.set_major_formatter(tick)
ax4.set_title("Distribution of Loan Amount vs. Loan Activity")

sns.set_palette("Spectral")
f, ax5 = plt.subplots(figsize=(10,8))
sns.violinplot(data=df,x='country',y='loan_amount',hue='gender',split='gender')
ax5.yaxis.set_major_formatter(tick)
ax5.set_title("Gender Disparity of Loan Distribution Based on Country and Loan Amount")

# Reflection 4:
# 1. This data representation shows that females tend to receive the lower end of the loan distribution. 


plt.show()