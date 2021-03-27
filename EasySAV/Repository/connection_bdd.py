import mysql.connector


def __init__(self):
    cnx = mysql.connector.connect(
        host="89.87.208.225",
        user="root",
        passwd="root",
        database="easy_sav"
    )
