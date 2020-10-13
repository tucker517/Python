from extraction_w_config import Extract
import urllib
import pandas as pd
import numpy as np
from numpy.core.records import record

class Transformation:
    
    def __init__(self, dataSource, dataSet):
        
        # Creating Extract class object here, to fetch data using its generic methods for APIs and CSV data sources
        extractObj = Extract()
        
        if dataSource == 'api':
            self.data = extractObj.getAPIsData(dataSet)
            funcName = dataSource+dataSet
        
        elif dataSource == 'csv':
            self.data = extractObj.getCSVData(dataSet)

        else:
            print('Unkown Data Source!! Please try again...')
            
    # Weather station data transformation
    def apiNOAA(self):
        stations_colorado = {}
        for record in self.data['records']:
            stn_no={}
            
            
            # Taking out yearly GDP value from records
            stations_colorado['GDP_in_rs_cr'] = int(record['gross_domestic_product_in_rs_cr_at_2004_05_prices'])
            stations_colorado[record['financial_year']] = stn_no
            station_list_nos = list(stations_colorado)
            
        