# Weather App - Full Stack Technical Assessment

## Overview

This project is a full-stack weather application built as part of the AI Engineer Intern Technical Assessment.

The application allows users to search for any city and retrieve real-time weather information and forecast data using external weather APIs. The project demonstrates backend API development, database integration, CRUD operations, data persistence, error handling, and frontend-backend communication.

---

## Features
<img width="1125" height="688" alt="image" src="https://github.com/user-attachments/assets/ed308d66-0878-47e5-8384-d523b6339402" />

<img width="1127" height="688" alt="image" src="https://github.com/user-attachments/assets/026e609c-660b-4604-bc80-28fbb1e206df" />

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

AI Engineer Intern Technical Assessment Submission
