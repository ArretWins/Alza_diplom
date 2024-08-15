import time

from selenium.common import NoSuchElementException, TimeoutException
from helpers.assertions import Assertions
from pages.base_page import BasePage
from locators.delivery_locators import DeliveryLocators
from selenium.webdriver.common.keys import Keys

import allure


class DeliveryPage(BasePage, DeliveryLocators, Assertions):

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
            self.click(self.ALZA_BOX, True)
            time.sleep(1)

    def open_showroom(self):
        with allure.step('Open showroom'):
            self.click(self.SHOWROOM)

    def open_markets(self):
        with allure.step('Open markets'):
            self.click(self.MARKET, True)

    def open_markets_and_boxes(self):
        with allure.step('Open markets and boxes'):
            self.click(self.MARKETS_AND_BOXES, True)

    def open_delivery_to_address(self):
        with allure.step('Open delivery to address'):
            self.click(self.DELIVERY_TO_ADDRESS, True)

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
            self.click(self.BRATISlAVA_MARKET, True)
            time.sleep(1)
            self.click(self.MARKET_CONFIRM)

    def buy_in_markets_and_boxes(self):
        with allure.step('Buy in alza box'):
            self.click(self.TATRACENTRUM_MARKET, True)
            time.sleep(1)
            self.click(self.MARKET_CONFIRM)

    def buy_in_market(self):
        with allure.step('Buy in market'):
            self.click(self.STREDA_MARKET, True)
            self.click(self.OPENING_HOURS)
            self.click(self.MARKET_CONFIRM)

    def assert_that_delivery_is_opened(self):
        with allure.step('Check if delivery page is opened'):
            assert self.get_element(self.DELIVERY_CONTAINER)

    def assert_that_method_is_checked(self):
        with allure.step('Check if payment method is checked'):
            assert self.get_element(self.CHECKED_LABEL)

    def assert_that_alzabox_is_checked(self):
        with allure.step('Check if alzabox method is checked'):
            self.assert_that_method_is_checked()
            self.assert_that_element_is_invisible(self.SHOWROOM_CHECKBOX)
            self.assert_that_element_is_invisible(self.MARKET_CHECKBOX)
            self.assert_that_element_is_invisible(self.MARKETS_AND_BOXES_CHECKBOX)
            self.assert_that_element_is_invisible(self.DELIVERY_TO_ADDRESS_CHECKBOX)

    def assert_that_showroom_is_checked(self):
        with allure.step('Check if showroom method is checked'):
            self.assert_that_method_is_checked()
            self.assert_that_element_is_invisible(self.ALZA_BOX_CHECKBOX)
            self.assert_that_element_is_invisible(self.MARKET_CHECKBOX)
            self.assert_that_element_is_invisible(self.MARKETS_AND_BOXES_CHECKBOX)
            self.assert_that_element_is_invisible(self.DELIVERY_TO_ADDRESS_CHECKBOX)

    def assert_that_market_is_checked(self):
        with allure.step('Check if market method is checked'):
            self.assert_that_method_is_checked()
            self.assert_that_element_is_invisible(self.ALZA_BOX_CHECKBOX)
            self.assert_that_element_is_invisible(self.SHOWROOM_CHECKBOX)
            self.assert_that_element_is_invisible(self.MARKETS_AND_BOXES_CHECKBOX)
            self.assert_that_element_is_invisible(self.DELIVERY_TO_ADDRESS_CHECKBOX)

    def assert_that_markets_and_boxes_is_checked(self):
        with allure.step('Check if markets and boxes method is checked'):
            self.assert_that_method_is_checked()
            self.assert_that_element_is_invisible(self.ALZA_BOX_CHECKBOX)
            self.assert_that_element_is_invisible(self.SHOWROOM_CHECKBOX)
            self.assert_that_element_is_invisible(self.MARKET_CHECKBOX)
            self.assert_that_element_is_invisible(self.DELIVERY_TO_ADDRESS_CHECKBOX)

    def assert_that_delivery_to_address_is_checked(self):
        with allure.step('Check if delivery method is checked'):
            self.assert_that_method_is_checked()
            self.assert_that_element_is_invisible(self.ALZA_BOX_CHECKBOX)
            self.assert_that_element_is_invisible(self.SHOWROOM_CHECKBOX)
            self.assert_that_element_is_invisible(self.MARKET_CHECKBOX)
            self.assert_that_element_is_invisible(self.MARKETS_AND_BOXES_CHECKBOX)