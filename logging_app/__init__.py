import json
import logging.config
import os
from typing import NoReturn


def setup_logging(
        default_path='resources/logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG') -> NoReturn:
    """
    Configure logging capabilities
    :param default_path: path to search for the logging configuration
    :param default_level: default level to log
    :param env_key: if using environment variable instead of default_path
    :return: it doesn't return a value
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level,
                            format="%(asctime)s - %(name)-15s - %(funcName)-15s - %(levelname)-8s - %(message)-10s")
