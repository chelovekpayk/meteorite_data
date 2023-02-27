#!.venv/bin python
# coding=utf-8

#https://www.coursera.org/learn/python-data-visualization/home/week/4

import requests
import json

class Meteorites():
    def __init__(self) -> None:
        self.source = 'https://data.nasa.gov/resource/gh4g-9sfh.json' #link to api
        self.data = requests.get(self.source).json() #request

    def save_json(self):
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

if __name__ == "__main__":
    #r = Meteorites().save_json()

    for i in Meteorites().data:
        print (i)