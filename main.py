#!.venv/bin python
# coding=utf-8
import os
import subprocess

from app import Meteorites
from db import Database

#Скрипт для проверки АПИ ключей
if os.path.isfile('secrets.sh'):
    subprocess.call("sleep.sh", shell=True)
    
    meteo_api = os.environ["METEO_API"]
    nasa_api = os.environ["NASA_API"]

    # You can insert your API key here

    data = Meteorites().get_data(nasa_api)
    db = Database(data)

    # Creating databases
    db.create_mt_table()
    db.create_geo_table()

    # Requesting to OWM API
    db.get_geodata_api(meteo_api)
    
else: print('I need API keys')
