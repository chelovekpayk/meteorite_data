#!.venv/bin python

import sqlite3
from main import Meteorites

con = sqlite3.connect('meteorites.db')
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS Meteorites''')
cur.execute('''DROP TABLE IF EXISTS Geodata''')

cur.execute('''
    CREATE TABLE Meteorites (
        id INTEGER NOT NULL PRIMARY KEY, 
        name TEXT, 
        nametype TEXT, 
        recclass TEXT, 
        mass REAL,
        fall TEXT,
        year INTEGER
        )'''
    )

cur.execute(
    '''CREATE TABLE Geodata(
        geo_id INTEGER NOT NULL PRIMARY KEY, 
        latitude REAL, 
        longtitude REAL
        )'''
    )


data = Meteorites().data

for item in data:
    cur.execute("""
                INSERT INTO Meteorites (name, nametype, recclass, mass, fall, year)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (item['name'], item['nametype'],
                 item['recclass'], item['mass'],
                 item['fall'], item['year'])
                )
con.commit()
