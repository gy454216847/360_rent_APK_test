from selenium.webdriver.common.by import By

from common.Common_fun import Common_fun


class main_page(Common_fun):
    login_register_btn_loc = (By.ID, 'com.lansent.renting:id/main_home_top_user_name_tv')
    eye_btn_loc = (By.ID, 'com.lansent.renting:id/main_home_income_eye_iv')
    my_bill_btn_loc = (By.ID, 'main_home_my_bill_tv')
    my_bonus_btn_loc = (By.ID, 'main_home_dividends_text_tv')
    my_house_btn_loc = (By.ID, 'main_home_my_house_iv')
    my_tenant_btn_loc = (By.ID, 'main_home_my_tenant_iv')
    income_help_btn_loc = (By.ID, 'main_home_income_help_iv')
    income_help_content_loc = (By.ID, 'com.lansent.renting:id/dialog_content_tv')
    account_loc = (By.ID, 'com.lansent.renting:id/main_home_total_income_tv')
    top_add_btn_loc = (By.ID, 'com.lansent.renting:id/main_home_top_add_iv')

    def hint_income(self):
        self.click_element(*self.eye_btn_loc)

    def click_income_help(self):
        self.click_element(*self.income_help_btn_loc)

    def click_my_bill(self):
        self.click_element(*self.my_bill_btn_loc)

    def click_my_bonus(self):
        self.click_element(*self.my_bonus_btn_loc)

    def click_my_house(self):
        self.click_element(*self.my_house_btn_loc)

    def click_my_tenant(self):
        self.click_element(*self.my_tenant_btn_loc)

    def click_add(self):
        self.click_element(*self.top_add_btn_loc)