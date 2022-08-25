import logging
import os
import coloredlogs
import warnings
from urllib3.exceptions import InsecureRequestWarning

def get_logger(class_name: str):
    log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()
    log = logging.getLogger(class_name)
    warnings.simplefilter('ignore', InsecureRequestWarning)
    coloredlogs.install(isatty=True, fmt="%(asctime)s %(name)s %(levelname)s %(message)s", level=log_level)
    return log