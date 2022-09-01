from roster import student_roster
from classroom_organizer import ClassroomOrganizer

student_iter = iter(student_roster)

print("\n")
print("Iterating through students in roster...")
print("\n")
for i in range(len(student_roster)):
  print(next(student_iter))

print("\n")

c_org = ClassroomOrganizer()
print("Combinations of tables of two generating...")
print("\n")
c_org.table_configs()
print("\n")
print("Combinations of tables of four that also share an interest in Math and Science...")
print("\n")
c_org.table_fav_subject_configs(student_roster)