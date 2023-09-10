from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline
from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage_03_data_transformation import DataTransformationPipline

STAGE_NAME = "Data Ingestion Stage 1"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} Started. <<<<<<<<<<")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} Completed. <<<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage 2"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} Started. <<<<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} Completed. <<<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage 3"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} Started. <<<<<<<<<<")
    obj = DataTransformationPipline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} Completed. <<<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e