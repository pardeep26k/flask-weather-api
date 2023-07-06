import requests
import json
import os
from datetime import datetime, timedelta, time


class Weather:
    def __init__(self):
        self.weather_api_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
        self.weather_api_key = 'W6EHL9RPQ2MQRPLL5F993C8D8'

    def get_weather(self, data):
        if type(data) is not list:
            return data
        for i in range(len(data)):
            location = data[i][5] + data[i][6] + data[i][7]
            full_url = self.weather_api_url + location + "/?key=" + self.weather_api_key
            response = self.check_and_get_weather_data(full_url, data[i][8])
            data[i].append(response)
        return [data]

    def check_and_get_weather_data(self, full_url, pin_code):
        file_name = 'data/' + pin_code + '.json'
        if self.does_file_exists(file_name):
            file = open(file_name)
            weather_data = json.load(file)
            format_date = datetime.strptime(weather_data['advance_time'], "%Y-%m-%d, %H:%M:%S")
            current_date_time = datetime.now()
            # check here if 2 hrs expired or not
            if current_date_time > format_date:
                os.remove(file_name)
                return self.call_weather_api(full_url, file_name)
            else:
                return weather_data

        else:
            return self.call_weather_api(full_url, file_name)

    def does_file_exists(self, file_path_name):
        return os.path.exists(file_path_name)

    def call_weather_api(self, full_url, file_name):
        response = requests.get(full_url)
        weather_data = response.json()
        # Logic here to save the weather data in files with pincode name and put the advance time for 2 hours so that
        # in future request we can validate file data without calling api
        now = datetime.now() + timedelta(hours=2)
        weather_data['advance_time'] = now.strftime("%Y-%m-%d, %H:%M:%S")
        with open(file_name, 'w') as f:
            json.dump(weather_data, f)
        return weather_data
