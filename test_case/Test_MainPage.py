from common.myunit import StartEnd
from pages.bill_page import bill_page
from pages.bonus_page import bonus_page
from pages.main_page import main_page


class Test_MainPage(StartEnd, main_page, bill_page, bonus_page):

    def test_hint_income(self):
        po = main_page(self.driver)
        po.hint_income()
        account_hint = self.get_text(*self.account_loc)
        self.assertEqual(account_hint, '****')

    def test_income_help(self):
        po = main_page(self.driver)
        po.click_income_help()
        income_help_content = self.get_text(*self.income_help_content_loc)
        self.assertEqual(income_help_content, '统计一个自然年（12个月）内，由租房产生的收益减去支出的总和')

    def test_enter_my_bill(self):
        po = main_page(self.driver)
        po.click_my_bill()
        self.assertEqual(self.get_text(*self.bill_title_loc), '账单统计')

    def test_enter_my_bonus(self):
        po = main_page(self.driver)
        po.click_my_bonus()
        self.assertTrue(po.isElementExist(*self.my_bonus_help_loc))

