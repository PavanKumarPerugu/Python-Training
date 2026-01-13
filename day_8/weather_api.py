import requests

# Ask user for city name
city = input("Enter city name: ")

# -------------------------------
# Step 1: Get latitude & longitude from city name
# -------------------------------
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {
    "name": city,
    "count": 1
}

geo_response = requests.get(geo_url, params=geo_params)
geo_data = geo_response.json()

if "results" not in geo_data:
    print("City not found.")
    exit()

latitude = geo_data["results"][0]["latitude"]
longitude = geo_data["results"][0]["longitude"]

# -------------------------------
# Step 2: Get weather data
# -------------------------------
weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

weather_response = requests.get(weather_url, params=weather_params)
weather_data = weather_response.json()

current = weather_data["current_weather"]

# -------------------------------
# Weather code meanings
# -------------------------------
weather_codes = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    95: "Thunderstorm"
}

weather_code = current["weathercode"]
weather_description = weather_codes.get(weather_code, "Unknown weather condition")

# -------------------------------
# Step 3: Display weather
# -------------------------------
print("\nWeather Report for", city)
print("------------------------")
print("Temperature:", current["temperature"], "°C")
print("Wind Speed:", current["windspeed"], "km/h")
print("Weather Code:", weather_code)
print("Condition:", weather_description)
