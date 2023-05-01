import requests
# http://api.openweathermap.org/data/2.5/forecast?q=Салехард&lang=ru&appid=a58cd71e6d3057b4ce76c3da27076585
# полученный при регистрации на OpenWeatherMap.org.
appid = "a58cd71e6d3057b4ce76c3da27076585"

def get_wind_direction(deg):
    l = ['С ','СВ',' В','ЮВ','Ю ','ЮЗ',' З','СЗ']
    for i in range(0, 8):
        step = 45
        min = i*step - 45/2
        max = i*step + 45/2
        if i == 0 and deg > 360-45/2:
            deg = deg - 360
        if deg >= min and deg <= max:
            res = l[i]
            break
    return res

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': 'Салехард,RU', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print('city:', data['city']['name'], data['city']['country'])
    for i in data['list']:
        print( (i['dt_txt'])[:16], '{0:+3.0f}'.format(i['main']['temp']),
               '{0:2.0f}'.format(i['wind']['speed']) + " м/с",
               get_wind_direction(i['wind']['deg']),
               i['weather'][0]['description'] )
except Exception as e:
    print("Exception (forecast):", e)
    pass
