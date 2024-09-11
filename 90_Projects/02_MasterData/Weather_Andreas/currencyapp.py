import logging
import json

import mysql.connector
import sqlite3
from databasemanager import DataBaseManager
import config as cfg


class CurrencyApp:
    def __init__(self):
        self.api_key = cfg.config["currency_api_key"]
        self.export_file = cfg.config["currency_export_file"]
        self.currency_data = {}
        self.db = DataBaseManager()

    # Die Währungsdaten werden von der API abgerufen und in self.currency_data gespeichert
    def fetch_currency_data(self):
        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/EUR"
        response = requests.get(url)
        data = response.json()
        eur_to_usd = data["conversion_rates"]["USD"]
        usd_to_eur = 1 / eur_to_usd
        self.currency_data = {
            "EUR_to_USD": eur_to_usd,
            "USD_to_EUR": usd_to_eur
        }
        logging.info("Fetched currency data")
        return self.currency_data

    # Währungsdaten werden in einer JSON-Datei gespeichert
    def save_to_json(self):
        with open(self.export_file, 'w', encoding='utf-8') as f:
            json.dump(self.currency_data, f, ensure_ascii=False, indent=4)
        logging.info(f"Currency data saved to {self.export_file}")

    # Währungsdaten werden in einer MySQL-Datenbank gespeichert
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
            # Eine Tabelle currency wird erstellt, falls sie noch nicht existiert
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS currency (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    eur_to_usd FLOAT,
                    usd_to_eur FLOAT
                )
            """)
            # Die Währungsdaten werden in die Tabelle eingefügt
            cursor.execute("""
                INSERT INTO currency (eur_to_usd, usd_to_eur)
                VALUES (%s, %s)
            """, (self.currency_data["EUR_to_USD"], self.currency_data["USD_to_EUR"]))
            connection.commit()
            logging.info("Currency data saved to MySQL database")
        except mysql.connector.Error as err:
            logging.error(f"Error: {err}")
        finally:
            # Die Verbindung zur Datenbank wird geschlossen
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                logging.info("MySQL connection closed")

    # Währungsdaten werden in einer SQLite-Datenbank gespeichert
    def save_to_sqlite(self):
        connection = None
        try:
            connection = sqlite3.connect('weather.db')
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS currency (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    eur_to_usd REAL,
                    usd_to_eur REAL
                )
            """)
            cursor.execute("""
                INSERT INTO currency (eur_to_usd, usd_to_eur)
                VALUES (?, ?)
            """, (self.currency_data["EUR_to_USD"], self.currency_data["USD_to_EUR"]))
            connection.commit()
            logging.info("Currency data saved to SQLite database")
        except sqlite3.Error as err:
            logging.error(f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()
                logging.info("SQLite connection closed")

    def create_table(self):
        sql = """
                CREATE TABLE IF NOT EXISTS currency (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    eur_to_usd REAL,
                    usd_to_eur REAL
                )
            """
        self.db.execute_sql(sql)

        logging.info("Currency data saved to SQLite database")

    def insert_data(self):
        data = (self.currency_data["EUR_to_USD"],
                self.currency_data["USD_to_EUR"])
        sql = """
                INSERT INTO currency (eur_to_usd, usd_to_eur)
                VALUES (?, ?)
                )
            """
        self.db.execute_sql(sql, data)

        logging.info("Currency data saved to SQLite database")
