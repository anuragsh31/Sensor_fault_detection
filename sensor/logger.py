import logging
import os
from datetime import datetime

from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   #current time stamp

logs_path = os.path.join(from_root(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  #it is format og logging from python documentation.
    #timestamp, lineno, name-root, levelname-info 
    level=logging.INFO,
)