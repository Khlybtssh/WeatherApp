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

def get_search(id: int):

    db = SessionLocal()

    search = (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == id)
        .first()
    )

    db.close()

    return search

def delete_search(id: int):

    db = SessionLocal()

    search = (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == id)
        .first()
    )

    if search is None:
        db.close()
        return None

    db.delete(search)

    db.commit()

    db.close()

    return {"message": "Search deleted successfully"}

def update_search(id: int, city: str):

    db = SessionLocal()

    search = (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == id)
        .first()
    )

    if search is None:
        db.close()
        return None

    search.city = city

    db.commit()

    db.refresh(search)

    db.close()

    return search