import sys
#from pyowm import OWM
import os
import requests

city = os.environ['CITY_NAME']
api = os.environ['OPENWEATHER_API_KEY']

r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric")
data = r.json()
weather = data['main']['temp']
wind = data['wind']['speed']
weathe_description = data['weather'][0]['description']
print(f"Погода в городе {city} {weather} градусов, скорость ветра {wind}")


# owm = OWM(api)
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place(city)
# weather = observation.weather
# temp = weather.temperature('celsius')['temp']
# print(temp)
# sys.stdout.write(str(temp))
