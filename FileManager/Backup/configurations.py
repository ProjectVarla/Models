# from typing import Optional

from pathlib import Path
from typing import Optional
from pydantic import BaseModel, validator


class RemoteBackup(BaseModel):
    host: str
    path: str

    @validator("path")
    def fix_path(cls, path):
        return path.replace("\\ ", " ").replace(" ", "\\ ")


class Configuration(BaseModel):
    PREFIX: str
    destination_dir: str
    zip_compression: bool
    keep_window: int

    source_directories: Optional[list[str]]
    remote_backups: Optional[list[RemoteBackup]]
    database_names: Optional[list[str]]

    @validator("source_directories")
    def fix_source_directories(cls, source_directories):
        return [
            path.replace("\\ ", " ").replace(" ", "\\ ") for path in source_directories
        ]

    @validator("destination_dir")
    def fix_destination_dir(cls, destination_dir):
        return destination_dir.replace("\\ ", " ").replace(" ", "\\ ")

    @validator("PREFIX")
    def fix_PREFIX(cls, PREFIX):
        return PREFIX.replace("\\ ", " ").replace(" ", "\\ ")
