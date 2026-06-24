import { useState } from "react";
import "./App.css";

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const getWeather = async () => {
  try {
    setLoading(true);
    setError("");

    const response = await fetch(`https://weatherapp-4fu9.onrender.com/api/v1/weather/${city}`);

    const data = await response.json();

    if (!response.ok) {
      setError(data.detail);
      setWeather(null);
      setLoading(false);
      return;
    }

    setWeather(data);
    setLoading(false);

  } catch (err) {
    setError("Failed to fetch weather");
    setWeather(null);
    setLoading(false);
  }
};

  return (
    <div className="container">
      <h1>Weather App</h1>

      <input
        type="text"
        placeholder="Enter city"
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />

      <button onClick={getWeather}>
        Get Weather
      </button>

      {error && (
        <p className="error">
          {error}
        </p>
      )}

      {weather && (
        <>
          <h2>{weather.city}</h2>

          <h3>
            Current Temperature:
            {" "}
            {weather.current_temperature}°C
          </h3>

          <div className="forecast">
            {weather.forecast.map((day) => (
              <div
                key={day.date}
                className="forecast-card"
              >
                <h4>
  {new Date(day.date).toLocaleDateString(
    "en-US",
    {
      day: "numeric",
      month: "short",
    }
  )}
</h4>

                <p>
                  Max: {day.max_temp}°C
                </p>

                <p>
                  Min: {day.min_temp}°C
                </p>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}

export default App;
