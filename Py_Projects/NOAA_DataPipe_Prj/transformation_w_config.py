from extraction_w_config import Extract
import urllib
from loading_w_config import MongoDB

class Transformation:
    
    def __init__(self, dataSource, dataSet):
        
        # Creating Extract class object here, to fetch data using its generic methods for APIs and CSV data sources
        extractObj = Extract()
        
        if dataSource == 'api':
            self.data = extractObj.getAPIsData(dataSet)
            funcName = dataSource+dataSet
        
            # getattr function takes in the function name of a class and calls it.
            getattr(self,funcName)()
        
        elif dataSource == 'csv':
            self.data = extractObj.getCSVData(dataSet)
            funcName = dataSource + dataSet
            getattr(self,funcName)()

        else:
            print('Unknown Data Source!! Please try again...')
            
    # Weather station data transformation
    def apiNOAA(self):
        weather_stations = {}
        for result in self.data['results']:  
            # Taking out station names, lat, and long
            weather_stations['Station_Name'] = str(result['name'])
            weather_stations['Latitude'] = int(result['latitude'])
            weather_stations['Longitude'] = int(result['longitude'])
            
        # connection to mongo db
        mongodb_obj = MongoDB(urllib.parse.quote_plus('<**username**>'), urllib.parse.quote_plus('<**password**>'), '<**host**>', '<**db_name**>')
        # Insert Data into MongoDB
        mongodb_obj.insert_into_db(weather_stations, 'Weather_Stations')
    
        
if __name__ == '__main__':
    dataSource = input("Please Select the DataSource i.e 'API'/'CSV'/'Database': ").lower()
    print(dataSource)
    dataSet = input('Please select the Data set for Transformation: ').title()
    print(dataSet)
    trans_obj = Transformation(dataSource, dataSet)
