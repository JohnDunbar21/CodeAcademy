import pandas as pd

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

# Examples:
# df.iloc[3:7] selects the 3rd row up to but not including the 7th row. Bear in mind that index 0 is the first row, so index 3 is actually the 4th row.
# df.iloc[:4] selects every row up to but not including row 4.
# df.iloc[-3] selects the rows starting at the 3rd last row and up to and including the final row.

april_may_june = df.iloc[3:7]
print(april_may_june)