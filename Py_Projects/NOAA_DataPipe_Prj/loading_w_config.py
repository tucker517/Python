from pymongo import MongoClient
import pandas as pd


class MongoDB:
    # Initialize the common usable variables in below function:
    def __init__(self, username, password, host, db_name, port='27017', authSource='admin'):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.authSource = authSource
        self.uri = 'mongodb://' + self.username + ':' + self.password + '@'+ self.host + ':'+ self.port + '/' + self.db_name + '?authSource=' + self.authSource
    
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print ("MongoDB Connection Successful!")
        except Exception as e:
            print("Connection unsuccessful... Please try again...")
            print(e)
            
    # Function to insert data in DB, could handle Python dictionary and Pandas data-frames
    def insert_into_db(self, data, collection):
        if isinstance(data, pd.DataFrame):
            try:
                self.db[collection].insert_many(data.to_dict('results'))
                print('Data Inserted Successfully')
            
            except Exception as e:
                print('OOPS!!! An error occurred while inserting the data into the database...')
                print(e)
            
            else:
                try:
                    self.db[collection].insert_many(data)
                    print('Data Inserted Successfully!')
                except Exception as e:
                    print("OOPS! An error occurred inserting the data...") 
                    print(e)
                    
    def read_from_db(self, collection):
        try:
            data = pd.DataFrame(list(self.db[collection].find()))  
            print('Data Fetched Successfully')
            return data
        except Exception as e:
            print("OOPS!! An error occurred while reading data from the database...")
            print(e)     
