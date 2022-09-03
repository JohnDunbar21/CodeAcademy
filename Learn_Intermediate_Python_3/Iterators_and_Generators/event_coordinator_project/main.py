guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  val = None
  while True:
    if val is not None:
      line_data = val.strip().split(",")
    else:
      line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    val = yield name

guestlist = read_guestlist("Learn_Intermediate_Python_3\Iterators_and_Generators\event_coordinator_project\guest_list.txt")

for i in range(1,11):
  print(next(guestlist))

print(guestlist.send("Jane,35"))

for g in guestlist:
  print(g)

print("\n")

whoIsOver21 = (guest for guest in guests if guests[guest] >= 21)

for g in whoIsOver21:
  print(g)

def table_one():
  for i in range(1,6):
    yield ("Chicken", "Table 1", "Seat {}".format(i))

def table_two():
  for i in range(1,6):
    yield ("Beef", "Table 2", "Seat {}".format(i))

def table_three():
  for i in range(1,6):
    yield ("Fish", "Table 3", "Seat {}".format(i))

def combined_tables():
  yield from table_one()
  yield from table_two()
  yield from table_three()

table_assignment = combined_tables()

def assign_tables(list_of_guests):
  for name in list_of_guests:
    yield (name, next(table_assignment))

guest_assignment = assign_tables(guests)

for person in guest_assignment:
  print(person)