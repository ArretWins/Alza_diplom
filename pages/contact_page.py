import time

from pages.base_page import BasePage
from locators.contact_locators import ContactLocators
from selenium.webdriver.common.keys import Keys

import allure


class ContactPage(BasePage, ContactLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_product(self):
        with allure.step('Click product button'):
            self.click(self.PRODUCT)

    def click_order(self):
        with allure.step('Click order button'):
            self.click(self.ORDER)

    def click_claims(self):
        with allure.step('Click claims button'):
            self.click(self.CLAIMS)

    def click_service(self):
        with allure.step('Click service button'):
            self.click(self.SERVICE)

    def click_other(self):
        with allure.step('Click other button'):
            self.click(self.OTHER)

    def click_post(self):
        with allure.step('Click post button'):
            self.click(self.POST_CONTAINER)

    def search_input(self):
        with allure.step('Search product'):
            self.fill(self.PRODUCT_INPUT, "Macbook")
            self.click(self.CHOOSE_PRODUCT)

    def search_discussion(self):
        with allure.step('Search discussion'):
            self.fill(self.DISCUSSION_SEARCH, "Minecrat")
            time.sleep(3)

    def assert_that_contact_page_is_opened(self):
        with allure.step('Assert that contact page is opened'):
            assert self.get_element(self.PRODUCT)
            assert self.get_element(self.ORDER)
            assert self.get_element(self.CLAIMS)
            assert self.get_element(self.SERVICE)
            assert self.get_element(self.OTHER)

    def assert_answer(self):
        with allure.step('Assert answer'):
            assert self.get_element(self.ANSWER)
