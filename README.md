# OpenStreetMeteo 🌞

## About

This project provides weather.py, a command line tool that takes in the name of a location as an argument, geocodes it using the Nominatim API, and pulls weather data for the location from Open-Meteo. Currently it returns hourly weather data for the current day printed in a table.

I started this project to practice formatting API requests and building command line tools. It might become the basis for more of my projects later on. 🙂

## Usage

**python weather.py "location"**

The API request uses Nominatim's [free form queries](https://nominatim.org/release-docs/develop/api/Search/#free-form-query)

## Dependencies

[requests](https://pypi.org/project/requests/)

[tabulate](https://pypi.org/project/tabulate/)

## APIs

Geocoding: OpenStreetMap Nominatim [(Website)](https://nominatim.org/) [(GitHub)](https://github.com/osm-search/Nominatim)

Weather: Open-Meteo [(Website)](https://open-meteo.com/) [(GitHub)](https://github.com/open-meteo/open-meteo)
