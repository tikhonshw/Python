# owm = pyowm.OWM('a58cd71e6d3057b4ce76c3da27076585')

import pyowm

owm = pyowm.OWM('a58cd71e6d3057b4ce76c3da27076585')

place = input("Город: ")

# ob = owm.weather_at_place('Салехард, RU')
ob = owm.weather_at_place(place)
w = ob.get_weather()
temp = w.get_temperature('celsius')["temp"]


print("В городе " + place + " сейчас " + w.get_detailed_status() + " темепература : " + str(temp) )

# print(w)
