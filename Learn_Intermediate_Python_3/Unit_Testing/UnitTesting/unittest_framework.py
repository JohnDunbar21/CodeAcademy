# Checkpoint 1
import unittest

def get_nearest_exit(row_number):
  if row_number < 15:
    location = 'front'
  elif row_number < 30:
    location = 'middle'
  else:
    # Checkpoint 6
    location = 'back'
  return location

# Checkpoint 2
class NearestExitTests(unittest.TestCase):
  # Checkpoint 3
  def test_row_1(self):
    self.assertEqual(get_nearest_exit(1), 'front', 'The nearest exit to row 1 is in the front!')
    
  # Checkpoint 3
  def test_row_20(self):
    self.assertEqual(get_nearest_exit(20), 'middle', 'The nearest exit to row 20 is in the middle!')
    
  # Checkpoint 3
  def test_row_40(self):
    self.assertEqual(get_nearest_exit(40), 'back', 'The nearest exit to row 40 is in the back!')

# Checkpoint 4
unittest.main()