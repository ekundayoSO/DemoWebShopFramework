import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:

    @staticmethod
    def getLogger():
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def find_element(self, *locator):
        return self.driver.find_element(*locator)


