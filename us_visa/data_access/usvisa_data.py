from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import *
from us_visa.exception import USvisaException
import pandas as pd
import numpy as np
import yaml
import sys
from typing import Optional

# Load YAML configuration
with open("config/config_con.yaml", "r") as file:
    config = yaml.safe_load(file)

class USvisaData:
    """
    This class helps to export the entire MongoDB collection as a pandas DataFrame.
    """

    def __init__(self):
        """
        Initialize MongoDB client using database name from the YAML config.
        """
        try:
            db_name = config['database']['database_name']
            self.mongo_client = MongoDBClient(database_name=db_name).client
        except Exception as e:
            raise USvisaException(e, sys)

    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Export the entire collection as a DataFrame.

        Args:
            collection_name (str): MongoDB collection name.
            database_name (Optional[str]): Optional override for database name.

        Returns:
            pd.DataFrame: DataFrame containing all documents from the collection.
        """
        try:
            db = self.mongo_client[database_name] if database_name else self.mongo_client[config['database']['database_name']]
            collection = db[collection_name]
            
            df = pd.DataFrame(list(collection.find()))
            
            # Drop MongoDB's default _id column if present
            if "_id" in df.columns:
                df.drop(columns=["_id"], inplace=True)
            
            # Replace 'na' string with np.nan
            df.replace({"na": np.nan}, inplace=True)
            
            return df

        except Exception as e:
            raise USvisaException(e, sys)


# if __name__ == "__main__":
#     data_exporter = USvisaData()
#     df = data_exporter.export_collection_as_dataframe("visa_data")
#     print(df.head())
