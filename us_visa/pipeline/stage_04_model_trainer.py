import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging

from us_visa.components.model_trainer import ModelTrainer

from us_visa.entity.config_entity import (DataTransformationConfig,
                                            ModelTrainerConfig)


from us_visa.entity.artifact_entity import (DataTransformationArtifact,
                                            ModelTrainerArtifact,
                                            ClassificationMetricArtifact)


STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
                
        self.data_transformation_config = DataTransformationConfig()
        self.data_transformation_artifact = DataTransformationArtifact(
            self.data_transformation_config.transformed_object_file_path,
            self.data_transformation_config.transformed_train_file_path,
            self.data_transformation_config.transformed_test_file_path
        )
        
        self.model_trainer_config = ModelTrainerConfig()
        self.model_training_artifact = ModelTrainerArtifact(
            trained_model_file_path=self.model_trainer_config.trained_model_file_path,
            metric_artifact=ClassificationMetricArtifact(
                    precision_score=0.0,
                    recall_score=0.0,
                    f1_score=0.0
                )
                )
        

    
    def main(self) -> ModelTrainerArtifact:
        """
        This method of TrainPipeline class is responsible for starting data transformation component
        """
        try:
            model_trainer = ModelTrainer(
                data_transformation_artifact=self.data_transformation_artifact,
                model_trainer_config=self.model_trainer_config
            )
            
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            
            return model_trainer_artifact
        
        except Exception as e:
            raise USvisaException(e, sys)
        

# if __name__ == '__main__':
#     try:
#         logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = ModelTrainingPipeline()  # ✅ Correct class
#         obj.main()
#         logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logging.exception(e)
#         raise e
