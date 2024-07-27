from pages.base_page import BasePage
from locators.basket_locators import BasketLocators


class BasketPage(BasePage, BasketLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_href_of_main_product(self):
        return self.get_href(self.MAIN_ITEM_NAME)

    def get_price_of_product(self):
        return self.get_price(self.LAST_PRICE)

    def assert_that_basket_is_opened(self):
        assert self.get_element(self.BASKET_STEPS)
        assert self.get_element(self.BASKET_TAB)
        assert self.get_element(self.BACK_TO_MAIN_BUTTON)

    def assert_that_basket_is_empty(self):
        assert self.get_element(self.EMPTY_BASKET)

    def assert_that_basket_is_not_empty(self):
        assert self.get_element(self.MAIN_ITEM_NAME)

    def assert_plus_button_is_worked(self):
        old_price = self.get_price(self.LAST_PRICE)
        self.click(self.PLUS_BUTTON)
        new_price = self.get_price(self.LAST_PRICE)
        assert old_price == new_price / 2

    def assert_minus_button_is_worked(self):
        self.click(self.PLUS_BUTTON)
        old_price = self.get_price(self.LAST_PRICE)
        self.click(self.MINUS_BUTTON)
        new_price = self.get_price(self.LAST_PRICE)
        assert new_price == old_price / 2
