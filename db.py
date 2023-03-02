import sqlite3

def create_mt_table(data: dict):
    """
    Fuction creates table 'Meteorites' in sql meteorites.db and inserts data in table 
    """
    con = sqlite3.connect('meteorites.db')
    cur = con.cursor()

    #creating table
    cur.execute('''DROP TABLE IF EXISTS Meteorites''')
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
    
    #inserting data
    for record in data:
        cur.execute("""
                INSERT INTO Meteorites (name, nametype, recclass, mass, fall, year)
                VALUES (?, ?, ?, ?, ?, ?)""",
                (record.get('name'), record.get('nametype'),
                 record.get('recclass'), record.get('mass'),
                 record.get('fall'), record.get('year'))
                )
    con.commit()

def create_geo_table(data: dict):
    """
    Fuction creates table 'Geodata' in sql meteorites.db and inserts data in table
    """
    con = sqlite3.connect('meteorites.db')
    cur = con.cursor()

    cur.execute('''DROP TABLE IF EXISTS Geodata''')
    cur.execute(
        '''CREATE TABLE Geodata(
            geo_id INTEGER NOT NULL PRIMARY KEY, 
            latitude REAL, 
            longtitude REAL,
            place TEXT,
            country TEXT,
            state TEXT
            )'''
        )

    for record in data:
        geo = record.get('geolocation')
        cur.execute("""
                    INSERT INTO Geodata(latitude, longtitude)
                    VALUES (?, ?)""",
                    (geo['latitude'], geo['longitude'])
                    )
    con.commit()
