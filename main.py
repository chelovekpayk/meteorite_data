#!.venv/bin python
# coding=utf-8

from app import Meteorites
import os
from db import Database

data = Meteorites().get_data()

db = Database(data)

db.create_mt_table()
db.create_geo_table()

api_key = os.environ['METEO_API']

db.get_geodata_api(api_key)
