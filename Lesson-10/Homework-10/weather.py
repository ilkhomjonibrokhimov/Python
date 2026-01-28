import requests

api_key = "3408efd4725cde57d2e1d44912d66b99"
lot = 41.315
lon = 69.289
URL = f'https://api.openweathermap.org/data/2.5/weather?lat={lot}&lon={lon}&appid={api_key}&units=metric'

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in Tashkent:")
    print("Temperature:", data['main']['temp'], "C")
    print("Sea level:", data['main']['sea_level'], "m")
    print("Humidity:", data['main']['humidity'], "%")
else:
    print(response.text)