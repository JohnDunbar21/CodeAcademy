import pandas as pd

orders = pd.read_csv('Visualise_Data_with_Python\Data_Manipulation_in_Python\Creating_Loading_and_Selecting_Data_with_Pandas\shoefly.csv')
print(orders.head())
emails = orders.email
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]
print(frances_palmer)
comfy_shoes = orders[(orders.shoe_type == 'clogs') | (orders.shoe_type == 'boots') | (orders.shoe_type == 'ballet flats')]
print(comfy_shoes)