import sqlite3
import time
import requests
class Database():
    """
    Create object for pulling data to database
    dict: dictionary
    """
    def __init__(self, data:dict):

        #creating connection to sql database
        self.con = sqlite3.connect('meteorites.db')
        self.cur = self.con.cursor()

        #dict to pull data
        self.data = data

    def create_mt_table(self):
        """
        Method creates table 'Meteorites' in sql meteorites.db and inserts data in table 
        """

        #creating table
        self.cur.execute('''DROP TABLE IF EXISTS Meteorites''')
        self.cur.execute('''
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

        #inserting data
        for record in self.data:
            self.cur.execute("""
                    INSERT INTO Meteorites (name, nametype, recclass, mass, fall, year)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    (record.get('name'), record.get('nametype'),
                    record.get('recclass'), record.get('mass'),
                    record.get('fall'), record.get('year'))
                    )
        self.con.commit()

    def create_geo_table(self):
        """
        Method creates table 'Geodata' in sql meteorites.db and inserts data in table
        """

        self.cur.execute('''DROP TABLE IF EXISTS Geodata''')
        self.cur.execute(
            '''CREATE TABLE Geodata(
                geo_id INTEGER NOT NULL PRIMARY KEY, 
                latitude REAL, 
                longtitude REAL,
                place TEXT,
                country TEXT,
                state TEXT
                )'''
            )

        #insert data in table
        for record in self.data:
            geo = record.get('geolocation')
            self.cur.execute("""
                        INSERT INTO Geodata(latitude, longtitude)
                        VALUES (?, ?)""",
                        (geo['latitude'], geo['longitude'])
                        )
        self.con.commit()

    def get_geodata_api(self, api_key:str):
        """
        Method for connecting to OpenWeatherMap
        Connects names for geoplaces from Recursive geodata API
        api_key: str api key for OWM
        """
        query =  '''SELECT Geodata.latitude, Geodata.longtitude FROM Geodata
        WHERE Geodata.latitude IS NOT NULL AND Geodata.latitude IS NOT 0.0 AND Geodata.longtitude IS NOT 0.0;'''
        data = self.cur.execute(query)

        url = 'http://api.openweathermap.org/geo/1.0/reverse'
        r = requests.Session()

        for i in data.fetchall():
            params = {'lat':i[0],
                    'lon':i[1],
                    'limit':1,
                    'appid':api_key}

            request_to_api = r.get(url=url, params=params).json()
            try:
                data = request_to_api[0]
            except IndexError:
                continue

            self.cur.execute('''UPDATE Geodata
                        SET place = ?,
                            country = ?,
                            state = ?
                        WHERE latitude = ? AND longtitude = ?;''',(data.get('name'), data.get('country'), data.get('state'), i[0], i[1]))
            time.sleep(1.1)

        self.con.commit()
