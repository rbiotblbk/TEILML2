import json
import logging


import os
from pathlib import Path
os.chdir(Path(__file__).parent)

# Logging wird konfiguriert
logging.basicConfig(filename='weather_app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Konfigurationsdatei config.json wird gelesen
with open("./config.json", mode="r", encoding="UTF-8") as file:
    config = json.load(file)
