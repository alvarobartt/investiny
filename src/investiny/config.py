import os

from pydantic.dataclasses import dataclass


@dataclass
class Config:
    date_format: str = os.getenv("INVESTINY_DATE_FORMAT", "%m/%d/%Y")
    time_format: str = os.getenv("INVESTINY_TIME_FORMAT", "%m/%d/%Y %H:%M")
