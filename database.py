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
        year INTEGER,
        FOREIGN KEY (id) 
        REFERENCES Geodata(geo_id)
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

def insert_meteorite_data():
    """
    Function for insert data in table meteorites
    """
    for record in data:
        cur.execute("""
                INSERT INTO Meteorites (name, nametype, recclass, mass, fall, year)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (record.get('name'), record.get('nametype'),
                 record.get('recclass'), record.get('mass'),
                 record.get('fall'), record.get('year'))
                )
    con.commit()

def insert_geo_data():
    """
    Func for insert data to Geodata table
    """
    for record in data:
        geo = record.get('geolocation')
        cur.execute("""
                INSERT INTO Geodata(latitude, longtitude)
                VALUES (?, ?)""",
                (geo['latitude'], geo['longitude'])
        )
    con.commit()

insert_meteorite_data()
insert_geo_data()
