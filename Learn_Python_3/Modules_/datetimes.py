from datetime import datetime

birthday = datetime(2000, 1, 31)
# datetime function has three compulsory arguments: year, month, and second.
# It also has optional arguments: hour, minutes, seconds...

birthday.year
birthday.day
birthday.month
birthday.weekday() # returns the day of the week inside the birthday object. runs from 0 to 6.

datetime.now() # returns the current time.
