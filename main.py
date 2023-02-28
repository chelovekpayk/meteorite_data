#!.venv/bin python
# coding=utf-8

#https://www.coursera.org/learn/python-data-visualization/home/week/4

import json
import requests


class Meteorites():
    ''' 
    Class for get data from NASA API. Init creates session obj and fill missing key values in dict.
    '''
    def __init__(self) -> None:
        self.source = 'https://data.nasa.gov/resource/gh4g-9sfh.json' #link to api
        self.data = requests.get(self.source, timeout=12).json() #request

        for record in self.data:
            if 'mass' not in record.keys():
                record.update({'mass':'na'})
            elif 'year' not in record.keys():
                record.update({'year':'na'})

    def save_json(self):
        """
        method to save result in a json-file
        """
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, allow_nan=True)

if __name__ == "__main__":
    Meteorites().save_json()
