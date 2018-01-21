# project/db_create.py


import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # create the table
    c.execute("""CREATE TABLE potluck(potluck_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, food_item TEXT NOT NULL, comments TEXT NOT NULL)""")

    # insert dummy data into the table
    c.execute(
        'INSERT INTO potluck (name, food_item, comments)'
        'VALUES("Tony Anania", "Chicken Cutlets", "Ok to eat hot or cold.")'
    )
