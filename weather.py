import sys
import requests

input_city = sys.argv[1]
geocoding_url = "https://nominatim.openstreetmap.org/search"
geocoding_params = {
    "q": input_city,
    "format": "json",
    "addressdetails": "1"}
geocoding_headers = {"User-Agent": "OpenStreetMeteo/1.0"}

geocoding_request = requests.get(url=geocoding_url, params=geocoding_params, headers=geocoding_headers)
geocoding_json = geocoding_request.json()
geocoding_dict = geocoding_json[0]
lat = geocoding_dict["lat"]
lon = geocoding_dict["lon"]

weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {
    "latitude": lat,
	"longitude": lon,
    "current": ["temperature_2m", "precipitation", "wind_speed_10m", "wind_direction_10m"],
	"hourly": ["temperature_2m", "precipitation", "wind_speed_10m", "wind_direction_10m"],
    "timezone": "auto",
    "forecast_days": 1
}

weather_request = requests.get(url=weather_url, params=weather_params)
weather_json = weather_request.json()

current_weather = weather_json["current"]

print(current_weather)