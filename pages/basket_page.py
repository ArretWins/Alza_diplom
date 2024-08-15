import time

from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.basket_locators import BasketLocators
import allure


class BasketPage(BasePage, BasketLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_name_of_main_product(self):
        with allure.step('Getting name of main product'):
            return self.get_text(self.MAIN_ITEM_NAME)

    def get_price_of_product(self):
        with allure.step('Getting price of'):
            return self.get_price(self.LAST_PRICE)

    def get_limit_of_product(self):
        with allure.step('Getting max limit of product'):
            limit = 1
            no_limit = 1
            while True:
                self.click(self.PLUS_BUTTON)
                time.sleep(0.1)
                no_limit += 1
                if no_limit > 3:
                    with allure.step('No limit of product'):
                        return False
                        break
                try:
                    self.get_element(self.PLUS_DISABLED)
                    limit = 2
                    return True
                    break
                except TimeoutException:
                    continue

    def click_plus_button(self):
        with allure.step('Click plus button'):
            self.click(self.PLUS_BUTTON)

    def click_minus_button(self):
        with allure.step('Click minus button'):
            self.click(self.MINUS_BUTTON)

    def delete_product(self):
        with allure.step('Click on "Delete from basket"'):
            time.sleep(1)
            self.click(self.DELETE_PRODUCT)

    def cancel_delete_product(self):
        with allure.step('Cancel delete of product'):
            self.click(self.CANCEL_DELETE_PRODUCT)

    def open_delivery_page(self):
        with allure.step('Open delivery page'):
            self.click(self.CONTINUE_BUTTON)

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
            self.click_plus_button()
            new_price = self.get_price(self.LAST_PRICE)
            assert old_price == new_price / 2

    def assert_minus_button_is_worked(self):
        with allure.step('Asserting minus button is worked'):
            self.click_plus_button()
            old_price = self.get_price(self.LAST_PRICE)
            self.click_minus_button()
            new_price = self.get_price(self.LAST_PRICE)
            assert new_price == old_price / 2

    def assert_disabled_plus_button(self):
        with allure.step('Asserting minus button is worked'):
            assert self.get_element(self.PLUS_DISABLED)

    def assert_that_product_deleted(self):
        with allure.step('Assert that product will be remove after click "minus button"'):
            assert self.get_element(self.EMPTY_IMAGE)

    @staticmethod
    def assert_that_prices_are_equals(price_1, price_2):
        with allure.step("Assert that prices are equals"):
            assert price_1 == price_2

    @staticmethod
    def assert_that_names_are_equals(name_1, name_2):
        with allure.step("Assert that names are equals"):
            assert name_1 in name_2
