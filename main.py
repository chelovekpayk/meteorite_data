#!.venv/bin python
# coding=utf-8
import os

from app import Meteorites
from db import Database

# You can insert your API key here
meteo_api = os.environ["METEO_API"]
nasa_api = os.environ["NASA_API"]

data = Meteorites().get_data(nasa_api)
db = Database(data)

# Creating databases
db.create_mt_table()
db.create_geo_table()

# Requesting to OWM API
db.get_geodata_api(meteo_api)