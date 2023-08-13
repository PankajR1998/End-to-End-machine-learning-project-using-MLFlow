from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipline

STAGE_NAME = "Data Ingestion Stage 1"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} Started. <<<<<<<<<<")
    obj = DataIngestionTrainingPipline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} Completed. <<<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e