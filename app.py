import json
import requests


class Meteorites():
    ''' 
    Class for get data from NASA API
    '''
    def __init__(self) -> None:
        self.source = None
        self.data = None


    def get_data(self) -> dict:
        '''
        method gets data from Nasa Api and returns data to store or work
        '''
        self.source = 'https://data.nasa.gov/resource/gh4g-9sfh.json' #link to api
        self.data = requests.get(self.source, timeout=12).json() #request


        for record in self.data:
            if record.get('year') is not None:
                record.update({'year':record['year'][:4]})
        for record in self.data:
            if record.get('geolocation') is None:
                record.update({'geolocation':{'latitude':None, 'longitude':None}})

        return self.data
                
    def save_json(self):
        """
        method to save result in a json-file for testing
        """
        self.data = self.get_data()
        
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, allow_nan=True)

if __name__ == "__main__":
    Meteorites().save_json()
