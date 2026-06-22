from database import SessionLocal
from models import WeatherSearch

def create_search(city, temperature):

    db = SessionLocal()

    search = WeatherSearch(
        city=city,
        current_temperature=temperature
    )

    db.add(search)
    db.commit()
    db.refresh(search)

    db.close()

    return search

def get_searches():

    db = SessionLocal()

    searches = db.query(WeatherSearch).all()

    db.close()

    return searches