from sqlalchemy import Column, Integer, String, Float
from database import Base

class WeatherSearch(Base):
    __tablename__ = "weather_searches"

    id = Column(Integer, primary_key=True, index=True)

    city = Column(String)

    current_temperature = Column(Float)