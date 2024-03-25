import unittest
import requests
from unittest.mock import Mock

requests = Mock()
def get_weather(city):
    try:
        response = requests.get(f"https://api.weather.com/v1/weather?q={city}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None

class TestGetWeather(unittest.TestCase):

    def test_get_weather_request_made(self):

        response_m = Mock()
        response_m.status_code = 200
        response_m.json.return_value =  {'weather': 'sunny'}
        requests.get.return_value = response_m
        self.assertEqual(get_weather('test'), {'weather': 'sunny'})



unittest.main()
