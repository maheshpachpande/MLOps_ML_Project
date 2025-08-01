# import os
# from datetime import date

# DATABASE_NAME = "us_visa"

# COLLECTION_NAME = "visa_data"

# MONGODB_URL_KEY = "URL"

# PIPELINE_NAME: str = "usvisa"
# ARTIFACT_DIR: str = "artifact"


# TRAIN_FILE_NAME: str = "train.csv"
# TEST_FILE_NAME: str = "test.csv"

# FILE_NAME: str = "usvisa.csv"
# MODEL_FILE_NAME = "model.pkl"


# TARGET_COLUMN = "case_status"
# CURRENT_YEAR = date.today().year
# PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"
# SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")


# """
# Data Ingestion related constant start with DATA_INGESTION VAR NAME
# """
# DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
# DATA_INGESTION_DIR_NAME: str = "data_ingestion"
# DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
# DATA_INGESTION_INGESTED_DIR: str = "ingested"
# DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25


from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("config/params.yaml")
SCHEMA_FILE_PATH = Path("config/schema.yaml")