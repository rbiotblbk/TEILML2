

from weatherapp import WeatherApp
from currencyapp import CurrencyApp
from oandaapp import OANDAApp
import config as cfg


def main():
    apps = [WeatherApp(), CurrencyApp(), OANDAApp()]
    for app in apps:
        app.fetch_data()
        app.save_to_json()
        app.save_to_mysql()
        app.save_to_sqlite()


if __name__ == "__main__":
    main()
