# Weather App - Full Stack Technical Assessment

🚀 Live Frontend:
https://weather-app-tau-eight-30.vercel.app

🔧 Live Backend API:
https://weatherapp-4fu9.onrender.com

📚 Swagger Documentation:
https://weatherapp-4fu9.onrender.com/docs

## Overview

This project was developed as a submission for the AI Engineer Intern Technical Assessment.

The application allows users to search for a city and retrieve real-time weather information and multi-day forecasts using external weather APIs. In addition to weather retrieval, the system stores search history in a database and provides full CRUD functionality, data export capabilities, validation, and error handling.

The project demonstrates both backend and frontend development skills through a FastAPI REST API and a React-based user interface.

---

## Assessment Requirements Covered

### Backend

* REST API development using FastAPI
* External API integration (Open-Meteo)
* SQLite database persistence
* Full CRUD operations
* Input validation
* Error handling
* CSV data export

### Frontend

* React-based user interface
* Weather search functionality
* Multi-day forecast display
* User-friendly error messages
* Frontend-backend communication

---

## Application Preview

### Weather Search Interface

Users can search for weather information by city name.

<img width="1127" height="690" alt="Weather Search Interface" src="https://github.com/user-attachments/assets/91c7bc11-afe2-4a2b-87c8-456962fda394" />

---

### Weather Forecast Results

The application displays current weather conditions along with forecast data retrieved from external weather services.

<img width="1127" height="688" alt="Weather Forecast Results" src="https://github.com/user-attachments/assets/026e609c-660b-4604-bc80-28fbb1e206df" />

---

### FastAPI API Documentation

Interactive Swagger documentation is automatically generated for testing and exploring API endpoints.

<img width="992" height="636" alt="FastAPI Swagger Documentation" src="https://github.com/user-attachments/assets/f6cacd43-f5c3-41e3-afed-f36add516b38" />

---

## Features

### Weather Search

* Search weather information by city name.
* Retrieve real-time weather data.
* Display multi-day weather forecasts.
* Validate city existence before processing requests.

### Error Handling

* Invalid city detection.
* User-friendly error messages.
* Graceful handling of API failures.

### Database Persistence

Every successful weather search is stored in SQLite.

Stored information includes:

* City name
* Current temperature
* Search history records

### CRUD Operations

#### Create

Store weather search results in the database.

#### Read

* Retrieve all stored searches.
* Retrieve a specific search by ID.

#### Update

Update existing weather records.

#### Delete

Delete existing weather records.

### Data Export

Export weather history records as CSV files.


### Weather Search

* Search weather information by city name.
* Retrieve real-time temperature data.
* Display a multi-day weather forecast.
* Validate user input and city existence.

### Error Handling

* Handles invalid city names gracefully.
* Displays meaningful error messages to users.
* Handles external API failures.

### Database Persistence

Every successful weather search is stored in a SQLite database.

Stored information includes:

* City name
* Current temperature
* Search history records

### CRUD Operations

#### Create

Store weather search results in the database.

#### Read

* View all stored searches.
* View a specific search by ID.

#### Update

Update existing weather search records.

#### Delete

Delete weather search records.

### Data Export

Export stored weather history data to CSV format.

---

## Architecture

The project follows a layered architecture to keep responsibilities separated and maintain clean code.

### Backend

#### FastAPI

Provides REST API endpoints.

#### Service Layer

Contains business logic for:

* Weather retrieval
* Forecast processing
* Validation

#### Repository Layer

Handles all database interactions.

#### SQLite Database

Stores weather search history.

#### External APIs

Open-Meteo APIs are used for:

* Geocoding city names
* Retrieving current weather
* Retrieving weather forecasts

---

## Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Requests
* Pydantic

### Frontend

* React
* Vite
* JavaScript
* CSS

---

## Project Structure

```text
Weather App
│
├── Front/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── public/
│   └── package.json
│
├── database.py
├── models.py
├── schemas.py
├── main.py
├── weather_client.py
├── weather_service.py
├── weather_repository.py
│
└── weather.db
```

---

## API Endpoints

### Weather

```http
GET /api/v1/weather/{city}
```

Returns:

* Current temperature
* Forecast information

---

### History

```http
GET /history
```

Returns all saved weather searches.

```http
GET /history/{id}
```

Returns a specific search record.

---

### Update

```http
PUT /history/{id}
```

Updates a saved weather record.

---

### Delete

```http
DELETE /history/{id}
```

Deletes a saved weather record.

---

### Export

```http
GET /export/csv
```

Exports saved weather history as a CSV file.

---

## Running the Backend

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

Navigate to the frontend directory:

```bash
cd Front
```

Install dependencies:

```bash
npm install
```

Run the React application:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

## Demonstrated Skills

This project demonstrates:

* REST API Development
* External API Integration
* Database Design
* CRUD Operations
* Error Handling
* Backend Architecture
* Frontend Development
* Frontend-Backend Communication
* Data Export Functionality
* Clean Code Organization

---

## Author

Osama Yousef

AI Engineer Intern Applicant

Technical Assessment Submission for PM Accelerator
