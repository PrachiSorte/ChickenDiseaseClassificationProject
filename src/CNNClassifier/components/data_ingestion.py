import os
import urllib.request as request
from zipfile import ZipFile
from CNNClassifier.utils.common import get_size
from CNNClassifier import logger
from CNNClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path

# Creating component for data ingestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading file from: {self.config.source_url} to {self.config.local_data_file}")
            filename, headers=request.urlretrieve(url=self.config.source_url, filename=self.config.local_data_file)
            logger.info(f"{filename} - File downloaded successfullywith following info :\n{headers}" )
        else:
            logger.info(f"File already exists of size: {get_size(Path( self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str    The path to the zip file to be extracted.
        Extracts the zip file to the specified directory.
        Function returns None.
        """
        if not os.path.exists(self.config.unzip_dir):
            os.makedirs(self.config.unzip_dir)
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"Extracted files to: {self.config.unzip_dir}")

    def initiate_data_ingestion(self):
        self.download_file()
        self.extract_zip_file()