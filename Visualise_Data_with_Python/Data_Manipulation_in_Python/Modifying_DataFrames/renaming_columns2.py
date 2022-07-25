import pandas as pd

df = pd.read_csv('Visualise_Data_with_Python\Data_Manipulation_in_Python\Modifying_DataFrames\imdb.csv')
# you can rename a column by using the rename() method and selecting columns as a parameter, ensuring to set inplace=True so it does not create another dataset.
df.rename(columns={
  'name': 'movie_title'},
  inplace=True,
)

print(df)