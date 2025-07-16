import os
from us_visa.constants import *
from dataclasses import dataclass
from datetime import datetime
import yaml

# Load YAML configuration
with open("config/config_con.yaml", "r") as file:
    config = yaml.safe_load(file)


# TIMESTAMP: str = datetime.now().strftime("%m_%d_%H_%M")


@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = config['pipeline']['pipeline_name']
    artifact_dir: str = config['pipeline']['artifact_dir']
    # timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()



@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, config['data_ingestion']['data_ingestion_dir_name'])
    feature_store_file_path: str = os.path.join(data_ingestion_dir, config['data_ingestion']['data_ingestion_feature_store_dir'], config['files']['file_name'])
    training_file_path: str = os.path.join(data_ingestion_dir, config['data_ingestion']['data_ingestion_ingested_dir'], config['files']['train_file_name'])
    testing_file_path: str = os.path.join(data_ingestion_dir, config['data_ingestion']['data_ingestion_ingested_dir'], config['files']['test_file_name'])
    train_test_split_ratio: float = config['data_ingestion']['data_ingestion_train_test_split_ratio']
    collection_name:str = config['data_ingestion']['collection_name']




@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir, config['data_validation']['data_validation_dir_name'])
    drift_report_file_path: str = os.path.join(data_validation_dir, config['data_validation']['data_validation_drift_report_dir'],
                                               config['data_validation']['data_validation_drift_report_file_name'])
    



@dataclass
class DataTransformationConfig:
    data_transformation_dir: str = os.path.join(training_pipeline_config.artifact_dir, 
                                                config['data_transformation']['data_transformation_dir_name'])
    transformed_train_file_path: str = os.path.join(data_transformation_dir, 
                                                    config['data_transformation']['data_transformation_transformed_data_dir'],
                                                    config['files']['train_file_name'].replace("csv", "npy"))
    transformed_test_file_path: str = os.path.join(data_transformation_dir, 
                                                   config['data_transformation']['data_transformation_transformed_data_dir'],
                                                   config['files']['test_file_name'].replace("csv", "npy"))
    transformed_object_file_path: str = os.path.join(data_transformation_dir,
                                                     config['data_transformation']['data_transformation_transformed_object_dir'],
                                                     config['files']['preprocessing_object_file_name'])
    
