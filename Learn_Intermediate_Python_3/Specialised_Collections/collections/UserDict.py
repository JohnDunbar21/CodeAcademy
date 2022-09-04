"""
The 'UserDict' container wrapper lets us create our own version of a dictionary. 
This class contains all of the functionality of a normal 'dict', except that we 
can access the dictionary data through the 'data' property.
"""


from collections import UserDict
data = {'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99, 'order_status': 'processing'},
        'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99, 'order_status': 'complete'},
        'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50, 'order_status': 'complete'},
        'order_7378': {'type': 'jacket', 'size': 'large', 'price': 24.99, 'order_status': 'processing'}}

class OrderProcessingDict(UserDict):

    def clean_orders(self):
        to_delete = []
        for key, value in self.data.items():
            if value['order_status'] == 'complete':
                to_delete.append(key)

        for item in to_delete:
            del self.data[item]

process_dict = OrderProcessingDict(data)
process_dict.clean_orders()
print(process_dict)

# Create a class which inherits from the UserDict class
class DisplayDict(UserDict):
    # A new method to increase the dictionary's functionality
    def display_info(self):
        print("Number of Keys: " + str(len(self.keys())))
        print("Keys: " + str(list(self.keys())))
        print("Number of Values: " + str(len(self.values())))
        print("Values: " + str(list(self.values())))
 
    # We can also overwrite a method from the dictionary class
    def clear(self):
        print("Deleting all items from the dictionary!")
        super().clear()
 
disp_dict = DisplayDict({'user': 'Mark', 'device': 'desktop', 'num_visits': 37})
 
disp_dict.display_info()
 
disp_dict.clear()