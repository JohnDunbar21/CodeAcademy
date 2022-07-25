import pandas as pd

df = pd.read_csv('Visualise_Data_with_Python\Data_Manipulation_in_Python\Creating_Loading_and_Selecting_Data_with_Pandas\imdb.csv')
# df.head() gives the first 5 rows and their headers.
print(df.head())
# df.info() gives information on the file. Gives RangeIndex, Data Columns and their headers, no. of entries, and data type, memory usage.
print(df.info())