q1 = '''
--sql
SELECT Meteorites.name, Geodata.latitude, Geodata.longtitude 
FROM Meteorites INNER JOIN Geodata ON (Meteorites.id = Geodata.geo_id)'''

year1980 = '''
--sql
SELECT Meteorites.id, Meteorites.year, Geodata.latitude, Geodata.longtitude FROM Meteorites INNER JOIN Geodata ON (Meteorites.id = Geodata.geo_id) 
WHERE Meteorites.year > 1980 and Geodata.latitude <> 0'''

query  = """
--sql
SELECT Meteorites.name, Meteorites.nametype, Meteorites.recclass, Meteorites.mass, Meteorites.year, Geodata.place, Geodata.country, Geodata.state FROM Meteorites INNER JOIN Geodata ON (Meteorites.id = Geodata.geo_id)
WHERE Geodata.place IS NOT NULL
;
"""
