import unittest
import feedback

class CustomerFeedbackTests(unittest.TestCase):

  # Write your code below:
  @unittest.expectedFailure
  def test_survey_form(self):
    self.assertEqual(feedback.issue_survey(), 'Success')

  def test_complaint_form(self):
    self.assertEqual(feedback.log_customer_complaint(), 'Success')

unittest.main()