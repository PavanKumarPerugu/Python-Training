import requests
import json
import os

# Get the folder where the script is
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
# ----------------------------
# Step 0: Load API key from JSON
# ----------------------------
CONFIG_FILE = "config.json"

if not os.path.exists(CONFIG_FILE):
    print(f"Error: {CONFIG_FILE} not found! Please create it with your API key.")
    exit()

with open(CONFIG_FILE) as f:
    config = json.load(f)

api_key = config.get("OPENWEATHER_API_KEY")
if not api_key:
    print("Error: API key not found in config.json")
    exit()

# ----------------------------
# Step 1: Setup
# ----------------------------
city = input("Enter city name: ")
url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"  # temperature in Celsius
}

# ----------------------------
# Step 2: Call API
# ----------------------------
try:
    response = requests.get(url, params=params)
    data = response.json()
except requests.exceptions.RequestException as e:
    print("Network error:", e)
    exit()

# ----------------------------
# Step 3: Handle errors
# ----------------------------
if response.status_code != 200:
    print("Error:", data.get("message", "Something went wrong"))
    exit()

# ----------------------------
# Step 4: Print weather
# ----------------------------
print(f"\nWeather Report for {city}")
print("----------------------------")
print("Temperature:", data["main"]["temp"], "°C")
print("Humidity:", data["main"]["humidity"], "%")
print("Wind Speed:", data["wind"]["speed"], "m/s")
print("Condition:", data["weather"][0]["description"].title())
