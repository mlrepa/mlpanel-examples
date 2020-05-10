import logging
import sys
import time
from typing import Text

loggers = {}


def get_logger(name: Text, loglevel: Text = 'INFO') -> None:
    """Set logger"""

    global loggers

    if loglevel not in logging._nameToLevel.keys():  # pylint: disable=protected-access
        loglevel = 'INFO'

    if loggers.get(name):
        return loggers.get(name)
    else:
        logger = logging.getLogger(name)
        logger.setLevel(loglevel)

        FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(FORMATTER)

        logger.setLevel(logging.DEBUG)  # better to have too much log than not enough
        logger.addHandler(console_handler)

        loggers[name] = logger

    return logger