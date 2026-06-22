from weather_client import get_coordinates, fetch_weather
from weather_repository import create_search


def get_weather(city: str):

    lat, lon = get_coordinates(city)

    weather = fetch_weather(lat, lon)

    temperature = weather["current"]["temperature_2m"]

    create_search(
        city=city,
        temperature=temperature
    )

    forecast = []

    daily = weather["daily"]

    for i in range(len(daily["time"])):

        forecast.append({
            "date": daily["time"][i],
            "max_temp": daily["temperature_2m_max"][i],
            "min_temp": daily["temperature_2m_min"][i]
        })

    return {
        "city": city,
        "current_temperature": temperature,
        "forecast": forecast
    }