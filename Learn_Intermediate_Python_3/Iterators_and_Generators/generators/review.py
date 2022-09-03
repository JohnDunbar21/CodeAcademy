def summa():
    yield 'Summa Cum Laude'
def magna():
    yield 'Magna Cum Laude' 
def cum_laude():
    yield 'Cum Laude'

days = 25
gpas = [3.2, 4.0, 3.6, 2.9]

def honors_generator(gpas):
  for gpa in gpas:
    if gpa > 3.9:
      yield from summa()
    elif gpa > 3.7:
      yield from magna()
    elif gpa > 3.5:
      yield from cum_laude()

def graduation_countdown(days):
  days_left = days
  while days >= 0:
    try:
      days_left = yield days
      if days_left is not None:
        days = days_left
        continue
      else:
        days -= 1
    except:
      print("{Generator Terminated}")
      break

countdown_generator= (day for day in range(days, -1, -1))

grad_days = graduation_countdown(days)

for day in grad_days:
  if day == 15:
    grad_days.send(10)
  elif day == 3:
    grad_days.close()
  print("Days Left: "+str(day))

honors = honors_generator(gpas)

for student in honors:
  print(student)