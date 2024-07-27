import time

from helpers import BASE_URL
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainLocators


class MainPage(BasePage, HeaderLocators, MainLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.open_page(BASE_URL)

    def close_privacy_window(self):
        self.click(self.PRIVACY_WINDOW)

    def get_href_of_first_product(self):
        return self.get_href(self.FIRST_ITEM_NAME)

    def assert_that_mainpage_is_opened(self):
        assert self.get_element(self.MAIN_LOGO)
        assert self.get_element(self.PROFILE_FIELD)
        assert self.get_element(self.BASKET)

    def assert_context(self):
        self.get_element(self.PROFILE_FIELD).click()
        time.sleep(1)
        assert self.get_element(self.CONTEXT_MENU)

    def assert_item_to_basket(self):
        self.click(self.FIRST_ITEM_BUTTON)
        time.sleep(1)
        assert self.ITEM_TO_BASKET
