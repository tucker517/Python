import pandas as pd
import json
import requests


class Extract():
    # Method to load the json configuration file created for API, CSV, and other process info.
    def __init__ (self):
        self.data_sources = json.load(open('data_config.json'))
        self.api = self.data_sources['data_sources']['api']
        self.csv_path = self.data_sources['data_sources']['csv']
   
    # Method to take args for request and define api's to use from config file    
    def getAPIsData(self, api_name):
        api_url = self.api[api_name]
        response = requests.get(api_url)
    # Create a json format file of the request response variable
        return response.json()
    
    def getCSVsData(self, csv_name):
    # Use the config file to load csv's and create a pandas dataframe from the file
        df = pd.read_csv(self.csv_path[csv_name])
        return df
        
        
        
        
        
        
        
        