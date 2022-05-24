# We need to import the CSV library that offers methods to parse and modify the csv files.

import csv

with open('cool_csv.csv') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        print(row)

# import csv
 
# list_of_email_addresses = []
# with open('users.csv', newline='') as users_csv:
  # user_reader = csv.DictReader(users_csv)
  # for row in user_reader:
    # list_of_email_addresses.append(row['Email'])