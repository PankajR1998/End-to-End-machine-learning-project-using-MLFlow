from mlproject.entity.config_entity import DataTransformationConfig
from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_tranfomation import DataTransformation
from mlproject import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_tranformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()


if __name__=='__main__':

    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} Started. <<<<<<<<<<")
        obj = DataTransformationPipline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} Completed. <<<<<<<<<<")
        
    except Exception as e:
        logger.exception(e)
        raise e