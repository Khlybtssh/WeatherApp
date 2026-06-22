from fastapi import FastAPI, HTTPException
from typing import Any
from datetime import datetime       
import requests
import weather_service, schemas
from schemas import WeatherResponse
from database import engine
from models import Base
from weather_repository import get_searches
app = FastAPI()

@app.get("/api/v1/weather/{city}",response_model= WeatherResponse)
def get_weather(city: str):

    return weather_service.get_weather(city)


Base.metadata.create_all(bind=engine)

@app.get("/history")
def get_history():

    return get_searches()