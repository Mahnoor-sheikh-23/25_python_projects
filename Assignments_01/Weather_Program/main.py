import requests
from pprint import pprint

API_Key = "f0cec8b607d15725ccf6f92b50e85c0e"

city = input("Enter city name: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data  = requests.get(base_url).json()

pprint(weather_data)