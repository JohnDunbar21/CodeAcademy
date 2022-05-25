class Menu:

    def __init__ (self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "The {m} menu runs from {s}:00 until {e}:00.".format(m=self.name, s=self.start_time, e=self.end_time)

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            if item in self.items:
                total += self.items[item]
        return total

brunch = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)
early_bird = Menu("early bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)
dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)
kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

class Franchise:

    def __init__ (self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__ (self):
        return "The restaurant is located at {loc}.".format(loc=self.address)

    def available_menus(self, time):
        available_items = []
        for items in self.menus:
            if time >= items.start_time and time <= items.end_time:
                available_items.append(items)
        return available_items

menu = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menu)
new_installment = Franchise("12 East Mulberry Street", menu)

print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

class Business:

    def __init__ (self, name, franchises):
        self.name = name
        self.franchises = franchises

new_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = Menu("Take a Arepa", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, 10, 20)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

arepas_business = Business("Take a Arepa", arepas_place)