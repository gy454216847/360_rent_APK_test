import unittest
from HTMLTestRunnerNew import HTMLTestRunner

from common.Common_fun import *


class run(Common_fun):
    report_dir = base_path + '/reports'
    test_dir = base_path + '/test_case'
    report_yaml_dir = base_path + '/config/test_report.yaml'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test_*')
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir + '/' + now + '_result.html'

    with open(report_yaml_dir, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    with open(report_name, 'wb') as file:
        runner = HTMLTestRunner(stream=file, title=data['title'], tester=data['tester'])
        logging.info('======start run testcase======')
        runner.run(discover)

    latest_report = Common_fun.latest_report(report_dir)
    logging.info('======send email======')
    Common_fun.send_mail(latest_report)
