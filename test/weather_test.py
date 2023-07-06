import unittest
from weather import Weather


class weatherTest(unittest.TestCase):

    def setUp(self):
        self.weather_obj = Weather()

    def test_call_weather_api(self):
        file = 'data/test.json'
        full_url = full_url = self.weather_obj.weather_api_url + 'Street 10, 75001 Paris, France' + "/?key=" + self.weather_obj.weather_api_key
        response = self.weather_obj.call_weather_api(full_url, file)
        self.assertIn('advance_time', response)

    def test_does_file_exists(self):
        self.assertFalse(self.weather_obj.does_file_exists('data/ab.json'))
        self.assertTrue(self.weather_obj.does_file_exists('data/test.json'))

    def test_check_and_get_weather_data_cached(self):
        full_url = 'test'
        pin_code = 'test'
        response = self.weather_obj.check_and_get_weather_data(full_url, pin_code)
        self.assertIn('advance_time', response)

