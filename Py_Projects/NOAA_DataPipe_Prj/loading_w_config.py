from pyodbc import connect as con
import pandas as pd


class MS_SQLConn():
    # Initialize the common usable variables in below function:
    def __init__(self, username, password, host, db_name, port):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.uri = 'DRIVER={ODBC Driver 17 for SQL Server};'+';SERVER='+ self.host+';DATABASE='+self.db_name+';UID='+self.username+';PWD='+self.password
        
        try:
            self.client = con(self.uri)
            self.db = self.client[self.db_name]
            print ("MS SQL Server Connection Successful.")
        except Exception as e:
            print("Connection unsuccessful... Please try again...")
            print(e)
            
# Function to insert data in DB, could handle Python dictionary and Pandas data-frames
def insert_into_db(self, data, collection):
    if isinstance(data, pd.DataFrame):
        try:
            self.db[collection]._insert_many(data.to_dict('records'))
            print('Data Inserted Successfully')
        
        except Exception as e:
            print('OOPS!!! An error occurred while inserting the data into the database...')
            print(e)
            
def read_from_db(self, collection):
    try:
        data = pd.DataFrame(list(self.db[collection].find()))  
        print('Data Fetched Successfully')
        return data
    except Exception as e:
        print("OOPS!! An error occurred while retreiving the data from the api")
        print(e)     
