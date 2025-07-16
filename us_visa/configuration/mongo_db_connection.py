import os
import sys
import pymongo
import certifi

from us_visa.exception import USvisaException
from us_visa.logger import logging

from dotenv import load_dotenv
from us_visa.constants import *
import yaml

# Example: Load from file
with open("config/config_con.yaml", "r") as file:
    config = yaml.safe_load(file)

ca = certifi.where()
load_dotenv()



class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=config['database']['database_name']) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv('URL')
                if mongo_db_url is None:
                    raise Exception(f"Environment key is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise USvisaException(e,sys)