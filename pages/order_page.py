from pages.base_page import BasePage
from locators.order_locators import OrderLocators
import allure

class OrdersPage(BasePage, OrderLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_orderspage_is_opened(self):
        with allure.step('Assert that orders are open'):
            assert self.get_element(self.SEARCH_ORDER_TEXT)
            assert self.get_element(self.SEARCH_ORDER_INPUT)
            assert self.get_element(self.SEARCH_ORDER_BUTTON)
