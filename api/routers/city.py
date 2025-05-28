from fastapi import APIRouter
import requests
from pydantic import BaseModel
import json

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

@city_router.get("/{city}")
def get_city(city: str| None = "Warsaw"):
    cityCord = getCityCoord(city)
    requestWeather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={cityCord['latitude']}&longitude={cityCord['longitude']}&current=temperature_2m&forecast_days=1")
    currentWeather = getWeatherData(requestWeather.json())
    return currentWeather