import pandas as pd

# When selecting a subset of data from a dataframe using logic, the indices tend to be non-consecutive, making it hard to use .iloc(). 
# We can use reset_index() on the dataframe and specify drop=True so you don't end up with an extra column, and inplace=True to modify our existing dataframe. 

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

df2 = df.loc[[1, 3, 5]]
#print(df2)
df2.reset_index(inplace=True, drop=True)
print(df2)