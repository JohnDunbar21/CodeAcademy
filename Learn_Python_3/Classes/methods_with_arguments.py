class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi * radius ** 2

circle = Circle()
pizza_area = circle.area(6) # Diameter 12 inches
teaching_table_area = circle.area(18) # Diameter 36 inches
round_room_area = circle.area(5730) # Diameter 11460 inches