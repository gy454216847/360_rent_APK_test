import logging
import unittest
from time import sleep

from common.desired_caps import appium_desired


class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('======打开app======')
        self.driver = appium_desired()

    def tearDown(self):
        logging.info('======关闭app======')
        sleep(3)
        self.driver.close_app()
