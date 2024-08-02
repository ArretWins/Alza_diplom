import time

from selenium.common import NoSuchElementException, TimeoutException

from helpers import BASE_URL
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainLocators
from locators.product_locators import ProductLocators
import allure


class MainPage(BasePage, HeaderLocators, MainLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        with allure.step('Open main page'):
            self.open_page(BASE_URL)

    def close_privacy_window(self):
        with allure.step('Close privacy window'):
            try:
                self.click(self.PRIVACY_WINDOW)
            except (NoSuchElementException, TimeoutException) as e:
                print(f"Could not close privacy window: {e}")
                assert False, f"Could not close privacy window: {e}"

    def open_first_product(self):
        with allure.step('Open first product'):
            self.click(self.FIRST_PRODUCT)

    def get_name_of_first_product(self):
        with allure.step('Get name of first product'):
            return self.get_text(self.FIRST_PRODUCT)

    def get_href_of_first_product(self):
        with allure.step('Take href of first product in main page'):
            return self.get_href(self.FIRST_ITEM_NAME)

    def assert_that_mainpage_is_opened(self):
        with allure.step('Assert main page is opened'):
            assert self.get_element(self.MAIN_LOGO)
            assert self.get_element(self.PROFILE_FIELD)
            assert self.get_element(self.BASKET)

    def assert_context(self):
        self.get_element(self.PROFILE_FIELD).click()
        time.sleep(1)
        assert self.get_element(self.CONTEXT_MENU)

    def assert_item_to_basket(self):
        with allure.step('Take item to basket'):
            self.click(self.FIRST_ITEM_BUTTON)
            time.sleep(1)
            assert self.ITEM_TO_BASKET

    def change_language(self):
        with allure.step('Change language'):
            self.click(self.LANGUAGE_SWITCHER)
            web = 'Alza.sk - Jazyk / Language'
            web2 = 'Alza.sk - Language'
            time.sleep(1)
            status_language_element = self.driver.find_element(*self.STATUS_LANGUAGE)
            status_language_text = status_language_element.text
            if web in status_language_text:
                with allure.step('Switch to english'):
                    self.click(self.ENGLISH_BUTTON)
            if web2 in status_language_text:
                with allure.step('Switch to slovak'):
                    self.click(self.SLOVAK_BUTTON)
            self.click(self.CONFIRM_BUTTON)

    def assert_that_language_switched_to_english(self):
        with allure.step("Assert language is switched to English"):
            assert self.PHONES

    def assert_that_language_switched_to_slovak(self):
        with allure.step("Assert language is switched to Slovak"):
            assert self.MOBILY
