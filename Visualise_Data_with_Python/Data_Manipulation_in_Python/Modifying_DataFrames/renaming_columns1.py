import pandas as pd

df = pd.read_csv('Visualise_Data_with_Python\Data_Manipulation_in_Python\Modifying_DataFrames\imdb.csv')

df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']

print(df)