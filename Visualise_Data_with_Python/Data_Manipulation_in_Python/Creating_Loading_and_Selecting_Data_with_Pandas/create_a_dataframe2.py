import pandas as pd

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115],
],
  columns=[
    'Store ID',
    'Location',
    'Number of Employees'
  ])

print(df2)