import os
from box.exceptions import BoxValueError
import yaml
import json
from mlproject import logger
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any




@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded Successfully.")
            return ConfigBox(content) 
    except BoxValueError:     # if file will be empty so the return  configbox will raise BoxValueError.
        raise ValueError("yaml file is empty.")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    
    # args : path = path of the File
    # return : size in KB

    size_in_kb = round(os.path.getsize(path)/1024)
    
    return f'~ {size_in_kb} KB'

