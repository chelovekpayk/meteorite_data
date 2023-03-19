#!.venv/bin python
# coding=utf-8
import os

from app import Meteorites
from db import Database

data = Meteorites().get_data()
db = Database(data)

#Creating databases
db.create_mt_table()
db.create_geo_table()

#You can insert your API key here
api_key = os.environ['METEO_API']

#Requesting to OWM API
db.get_geodata_api(api_key)
