from pydantic import BaseModel

class ForecastDay(BaseModel):
    date: str
    max_temp: float
    min_temp: float


class WeatherResponse(BaseModel):
    city: str
    current_temperature: float
    forecast: list[ForecastDay]