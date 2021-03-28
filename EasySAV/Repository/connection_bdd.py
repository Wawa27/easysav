import mysql.connector
import logging


def start():
    try:
        database = mysql.connector.connect(
            host="89.87.208.225",
            user="root",
            passwd="root",
            database="easy_sav"
        )
        return database

    except:
        logging.critical(" Connection with the database failed")
        exit()
