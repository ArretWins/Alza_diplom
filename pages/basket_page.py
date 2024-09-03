import time

from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.basket_locators import BasketLocators
import allure


class BasketPage(BasePage, BasketLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Getting name of main product')
    def get_name_of_main_product(self):
        return self.get_text(self.MAIN_ITEM_NAME)

    @allure.step('Getting price of product')
    def get_price_of_product(self):
        return self.get_price(self.LAST_PRICE)

    @allure.step('Getting max limit of product')
    def get_limit_of_product(self):
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
                return True
                break
            except TimeoutException:
                continue

    @allure.step('Click plus button')
    def click_plus_button(self):
        self.click(self.PLUS_BUTTON)

    @allure.step('Click minus button')
    def click_minus_button(self):
        self.click(self.MINUS_BUTTON)

    @allure.step('Click on "Delete from basket"')
    def delete_product(self):
        time.sleep(1)
        self.click(self.DELETE_PRODUCT)

    @allure.step('Cancel of deleting of product')
    def cancel_delete_product(self):
        self.click(self.CANCEL_DELETE_PRODUCT)

    @allure.step('Open delivery page')
    def open_delivery_page(self):
        self.click(self.CONTINUE_BUTTON)
        if self.get_element(self.CLOSE_ITEMS_BUTTON):
            self.close_added_items()

    @allure.step('Close added items')
    def close_added_items(self):
        self.click(self.CLOSE_ITEMS_BUTTON)

    @allure.step('Assert that basket is open')
    def assert_that_basket_is_opened(self):
        assert self.get_element(self.BASKET_STEPS)
        assert self.get_element(self.BASKET_TAB)
        assert self.get_element(self.BACK_TO_MAIN_BUTTON)

    @allure.step('Assert that basket is empty')
    def assert_that_basket_is_empty(self):
        assert self.get_element(self.EMPTY_BASKET)

    @allure.step('Assert that basket is not empty')
    def assert_that_basket_is_not_empty(self):
        assert self.get_element(self.MAIN_ITEM_NAME)

    @allure.step('Assert that plus button is worked')
    def assert_plus_button_is_worked(self):
        old_price = self.get_price(self.LAST_PRICE)
        self.click_plus_button()
        new_price = self.get_price(self.LAST_PRICE)
        assert old_price == new_price / 2

    @allure.step('Assert that minus button is worked')
    def assert_minus_button_is_worked(self):
        self.click_plus_button()
        old_price = self.get_price(self.LAST_PRICE)
        self.click_minus_button()
        new_price = self.get_price(self.LAST_PRICE)
        assert new_price == old_price / 2

    @allure.step('Assert that minus button is worked')
    def assert_disabled_plus_button(self):
        assert self.get_element(self.PLUS_DISABLED)

    @allure.step('Assert that product will be remove after click "minus button"')
    def assert_that_product_deleted(self):
        assert self.get_element(self.EMPTY_IMAGE)

    @allure.step("Assert that prices are equals")
    def assert_that_prices_are_equals(self, price_1):
        price_from_basket = self.get_price_of_product()
        assert price_1 == price_from_basket

    @allure.step("Assert that names are equals")
    def assert_that_names_are_equals(self, name_1):
        name_from_basket = self.get_name_of_main_product()
        assert name_1 in name_from_basket
