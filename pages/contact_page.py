import time

from pages.base_page import BasePage
from locators.contact_locators import ContactLocators
from selenium.webdriver.common.keys import Keys

import allure


class ContactPage(BasePage, ContactLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_contact_page_is_opened(self):
        with allure.step('Assert that contact page is opened'):
            assert self.get_element(self.PRODUCT)
            assert self.get_element(self.ORDER)
            assert self.get_element(self.CLAIMS)
            assert self.get_element(self.SERVICE)
            assert self.get_element(self.OTHER)