import logging
import unittest
from common.myunit import StartEnd
from pages.add_page import add_page
from pages.bill_page import bill_page
from pages.bonus_page import bonus_page
from pages.house_page import house_page
from pages.main_page import main_page
from pages.tenant_page import tenant_page


class Test_MainPage(StartEnd, main_page, bill_page, bonus_page, house_page, tenant_page, add_page):

    @unittest.skip('test_hint_income')
    def test_hint_income(self):
        logging.info('======test hint income======')
        po = main_page(self.driver)
        po.hint_income()
        account_hint = self.get_text(*self.account_loc)
        self.assertEqual(account_hint, '****')

    @unittest.skip('test_hint_income')
    def test_income_help(self):
        logging.info('======test income help======')
        po = main_page(self.driver)
        po.click_income_help()
        income_help_content = self.get_text(*self.income_help_content_loc)
        self.assertEqual(income_help_content, '统计一个自然年（12个月）内，由租房产生的收益减去支出的总和')

    @unittest.skip('test_hint_income')
    def test_enter_my_bill(self):
        logging.info('======test enter my bill======')
        po = main_page(self.driver)
        po.click_my_bill()
        self.assertEqual(self.get_text(*self.bill_title_loc), '账单统计')

    @unittest.skip('test_hint_income')
    def test_enter_my_bonus(self):
        logging.info('======test enter my bonus======')
        po = main_page(self.driver)
        po.click_my_bonus()
        self.assertTrue(po.isElementExist(*self.my_bonus_help_loc))

    @unittest.skip('test_hint_income')
    def test_enter_my_house(self):
        logging.info('======test enter my house======')
        po = main_page(self.driver)
        po.click_my_house()
        self.assertEqual(self.get_text(*self.my_house_title_loc), '我的房屋')

    @unittest.skip('test_hint_income')
    def test_enter_my_tenant(self):
        logging.info('======test enter my tenant======')
        po = main_page(self.driver)
        po.click_my_tenant()
        self.assertEqual(self.get_text(*self.my_tenant_title_loc), '我的租客')

    # @unittest.skip('test_hint_income')
    def test_enter_my_add(self):
        logging.info('======test enter my add======')
        po = main_page(self.driver)
        po.click_add()
        self.assertEqual(self.get_text(*self.lock_buy_now_loc), '立即购买')