import logging
import json

import mysql.connector
import sqlite3
import config as cfg


class WeatherApp:
    # Klasse WeatherApp wird initialisiert
    def __init__(self):
        self.api_key = cfg.config["api_key"]
        self.cities = cfg.config["city"]
        self.langs = cfg.config["lang"]
        self.unit = cfg.config["unit"]
        self.export_file = cfg.config["export_file"]
        self.weather_data = []

    # Die Wetterdaten werden von der OpenWeatherMap abgrufen und in self.weather_data gespeichert
    def fetch_data(self):
        for city in self.cities:
            weather_info = {"city": city}
            for lang in self.langs:
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units={self.unit}&lang={lang}"
                response = requests.get(url)
                data = response.json()
                if lang == "de":
                    weather_info["temperature"] = data["main"]["temp"]
                    weather_info["humidity"] = data["main"]["humidity"]
                    weather_info["description_de"] = data["weather"][0]["description"]
                elif lang == "en":
                    weather_info["description_en"] = data["weather"][0]["description"]
            self.weather_data.append(weather_info)
            logging.info(f"Fetched weather data for {city}")
        return self.weather_data

    # Wetterdaten werden in einer JSON-Datei gespeichert
    def save_to_json(self):
        with open(self.export_file, 'w', encoding='utf-8') as f:
            json.dump(self.weather_data, f, ensure_ascii=False, indent=4)
        logging.info(f"Weather data saved to {self.export_file}")

    # Wetterdaten werden in einer MySQL-Datenbank gespeichert
    def save_to_mysql(self):
        connection = None
        try:
            # Es wird eine Verbindung zur MySQL-Datenbank hergestellt
            connection = mysql.connector.connect(
                host='localhost',
                user='user',
                password='geheim',
                database='weatherdb'
            )
            cursor = connection.cursor()
            # Eine Tabelle weather wird erstellt, falls sie noch nicht existiert
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS weather (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    city VARCHAR(255),
                    temperature FLOAT,
                    humidity INT,
                    description_de VARCHAR(255),
                    description_en VARCHAR(255)
                )
            """)
            # Die Wetterdaten werden in die Tabelle eingefügt
            for data in self.weather_data:
                cursor.execute("""
                    INSERT INTO weather (city, temperature, humidity, description_de, description_en)
                    VALUES (%s, %s, %s, %s, %s)
                """, (data["city"], data["temperature"], data["humidity"], data["description_de"], data["description_en"]))
            connection.commit()
            logging.info("Weather data saved to MySQL database")
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
        finally:
            # Die Verbindung zur Datenbank wird geschlossen
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                logging.info("MySQL connection closed")

    # Wetterdaten werden in einer SQLite-Datenbank gespeichert
    def save_to_sqlite(self):
        connection = None
        try:
            connection = sqlite3.connect('weather.db')
            cursor = connection.cursor()
            cursor.execute("""
              
                )
            """)
            for data in self.weather_data:
                cursor.execute("""
                    INSERT INTO weather (city, temperature, humidity, description_de, description_en)
                    VALUES (?, ?, ?, ?, ?)
                """, (data["city"], data["temperature"], data["humidity"], data["description_de"], data["description_en"]))
            connection.commit()
            logging.info("Weather data saved to SQLite database")
        except sqlite3.Error as err:
            logging.error(f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()
                logging.info("SQLite connection closed")

    def create_table(self):
        sql = """
                 CREATE TABLE IF NOT EXISTS weather (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT,
                    temperature REAL,
                    humidity INTEGER,
                    description_de TEXT,
                    description_en TEXT
                )
            """
        self.db.execute_sql(sql)

        logging.info("Currency data saved to SQLite database")

    def insert_data(self):
        data = (data["city"], data["temperature"], data["humidity"],
                data["description_de"], data["description_en"])
        sql = """
                INSERT INTO weather (city, temperature, humidity, description_de, description_en)
                    VALUES (?, ?, ?, ?, ?)
                )
            """
        self.db.execute_sql(sql, data)

        logging.info("Currency data saved to SQLite database")
