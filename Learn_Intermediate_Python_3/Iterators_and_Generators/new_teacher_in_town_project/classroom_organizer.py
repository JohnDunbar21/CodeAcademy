from roster import student_roster
import itertools
# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students

  def __iter__(self):
    for i in self.sorted_names:
      print(next(i))

  def table_configs(self):
    configs = itertools.combinations(self.sorted_names, 2)
    print(list(configs))

  def table_fav_subject_configs(self, students):
    student_subs = []
    for student in students:
      if student['favorite_subject'] == 'Math' or student['favorite_subject'] == 'Science':
        student_subs.append(student)
    configs = itertools.combinations(student_subs, 4)
    print(list(configs))