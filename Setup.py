from mysql.connector import errorcode
import mysql.connector
from CarRenatlBackend import cursor

DB_NAME = "car_rental"

def createDatabase():
    query = f'create database if not exists {DB_NAME}'
    cursor.execute(query)
    print(f'Database {DB_NAME} created')

TABLES = {}
TABLES["todos"] = (
    "create table `todos`("
    "`id` int(11) not null auto_increment,"
    "`todo` varchar(255) not null,"
    "`created_on` datetime default current_timestamp,"
    "primary key(`id`)"
    ")"
)

def createTables():
    query = f'use {DB_NAME}'
    cursor.execute(query)

    for table_name in TABLES:
        query_table = TABLES[table_name]
        try:
            print(f'creating table {table_name}')
            cursor.execute(query_table)
            print(f'created {table_name} table')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print(f'{table_name} already exists!')
            else:
                print(err.msg)

# createDatabase()
# createTables()
