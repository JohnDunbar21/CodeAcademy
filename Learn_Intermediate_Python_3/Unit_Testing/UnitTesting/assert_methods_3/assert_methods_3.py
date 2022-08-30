import unittest
import alerts

# Write your code here:
class SystemAlertTests(unittest.TestCase):
  
  def test_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)

  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)

unittest.main()