import sys
from pyowm import OWM
import os
import requests

city = os.environ.setdefault('CITY_NAME', 'Москва')
api = os.environ.setdefault('OPENWEATHER_API_KEY', 'd0fc3409700ca80d231ea8402ca0b872')

# r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric")
# data = r.json()
# weather = data['main']['temp']
# wind = data['wind']['speed']
# weathe_description = data['weather'][0]['description']
# # print(f"Погода в городе {city} {weather} градусов, скорость ветра {wind}")


owm = OWM(api)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
weather = observation.weather
temp = weather.temperature('celsius')['temp']
#print(temp)

sys.stdout.write(str(temp))
