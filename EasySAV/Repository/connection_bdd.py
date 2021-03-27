import mysql.connector


def start():
    database = mysql.connector.connect(
        host="89.87.208.225",
        user="root",
        passwd="root",
        database="easy_sav"
    )

    return database
