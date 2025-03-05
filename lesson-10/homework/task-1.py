import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print(f"Failed to retrieve weather data. Error {response.status_code}: {response.text}")

API_KEY = "your_api_key_here"
CITY_NAME = "Tashkent"

get_weather(CITY_NAME, API_KEY)
