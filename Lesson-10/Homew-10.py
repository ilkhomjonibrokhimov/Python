import requests

API_KEY = "3408efd4725cde57d2e1d44912d66b99"
CITY = "Tashkent"
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"  # Celsius
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Condition: {weather}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Status code:", response.status_code)
    print(response.text)

