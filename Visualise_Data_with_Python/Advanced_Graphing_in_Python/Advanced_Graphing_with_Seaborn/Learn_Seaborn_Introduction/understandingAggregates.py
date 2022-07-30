import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


gradebook = pd.read_csv("Visualise_Data_with_Python\Advanced_Graphing_in_Python\Advanced_Graphing_with_Seaborn\Learn_Seaborn_Introduction\gradebook.csv")
print(gradebook)

# An aggregate is a number used to describe a set of data, such as mean, median, and mode. 

assignment1 = gradebook[gradebook.assignment_name == "Assignment 1"]
#print(assignment1)
asn1_median = np.median(assignment1.grade)
print(asn1_median)