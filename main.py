import requests

input_city = "Kelowna, BC"
geocoding_url = "https://nominatim.openstreetmap.org/search"
geocoding_params = {"q": input_city, "format": "json", "addressdetails": "1"}

city_char_list = []

for i in input_city:
    if i == " ":
        city_char_list.append("+")
    else:
        city_char_list.append(i)

city_parsed = "".join(city_char_list)

#lat = None
#long = None
#weather_url = "https://api.open-meteo.com/v1/forecast?"
#weather_params = {"latitude": lat, "longitude": long, "current": "temperature_2m&wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"}

geocoding_json = requests.get(url=geocoding_url, params=geocoding_params)

print(geocoding_json)