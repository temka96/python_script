#from pyowm import OWM
# import os

# #https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=d0fc3409700ca80d231ea8402ca0b872
# owm = OWM('e43287f5a8c17a47f63c5ea01efe4869')
# city = os.environ.setdefault('CITY_NAME', 'Саратов')
# api = os.environ.setdefault('OPENWEATHER_API_KEY', 'd0fc3409700ca80d231ea8402ca0b872')


import pyowm

owm =  pyowm.OWM('d0fc3409700ca80d231ea8402ca0b872')

place = input("В каком городе/стране?: ")
observation = owm.weather_at_place(place)
w = observation.get_weather()

print("В городе " + place + " сейчас " + w.get_detailed_status())
temp = w.get_temperature('celsius')['temp']
print('Температура в районе: ' + str(temp) + '°C')