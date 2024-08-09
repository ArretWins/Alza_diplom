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

    def open_alzabox(self):
        with allure.step('Open alza box'):
            self.click(self.ALZA_BOX)
            time.sleep(1)

    def open_showroom(self):
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

    def choose_address(self):
        with allure.step('Choose address for delivery'):
            self.fill(self.DELIVERY_INPUT, '040 01')
            time.sleep(2)
            self.fill(self.DELIVERY_INPUT, Keys.ARROW_DOWN)
            self.fill(self.DELIVERY_INPUT, Keys.ENTER)

    def confirm_delivery_time(self):
        with allure.step('Confirm delivery time'):
            self.click(self.DELIVERY_TIME_BUTTON)

    def confirm_showroom(self):
        with allure.step('Confirm showroom'):
            self.click(self.SHOWROOM_COMFIRM)

    def buy_alza_box(self):
        with allure.step('Buy in alza box'):
            self.click(self.BRATISlAVA_MARKET)
            self.click(self.MARKET_CONFIRM)

    def buy_in_markets_and_boxes(self):
        with allure.step('Buy in markets and boxes'):
            self.click(self.DROGERIA)
            self.click(self.DROGERIA_CONFIRM)

    def buy_in_market(self):
        with allure.step('Buy in market'):
            self.click(self.SENEC_MARKET)
            self.click(self.OPENING_HOURS)
            self.click(self.MARKET_CONFIRM)

    def assert_that_delivery_is_opened(self):
        with allure.step('Check if delivery page is opened'):
            assert self.get_element(self.DELIVERY_CONTAINER)

    def assert_that_method_is_checked(self):
        with allure.step('Check if payment method is checked'):
            assert self.get_element(self.CHECKED_LABEL)
