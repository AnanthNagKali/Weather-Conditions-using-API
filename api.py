import requests
import os
from datetime import datetime

api = os.environ['weather_api']
location = input('enter your location:')

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
#print(api_data)
if api_data['cod'] == '404':
    print("Invalid location:{},Please check you location name".format(location))
else:
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt=api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-------------------------------------------------------")
    print("Weather stats for - {} || {}".format(location.upper(),date_time))
    print("--------------------------------------------------------")

    print("current temperature : {:.2f} deg C".format(temp_city))
    print("Current weather desc :",weather_desc)
    print("current humidity:",hmdt,'%')
    print("current wind speed:",wind_spd,'kmph')