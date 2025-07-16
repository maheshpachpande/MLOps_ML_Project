import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion
from us_visa.components.data_validation import DataValidation
from us_visa.components.data_transformation import DataTransformation

from us_visa.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig,
                                            DataTransformationConfig)


from us_visa.entity.artifact_entity import (DataIngestionArtifact,
                                            DataValidationArtifact,
                                            DataTransformationArtifact)


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainPipeline:
    def __init__(self):
        self.data_ingestion_cfg = DataIngestionConfig()        
        self.data_ingestion_artifact = DataIngestionArtifact(self.data_ingestion_cfg.training_file_path,
                                                             self.data_ingestion_cfg.testing_file_path)
        
        self.data_validation_config = DataValidationConfig()
        self.data_validation_artifact = DataValidationArtifact(
            self.data_validation_config.data_validation_dir,
            self.data_validation_config.drift_report_file_path,
            message="Data validation completed successfully"
        )
        
        self.data_transformation_config = DataTransformationConfig()
        self.data_transformation_artifact = DataTransformationArtifact(
            self.data_transformation_config.transformed_object_file_path,
            self.data_transformation_config.transformed_train_file_path,
            self.data_transformation_config.transformed_test_file_path
        )
       
        

    
    def main(self) -> DataTransformationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data transformation component
        """
        try:
            data_transformation = DataTransformation(data_ingestion_artifact=self.data_ingestion_artifact,
                                                     data_transformation_config=self.data_transformation_config,
                                                     data_validation_artifact=self.data_validation_artifact)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise USvisaException(e, sys)
        

# if __name__ == '__main__':
    # try:
    #     logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    #     obj = DataTransformationTrainPipeline()
    #     obj.main()
    #     logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    # except Exception as e:
    #     logging.exception(e)
    #     raise e