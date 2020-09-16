import logging
import unittest
from time import sleep

from common.desired_caps import appium_desired


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('======Open app======')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('======Close app======')
        sleep(3)
        self.driver.close_app()
