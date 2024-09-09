import requests
from pprint import pprint
import datetime

import json


import os
from pathlib import Path
os.chdir(Path(__file__).parent)


LAT = 52.5244
LON = 13.4105
API_KEY = "bf74a3d336b9f22dd6af67b521a73839"
UNIT = "metric"
LANG = "de"
CITY = "Berlin"
COUNTRY = "de"

EXPORT_FILE = "myweather.json"

url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units={UNIT}&lang={LANG}"


url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid={API_KEY}&units={UNIT}&lang={LANG}"


# Call the End Point
response = requests.get(url)
data = response.json()


pprint(data)


# Get Temperature
print(data["main"]["temp"])

# Get Desc
print(data["weather"][0]["description"])

sunrise = data["sys"]["sunrise"]  # UTC
sunrise = datetime.datetime.fromtimestamp(sunrise)
print(sunrise)


sunset = data["sys"]["sunset"]  # UTC
sunset = datetime.datetime.fromtimestamp(sunset)
print(sunset)


# Save to a LOCAL JSON
data = json.dumps(data)

with open(f"./json_imports/{EXPORT_FILE}", mode="w", encoding="UTF-8") as file:
    file.write(data)


# Save2 to a LOCAL JSON
with open(f"./json_imports/{EXPORT_FILE}", mode="w", encoding="UTF-8") as file:
    json.dump(data, file)
