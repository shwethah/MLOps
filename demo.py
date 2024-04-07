from us_visa.logger import logging
from us_visa.exception import USvisaException
from us_visa.constant import *
import sys

try:
    print("Database name: " + DATABASE_NAME)

except Exception as error:
    logging.info(error)
    raise USvisaException(error, sys) from error
