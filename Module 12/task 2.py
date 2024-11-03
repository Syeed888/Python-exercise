import requests
import json

def get_weather(city_name):
    api_key = "0d7f342ba758dff66f8e9edc30a5c79c"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    parameter = {
        "q": city_name,
        "appid": api_key
    }

    response = requests.get(base_url, params=parameter)
    data = response.json()

    if response.status_code == 200:

        weather_description = data['weather'][0]['description']
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15

        print(f"Weather in {city_name.capitalize()}: {weather_description}")
        print(f"Temperature: {temp_celsius:.2f}°C")
    else:
        print("City not found.")


city_name = input("Enter the name of the municipality: ")
get_weather(city_name)
