import unittest
from HTMLTestRunnerNew import HTMLTestRunner

from common.Common_fun import *


class run(Common_fun):
    report_dir = base_path + '/reports'
    test_dir = base_path + '/test_case'

    logging.info('======start run testcase======')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test_*')
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir + '/' + now + '_result.html'

    with open(report_name, 'wb') as file:
        runner = HTMLTestRunner(stream=file, title='360租房自动化测试报告', tester='甘宇')
        runner.run(discover)
    latest_report = Common_fun.latest_report
    Common_fun.send_mail(latest_report)
