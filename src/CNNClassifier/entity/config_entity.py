from dataclasses import dataclass
from pathlib import Path

#Defining entity or configuration class
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path             # All these values are taken from the config.yaml file
    source_url: str
    local_data_file: Path
    unzip_dir: Path