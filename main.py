from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from typing import Any
from datetime import datetime       
import requests
import weather_service, schemas, csv
from schemas import WeatherResponse, UpdateSearch
from database import engine
from models import Base
from weather_repository import (
    get_searches,
    get_search,
    delete_search,
    update_search
)
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/api/v1/weather/{city}",response_model= WeatherResponse)
def get_weather(city: str):
    return weather_service.get_weather(city)

Base.metadata.create_all(bind=engine)

@app.get("/history")
def get_history():
    return get_searches()

@app.get("/history/{id}")
def get_history_record(id: int):
    return get_search(id)

@app.delete("/history/{id}")
def delete_history(id: int):

    result = delete_search(id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Record not found"
        )

    return result

@app.put("/history/{id}")
def update_history(
    id: int,
    request: UpdateSearch
):

    result = update_search(
        id=id,
        city=request.city
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Record not found"
        )

    return result

@app.get("/export/csv")
def export_csv():

    searches = get_searches()

    with open("weather_history.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "id",
            "city",
            "current_temperature"
        ])

        for search in searches:

            writer.writerow([
                search.id,
                search.city,
                search.current_temperature
            ])

    return FileResponse(
        "weather_history.csv",
        media_type="text/csv",
        filename="weather_history.csv"
    )