from src.project4.logger import logging
from src.project4.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info('The execution has started')
    
    try:
       10/0
    except Exception as e:
        logging.info('Custom Exception')
        raise CustomException(e,sys)