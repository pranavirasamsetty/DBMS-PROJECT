import mysql.connector

config = {
    "user": "root",
    "host": "localhost"
}

db = mysql.connector.connect(**config)
cursor = db.cursor()