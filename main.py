#!.venv/bin python
# coding=utf-8

from app import Meteorites
from db import create_mt_table, create_geo_table

data = Meteorites().get_data()

create_mt_table(data)
create_geo_table(data)
