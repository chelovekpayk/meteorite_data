#!venv/bin python
# coding=utf-8

import requests
import json
import sqlite3

class Meteorites():
    def __init__(self) -> None:
        self.source = 'https://data.nasa.gov/resource/gh4g-9sfh.json' #link to api
        self.data = requests.get(self.source).json() #request

    def save_json(self):
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

if __name__ == "__main__":
    r = Meteorites()
    r.save_json()

    db = sqlite3.connect('meteorite.db')
    cursor = db.cursor()
    db.execute('''CREATE TABLE IF NOT EXISTS Meteorites
    (id INTEGER UNIQUE, name TEXT, nametype TEXT, recclass TEXT, mass INTEGER, year TEXT, reclat RE
     subject TEXT, headers TEXT, body TEXT)''')