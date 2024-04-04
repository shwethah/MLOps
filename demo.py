from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    a = 1/"10"
    print(a)

except Exception as error:
    logging.info(error)
    raise USvisaException(error, sys) from error
