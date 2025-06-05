from fastapi import APIRouter
import requests
from pydantic import BaseModel
import json
from logging import INFO, Formatter, getLogger
from .weatherCodes import weather_status_codes as weatherDictionary
from dotenv import load_dotenv
from azure.monitor.opentelemetry import configure_azure_monitor


#load environmental variables
load_dotenv()

#set up logger name and formatter
configure_azure_monitor(
    logger_name = "my_azure_logger",
    logging_formatter=Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

)

#pass my azure logger to default logger and set level of logging to INFO
logger = getLogger("my_azure_logger")
logger.setLevel(INFO)


city_router = APIRouter()


class temperatureUnits(BaseModel):
    temperature_2m:str

class currentBase(BaseModel):
    temperature_2m:float

class Weather(BaseModel):
    latitude:float
    longitude:float
    current_units:temperatureUnits
    current:currentBase


def getWeatherData(data):
    temp = {
        key: (
            {k:v for k, v in value.items() if k =='temperature_2m'} 
            if key == 'current' and isinstance(value,dict)
            else 
            {k:v for k, v in value.items() if k == 'temperature_2m'}
            if key == 'current_units' and isinstance(value,dict)
            else value
        )
        for key, value in data.items()
        if key in ['latitude', 'longitude', 'current_units', 'current']
    }
    weather = Weather(**temp)
    return weather

def getCityCoord(city: str):
    cityParam = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json")
    cityParam = cityParam.json()
    return {"latitude": cityParam['results'][0]["latitude"], "longitude": cityParam['results'][0]['longitude']}

def checkRainLevel(coordinates: str):
    requestRainLevel = requests.get((f"https://api.open-meteo.com/v1/forecast?latitude={coordinates['latitude']}&longitude={coordinates['longitude']}&current=rain,weather_code"))
    requestRainLevel = requestRainLevel.json()
    return {"Rain level:" : requestRainLevel['current']['rain'], 
            "Current Weather": weatherDictionary[requestRainLevel['current']['weather_code']]}

@city_router.get("/temperature/{city}")
def get_city(city: str):
    cityCord = getCityCoord(city)
    requestWeather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={cityCord['latitude']}&longitude={cityCord['longitude']}&current=temperature_2m&forecast_days=1")
    currentWeather = getWeatherData(requestWeather.json())
    logger.info(currentWeather)
    return currentWeather

@city_router.get("/rain/{city}")
def checkRain(city: str):
    cityCord = getCityCoord(city)
    rainStatus = checkRainLevel(cityCord)
    return rainStatus
