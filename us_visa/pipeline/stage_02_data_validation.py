import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion
from us_visa.components.data_validation import DataValidation

from us_visa.entity.config_entity import (DataIngestionConfig,
                                            DataValidationConfig)


from us_visa.entity.artifact_entity import (DataIngestionArtifact,
                                            DataValidationArtifact)


STAGE_NAME = "Data Validation stage"

class DataValidationTrainPipeline:
    def __init__(self):
        self.data_ingestion_cfg = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.data_ingestion_artifact = DataIngestionArtifact(self.data_ingestion_cfg.training_file_path,
                                                             self.data_ingestion_cfg.testing_file_path)
        
        

    # def main(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
    def main(self) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is responsible for starting data validation component
        """
        
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(data_ingestion_artifact=self.data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config
                                             )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")

            
            return data_validation_artifact

        except Exception as e:
            raise USvisaException(e, sys) from e
        
        
# if __name__ == '__main__':
#     try:
#         logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = DataValidationTrainPipeline()
#         obj.main()
#         logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logging.exception(e)
#         raise e