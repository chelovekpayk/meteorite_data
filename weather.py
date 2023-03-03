import os
import sqlite3
import requests
import traceback
import time

api_key = os.environ['METEO_API']

#database connection
con = sqlite3.connect('meteorites.db')
cur = con.cursor()

query =  '''SELECT Geodata.latitude, Geodata.longtitude FROM Geodata 
WHERE Geodata.latitude IS NOT NULL AND Geodata.latitude IS NOT 0.0 AND Geodata.longtitude IS NOT 0.0;''' #266 601

url = 'http://api.openweathermap.org/geo/1.0/reverse'

data = cur.execute(query)

r = requests.Session()

try:
    c = 0
    for i in data.fetchall():
        c += 1
        params = {'lat':i[0],
                'lon':i[1],
                'limit':1,
                'appid':api_key}
        print(c, params['lat'], params['lon'])
        
        request_to_api = r.get(url=url, params=params).json()
        try:
            data = request_to_api[0]
        except IndexError:
            continue

        cur.execute('''UPDATE Geodata
                    SET place = ?,
                        country = ?,
                        state = ?
                    WHERE latitude = ? AND longtitude = ?;''',(data.get('name'), data.get('country'), data.get('state'), i[0], i[1]))
        time.sleep(1.1)
except:
    traceback.print_exc()

finally:
    con.commit()
        