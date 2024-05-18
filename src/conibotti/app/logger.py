from enum import Enum, IntEnum
from logging import INFO, CRITICAL, DEBUG, ERROR, NOTSET, WARNING
from logging import addLevelName
from logging.config import dictConfig
from pathlib import Path
from yaml import load, Loader

from app.app_types import LogConfig


class LogLevel(IntEnum, Enum):
    NULL = NOTSET
    WARN = WARNING
    FATAL = CRITICAL
    EMERG = CRITICAL

    NOTSET = NOTSET
    DEBUG = DEBUG
    INFO = INFO
    WARNING = WARNING
    ERROR = ERROR
    CRITICAL = CRITICAL

    ALL = 999


def setup_logger(config_file: str = "config/logging.yml"):
    config = __read_config(config_file)
    dictConfig(config)
    addLevelName(LogLevel.ALL, LogLevel.ALL.name)


def __read_config(config_file: str):
    with Path(config_file).open("rb") as f:
        config: LogConfig = load(f, Loader=Loader)

        return config
