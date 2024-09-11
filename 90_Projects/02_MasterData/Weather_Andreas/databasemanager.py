

__author__ = "Andreas"
__version__ = 1.0
__doc__ = """ 
sddsfdsf
sdfsdfsdf
sdfsdfsd
"""


import sqlite3
import logging
import mysql.connector
import config as cfg


class DataBaseManager:
    """Universal DataBase Manager which can be used for SQLite and MySQL based on config.json
    """

    def __init__(self) -> None:
        self.database_name = 'weather.db'

        if cfg.dbengine == '"sqlite':
            self.conn = sqlite3.connect('weather.db')
        else:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='user',
                password='geheim',
                database='weatherdb'
            )

    def execute_sql(self, sql: str, data: tuple = None) -> None:
        """Executes DML SQL Statement (Insert, Update, Delete)

        Args:
            sql (str): _description_
            data (tuple, optional): _description_. Defaults to None.
        """
        try:
            connection = sqlite3.connect(self.database_name)
            cursor = connection.cursor()

            if data:
                cursor.execute(sql, data)
            else:
                cursor.execute(sql)

            connection.commit()

        except sqlite3.Error as err:
            logging.error(f"Error: {err}")
        finally:
            if connection:
                cursor.close()
                connection.close()
                logging.info("SQLite connection closed")
