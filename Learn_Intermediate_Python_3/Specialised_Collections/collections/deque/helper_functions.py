import csv

def process_csv_supplies():
    data = []
    with open('Learn_Intermediate_Python_3\Specialised_Collections\collections\deque\supplies_data.csv', 'r') as csvfile:
        r = csv.reader(csvfile)
        for row in r:
            data.append(row)
    return data