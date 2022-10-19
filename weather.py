import requests, json
from decouple import config

WEATHER_API_KEY = config('WEATHER')

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


class City:
    def __init__(self,name,lon,lat):
        self.name = name 
        self.lon = lon 
        self.lat = lat 


basra = City("Basra ,IQ","47.783489","30.508102")

baghdad = City("Baghdad, IQ","44.361488","30.508102")



limit = 5
URL = BASE_URL + "lat=" + basra.lat + "&lon=" + basra.lon +"&lang=ar"+"&units=metric"+ "&appid=" + WEATHER_API_KEY

def getCurrentWeather():

    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()

        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
     
        
        return f""" \n
        {basra.name:-^30} \n
        درجة الحرارة : {temperature} °C\n
        الرطوبة : {humidity} %\n
        الضغط : {pressure} hPa\n
        {report[0]['description']}
        
        """
    else:
        print("Error in the HTTP request")