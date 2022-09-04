"""
The 'ChainMap' container allows us to store many mappings in an ordered group, but lookups 
(accessing the value using a key) are repeated for every mapping inside of the 'ChainMap' 
until something is found or the end is reached. If we try to modify the data in any way, 
then only the first mapping in the 'ChainMap' will receive the changes. When accessing data, 
one way to think of the 'ChainMap' is that it treats all of the stored dictionaries as one 
large dictionary, where if there are repeated keys, then the first found result is returned.

Note: In order to modify data from dictionaries which are deeper in the ChainMap, we will 
need to iterate through the dictionaries which are stored inside of it.

Another interesting concept that the 'ChainMap' uses is the concept of a parent mappings. 
If we use the 'parents' property, all mappings except the first one will be returned. 
This is because those mappings are considered to be the parent mappings to the first one. 
You can add a new 'child' mapping to the front of the list of mappings using the 'new_child()' method.
"""


year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

from collections import ChainMap

profit_map = ChainMap(*year_profit_data) # '*' required so constructor reads each dictionary as an individual argument.

def get_profits(data):
  total_holiday_profit = 0.0
  total_standard_profit = 0.0
  for month in data.keys():
    if 'holiday' in month:
      total_holiday_profit += data[month]
    else:
      total_standard_profit += data[month]
  return total_standard_profit, total_holiday_profit

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

for month in new_months_data:
  profit_map = profit_map.new_child(month)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)

year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit

print(year_diff_standard_profit)
print(year_diff_holiday_profit)