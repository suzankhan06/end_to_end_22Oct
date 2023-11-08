import logging
import os
from datetime import datetime

#creating log file format
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#creating log path
log_path=os.path.join(os.getcwd(), "logs")

#creating directory for our log file
os.makedirs(log_path, exist_ok=True)

#joing our log_file and log_path in our directory

LOG_FILEPATH=os.path.join(log_path, LOG_FILE)

#creating logging configuration

logging.basicConfig(level=logging.INFO, 
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    
)



