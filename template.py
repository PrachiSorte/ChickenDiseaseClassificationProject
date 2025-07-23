import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "CNNClassifier"    # as generic template

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",  # to install your local project folder as a package
    f"src/{project_name}/components/__init__.py", #constructor file
    f"src/{project_name}/utils/__init__.py", #constructor file
    f"src/{project_name}/config/__init__.py", #constructor file  
    f"src/{project_name}/config/configuration.py",     
    f"src/{project_name}/pipeline/__init__.py", #constructor file
    f"src/{project_name}/constants/__init__.py", #constructor file
    f"src/{project_name}/entity/__init__.py", #constructor file
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
       
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Handling paths with pathlib ( / in Linux and \ in Windows)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # create directory if it does not exist
        logging.info(f"Created directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # create an empty file
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} File already exists: {filepath}")