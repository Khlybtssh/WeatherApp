from fastapi import HTTPException
import requests

def get_coordinates(city: str):

    url = (
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    )

    response = requests.get(url)

    data = response.json()

    if "results" not in data:
        raise HTTPException(
            status_code=404,
            detail=f"City '{city}' not found"
        )

    result = data["results"][0]

    return (
        result["latitude"],
        result["longitude"]
    )


def fetch_weather(lat: float, lon: float):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}"
        f"&longitude={lon}"
        f"&current=temperature_2m"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&timezone=auto"
    )

    response = requests.get(url)

    return response.json()

