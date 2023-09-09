import os
import pandas as pd
from mlproject import logger
from mlproject.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self,config: DataValidationConfig) -> None:
        self.config = config
        
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)
            all_schema = self.config.all_schema.keys()
            # os.makedirs()

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'Validation status of {col}: {validation_status}')
                    
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'Validation status of {col}: {validation_status}')
            return validation_status
        except Exception as e:
            raise e

            
            