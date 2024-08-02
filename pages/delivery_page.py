import time

from selenium.common import NoSuchElementException, TimeoutException

from pages.base_page import BasePage
from locators.delivery_locators import DeliveryLocators
from selenium.webdriver.common.keys import Keys

import allure

class DeliveryPage(BasePage, DeliveryLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def close_dialog_window(self):
        with allure.step('Close dialog window'):
            try:
                self.click(self.CLOSE_DIALOG_BUTTON)
            except (NoSuchElementException, TimeoutException) as e:
                print(f"Could not close dialog window: {e}")
                assert False, f"Could not close dialog window: {e}"

    def open_alza_box(self):
        with allure.step('Open alza box'):
            self.click(self.ALZA_BOX)

    def open_show_room(self):
        with allure.step('Open show room'):
            self.click(self.SHOWROOM)

    def open_markets(self):
        with allure.step('Open markets'):
            self.click(self.MARKET)

    def open_markets_and_boxes(self):
        with allure.step('Open markets and boxes'):
            self.click(self.MARKETS_AND_BOXES)

    def open_delivery_to_address(self):
        with allure.step('Open delivery to address'):
            self.click(self.DELIVERY_TO_ADDRESS)

    def assert_that_delivery_is_opened(self):
        with allure.step('Check if delivery page is opened'):
            assert self.get_element(self.DELIVERY_CONTAINER)


