import requests
from pprint import pprint
import datetime

import json


import os
from pathlib import Path
os.chdir(Path(__file__).parent)


# Read the config
with open("./config.json", mode="r", encoding="UTF-8") as file:
    config = json.load(file)


for city in config["city"]:

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config["api_key"]}&units={config["unit"]}&lang={config["lang"]}"

    # Call the End Point
    response = requests.get(url)
    data = response.json()

    print(f"City: {city}")
    print("=" * 50)

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

    print("\n\n")
