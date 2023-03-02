import os
import sqlite3
import requests
import traceback

api_key = os.environ['METEO_API']

#database connection
con = sqlite3.connect('meteorites.db')
cur = con.cursor()

query =  '''SELECT Geodata.latitude, Geodata.longtitude FROM Geodata 
WHERE Geodata.latitude is not NULL AND (Geodata.latitude IS NOT 0.0 OR Geodata.longtitude IS NOT 0.0)
LIMIT 60;'''

url = 'http://api.openweathermap.org/geo/1.0/reverse'

data = cur.execute(query)

r = requests.Session()

try:
    c = 0
    for i in data.fetchall():
        c += 1
        print(c)
        params = {'lat':i[0],
                'lon':i[1],
                'limit':1,
                'appid':api_key}
        
        request_to_api = r.get(url=url, params=params).json()

        data = request_to_api[0]

        cur.execute('''UPDATE Geodata
                    SET place = ?,
                        country = ?,
                        state = ?
                    WHERE latitude = ?;''',(data.get('name'), data.get('country'), data.get('state'), i[0]))
except:
    traceback.print_exc()

finally:
    con.commit()
        