import time

from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.basket_locators import BasketLocators
import allure


class BasketPage(BasePage, BasketLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_href_of_main_product(self):
        with allure.step('Getting href of main product'):
            return self.get_href(self.MAIN_ITEM_NAME)

    def get_price_of_product(self):
        with allure.step('Getting price of'):
            return self.get_price(self.LAST_PRICE)

    def get_limit_of_product(self):
        with allure.step('Getting max limit of product'):
            limit = 1
            while True:
                self.click(self.PLUS_BUTTON)
                # self.click(self.PLUS_BUTTON)
                time.sleep(0.1)
                try:
                    self.get_element(self.PLUS_DISABLED)
                    limit = 2
                    break
                except TimeoutException:
                    continue
            print("LIMIT")


    def assert_that_basket_is_opened(self):
        with allure.step('Asserting basket is open'):
            assert self.get_element(self.BASKET_STEPS)
            assert self.get_element(self.BASKET_TAB)
            assert self.get_element(self.BACK_TO_MAIN_BUTTON)

    def assert_that_basket_is_empty(self):
        with allure.step('Asserting basket is empty'):
            assert self.get_element(self.EMPTY_BASKET)

    def assert_that_basket_is_not_empty(self):
        with allure.step('Asserting basket is not empty'):
            assert self.get_element(self.MAIN_ITEM_NAME)

    def assert_plus_button_is_worked(self):
        with allure.step('Asserting plus button is worked'):
            old_price = self.get_price(self.LAST_PRICE)
            self.click(self.PLUS_BUTTON)
            new_price = self.get_price(self.LAST_PRICE)
            assert old_price == new_price / 2

    def assert_minus_button_is_worked(self):
        with allure.step('Asserting minus button is worked'):
            self.click(self.PLUS_BUTTON)
            old_price = self.get_price(self.LAST_PRICE)
            self.click(self.MINUS_BUTTON)
            new_price = self.get_price(self.LAST_PRICE)
            assert new_price == old_price / 2

    def assert_disabled_plus_button(self):
        with allure.step('Asserting minus button is worked'):
            assert self.get_element(self.PLUS_DISABLED)