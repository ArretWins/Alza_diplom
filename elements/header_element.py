import allure

from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.context_menu_locators import ContextMenuLocators


class HeaderElement(BasePage, HeaderLocators, ContextMenuLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_orders(self):
        self.click(self.ORDERS)

    def open_basket(self):
        self.click(self.BASKET)

    def open_login(self):
        self.click(self.CONTEXT_LOGIN)

    def assert_that_login_correct(self):
        with allure.step('Assert that your login was correct'):
            self.get_element(self.USER_LOGIN)
