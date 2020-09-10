# 初始化和封装一下基本方法
import logging
import os
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

base_path = os.path.dirname(os.path.dirname(__file__))


class Common(object):
    """
    封装公共方法
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        """
        找一个元素
        :param loc:元素地址
        :return:
        """
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """
        找一组元素
        :param loc:元素地址
        :return:
        """
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        """
        获取窗口大小
        :return:窗口长和宽
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_left(self):
        """
        向左滑
        :return:
        """
        logging.info("------swipe_left-------")
        l = self.get_window_size()
        x1 = int(l[0] * 0.1)
        x2 = int(l[0] * 0.9)
        y = int(l[1] * 0.5)
        return self.swipe(x2, y, x1, y)

    def swipe_right(self):
        """
        向右滑
        :return:
        """
        logging.info("------swipe_right-------")
        l = self.get_window_size()
        x1 = int(l[0] * 0.1)
        x2 = int(l[0] * 0.9)
        y = int(l[1] * 0.5)
        return self.swipe(x1, y, x2, y)

    def swipe_up(self):
        """
        向上滑
        :return:
        """
        logging.info("------swipe_up------")
        l = self.get_window_size()
        x = int(l[0] * 0.5)
        y1 = int(l[1] * 0.1)
        y2 = int(l[2] * 0.9)
        return self.swipe(x, y1, x, y2)

    def swipe_down(self):
        """
        向下滑
        :return:
        """
        logging.info("------swipe_down------")
        l = self.get_window_size()
        x = int(l[0] * 0.5)
        y1 = int(l[1] * 0.1)
        y2 = int(l[2] * 0.9)
        return self.swipe(x, y2, x, y1)

    def getTime(self):
        """
        获取当前时间
        """
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def get_Screen_Shot(self, module):
        """
        截图
        :param module:图片模式
        """
        time = self.getTime()
        image_file = base_path + '/screenshots/%s_%s.png' % (module, time)
        logging.info('====== get %s screenshot ======' % module)
        self.driver.get_screenshot_as_file(image_file)

    def click_element(self, *loc):
        """
        点击元素
        :param loc: 元素地址
        """
        self.driver.find_element(*loc).click()

    def type_element(self, *loc, text):
        """
        输入文本
        :param loc: 文本框地址
        :param text: 文本内容
        """
        self.driver.find_element(*loc).send_keys(text)

    def WebDriverWait(self, seconds, *loc):
        """
        元素显示等待
        :param seconds: 等待几秒
        :param loc: 元素地址
        """
        WebDriverWait(self.driver, seconds).until(lambda x: x.find_element(*loc))

    def isElementExist(self, *loc):
        """
        元素是否存在
        :param loc: 元素地址
        :return:
        """
        try:
            self.find_element(*loc)
        except NoSuchElementException as e:
            print('元素不存在')
            return False
        else:
            print('元素存在')
            return True








if __name__ == '__main__':
    print(base_path)
