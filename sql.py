q1 = '''SELECT Meteorites.name, Geodata.latitude, Geodata.longtitude 
FROM Meteorites INNER JOIN Geodata ON (Meteorites.id = Geodata.geo_id)'''

year1980 = '''SELECT Meteorites.id, Meteorites.year, Geodata.latitude, Geodata.longtitude FROM Meteorites INNER JOIN Geodata ON (Meteorites.id = Geodata.geo_id) 
WHERE Meteorites.year > 1980 and Geodata.latitude <> 0'''
