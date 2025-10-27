import requests
import sys

input_city = sys.argv[1]
geocoding_url = "https://nominatim.openstreetmap.org/search"
geocoding_params = {"q": input_city, "format": "json", "addressdetails": "1"}
geocoding_headers = {"User-Agent": "OpenStreetMeteo/1.0"}

#lat = None
#long = None
#weather_url = "https://api.open-meteo.com/v1/forecast?"
#weather_params = {"latitude": lat, "longitude": long, "current": "temperature_2m&wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"}

geocoding_request = requests.get(url=geocoding_url, params=geocoding_params, headers=geocoding_headers)
geocoding_json = geocoding_request.json()

print(geocoding_json)