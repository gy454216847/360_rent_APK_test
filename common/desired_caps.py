import logging
import logging.config
import yaml
from appium import webdriver

from common.Common_fun import base_path

log_config_path = base_path + '/config/log.conf'
caps_yaml_path = base_path + '/config/360_rent_APK_caps.yaml'
logging.config.fileConfig(log_config_path)
logging = logging.getLogger()

def appium_desired():
    """
    启动app
    :return: driver
    """
    with open(caps_yaml_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('======start app======')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    appium_desired()
