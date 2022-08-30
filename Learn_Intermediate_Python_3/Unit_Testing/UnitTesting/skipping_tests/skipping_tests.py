import unittest
import entertainment

class EntertainmentSystemTests(unittest.TestCase):

  @unittest.skipIf(entertainment.regional_jet(), 'Not available on regional jets')
  def test_movie_license(self):
    daily_movie = entertainment.get_daily_movie()
    licensed_movies = entertainment.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  @unittest.skipUnless(entertainment.regional_jet() is False, 'Not available on regional jets')
  def test_wifi_status(self):
    wifi_enabled = entertainment.get_wifi_status()
    self.assertTrue(wifi_enabled)

  def test_device_temperature(self):

    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')

    device_temp = entertainment.get_device_temp()
    self.assertLess(device_temp, 35)

  def test_maximum_display_brightness(self):

    if entertainment.regional_jet():
      self.skipTest('Not available on regional jets')

    brightness = entertainment.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)


unittest.main()