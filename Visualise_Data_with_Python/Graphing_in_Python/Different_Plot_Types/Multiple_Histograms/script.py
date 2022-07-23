from matplotlib import pyplot as plt
import csv

def convert_time_to_num(time):
  mins = int(time[-2:])
  frac_of_hour = mins/60.0
  hour = int(time[:-3])
  time = hour + frac_of_hour
  return time

sales_times_raw = []
with open('Visualise_Data_with_Python\Graphing_in_Python\Different_Plot_Types\Multiple_Histograms\sales_times.csv') as csvDataFile:
  csvReader = csv.reader(csvDataFile)
  for row in csvReader:
    sales_times_raw.append(row[2])
  sales_times_raw = sales_times_raw[1:]

sales_times1 = []
for time in sales_times_raw:
  sales_times1.append(convert_time_to_num(time))

sales_times2_raw = []
with open('Visualise_Data_with_Python\Graphing_in_Python\Different_Plot_Types\Multiple_Histograms\sales_times_s2.csv') as csvDataFile:
  csvReader = csv.reader(csvDataFile)
  for row in csvReader:
    sales_times2_raw.append(row[2])
  sales_times2_raw = sales_times2_raw[1:]

sales_times2 = []
for time in sales_times2_raw:
  sales_times2.append(convert_time_to_num(time))