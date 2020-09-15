# 初始化和封装一下基本方法
import logging
import os
import smtplib
import time
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import yaml
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

base_path = os.path.dirname(os.path.dirname(__file__))


class Common_fun(object):
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
        return self.swipe(x2, y, x1, y, 1000)

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
        return self.swipe(x1, y, x2, y, 1000)

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
        return self.swipe(x, y1, x, y2, 1000)

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
        return self.swipe(x, y2, x, y1, 1000)

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

        return self.driver.find_element(*loc).click()

    def type_element(self, *loc, text):
        """
        输入文本
        :param loc: 文本框地址
        :param text: 文本内容
        """
        return self.driver.find_element(*loc).send_keys(text)

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

    def get_text(self, *loc):
        element_text = self.driver.find_element(*loc).text
        return element_text

    def get_csv_data(self, csv_file, line):
        logging.info('=====get_csv_data======')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


    def latest_report(report_dir):
        lists = os.listdir(report_dir)
        print(lists)
        lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
        print(lists[-1])
        file = os.path.join(report_dir, lists[-1])
        return file

    def send_mail(latest_report):
        f = open(latest_report, 'rb')
        mail_content = f.read()
        f.close()
        yamlfile = base_path + '/config/' + 'email.yaml'
        file = open(yamlfile, encoding='utf-8')
        data = yaml.load(file, Loader=yaml.FullLoader)

        smtpserver = data['smtpserver']

        user = data['user']
        password = data['password']

        sender = data['sender']
        receives = data['receives']

        subject = data['subject']

        msg = MIMEMultipart()
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = receives
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        text_msg = MIMEText('查看自动化测试请下载附件', 'plain', 'utf-8')
        msg.attach(text_msg)
        file_msg = MIMEApplication(mail_content)
        file_msg.add_header('content-disposition', 'attchment', filename='自动化测试报告.html')

        msg.attach(file_msg)

        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.helo(smtpserver)
        smtp.ehlo(smtpserver)
        smtp.login(user, password)

        print("Start send email....")
        smtp.sendmail(sender, receives, msg.as_string())
        smtp.quit()
        print("Send email end")
