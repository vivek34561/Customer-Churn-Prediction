import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO)

project_name = "Churn_Prediction"

list_of_files = [
   
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluator.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipelines.py",
    f"src/{project_name}/pipelines/prediction_pipelines.py",
    f"src/{project_name}/configs/__init__.py",
    f"src/{project_name}/configs/config.yaml",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/tests/__init__.py",
    f"src/{project_name}/tests/test_data_ingestion.py",
    f"src/{project_name}/tests/test_transformation.py",
    f"src/{project_name}/tests/test_model.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir , exist_ok = True)
        logging.info(f"Creating diretory:{filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath , 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
            
            
    else:
        logging.info(f"{filename} is already exists")        