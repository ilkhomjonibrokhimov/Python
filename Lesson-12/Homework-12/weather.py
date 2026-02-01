from bs4 import BeautifulSoup
import requests
import os

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "weather.html")

with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

weather_data = []

rows = soup.find("tbody").find_all('tr')
for row in rows:
    cols = row.find_all('td')
    day = cols[0].text.strip()
    temp = int(cols[1].text.replace("°C", "").strip())
    condition = cols[2].text.strip()

    weather_data.append({
        'day': day,
        "temperature": temp,
        'condition': condition
    })

print(weather_data)

print("\n5-day weather forecast: ")
for data in weather_data:
    print(f"{data['day']}: {data['temperature']}°C, {data['condition']}")

max_temp = max(item['temperature'] for item in weather_data)
hot_day = [item['day'] for item in weather_data if item['temperature'] == max_temp]
print(f"\nThe highest tempereature: {max_temp}°C on {(',').join(hot_day)}")

sunny = [item['day'] for item in weather_data if item['condition'] == 'Sunny']
print(f"Sunny days: {(', ').join(sunny)}")

average_temp = sum(item['temperature'] for item in weather_data) / len(weather_data)
print(f"\nAverage temperature for the week: {average_temp:.2f}°C\n")

