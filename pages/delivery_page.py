import time

from helpers.assertions import Assertions
from pages.base_page import BasePage
from locators.delivery_locators import DeliveryLocators
from selenium.webdriver.common.keys import Keys

import allure


class DeliveryPage(BasePage, DeliveryLocators, Assertions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open alza box')
    def open_alzabox(self):
        self.click(self.ALZA_BOX)
        self.driver.implicitly_wait(1)

    @allure.step('Open showroom')
    def open_showroom(self):
        self.click(self.SHOWROOM)

    @allure.step('Open markets')
    def open_markets(self):
        self.click(self.MARKET)

    @allure.step('Open markets and boxes')
    def open_markets_and_boxes(self):
        self.click(self.MARKETS_AND_BOXES)

    @allure.step('Open delivery to address')
    def open_delivery_to_address(self):
        self.click(self.DELIVERY_TO_ADDRESS)

    @allure.step('Choose address for delivery')
    def choose_address(self):
        self.fill(self.DELIVERY_INPUT, '040 01')
        time.sleep(2)
        self.fill(self.DELIVERY_INPUT, Keys.ARROW_DOWN)
        self.fill(self.DELIVERY_INPUT, Keys.ENTER)

    @allure.step('Confirm delivery time')
    def confirm_delivery_time(self):
        self.click(self.DELIVERY_TIME_BUTTON)

    @allure.step('Confirm showroom')
    def confirm_showroom(self):
        self.click(self.SHOWROOM_COMFIRM)

    @allure.step('Buy in alza box')
    def buy_alza_box(self):
        self.click(self.BRATISlAVA_MARKET)
        self.driver.implicitly_wait(1)
        self.click(self.MARKET_CONFIRM)

    @allure.step('Buy in alza box')
    def buy_in_markets_and_boxes(self):
        self.click(self.BRATISlAVA_MARKET)
        self.driver.implicitly_wait(1)
        self.click(self.MARKET_CONFIRM)

    @allure.step('Buy in market')
    def buy_in_market(self):
        self.click(self.BRATISlAVA_MARKET)
        self.click(self.MARKET_CONFIRM)

    @allure.step('Check if delivery page is opened')
    def assert_that_delivery_is_opened(self):
        assert self.get_element(self.DELIVERY_CONTAINER)

    @allure.step('Check if payment method is checked')
    def assert_that_method_is_checked(self):
        assert self.get_element(self.CHECKED_LABEL)

    @allure.step('Check if alzabox method is checked')
    def assert_that_alzabox_is_checked(self):
        self.assert_that_method_is_checked()
        self.assert_that_element_is_invisible(self.SHOWROOM_CHECKBOX)
        self.assert_that_element_is_invisible(self.MARKET_CHECKBOX)
        self.assert_that_element_is_invisible(self.MARKETS_AND_BOXES_CHECKBOX)
        self.assert_that_element_is_invisible(self.DELIVERY_TO_ADDRESS_CHECKBOX)

    @allure.step('Check if showroom method is checked')
    def assert_that_showroom_is_checked(self):
        self.assert_that_method_is_checked()
        self.assert_that_element_is_invisible(self.ALZA_BOX_CHECKBOX)
        self.assert_that_element_is_invisible(self.MARKET_CHECKBOX)
        self.assert_that_element_is_invisible(self.MARKETS_AND_BOXES_CHECKBOX)
        self.assert_that_element_is_invisible(self.DELIVERY_TO_ADDRESS_CHECKBOX)

    @allure.step('Check if market method is checked')
    def assert_that_market_is_checked(self):
        self.assert_that_method_is_checked()
        self.assert_that_element_is_invisible(self.ALZA_BOX_CHECKBOX)
        self.assert_that_element_is_invisible(self.SHOWROOM_CHECKBOX)
        self.assert_that_element_is_invisible(self.MARKETS_AND_BOXES_CHECKBOX)
        self.assert_that_element_is_invisible(self.DELIVERY_TO_ADDRESS_CHECKBOX)

    @allure.step('Check if markets and boxes method is checked')
    def assert_that_markets_and_boxes_is_checked(self):
        self.assert_that_method_is_checked()
        self.assert_that_element_is_invisible(self.ALZA_BOX_CHECKBOX)
        self.assert_that_element_is_invisible(self.SHOWROOM_CHECKBOX)
        self.assert_that_element_is_invisible(self.MARKET_CHECKBOX)
        self.assert_that_element_is_invisible(self.DELIVERY_TO_ADDRESS_CHECKBOX)

    @allure.step('Check if delivery method is checked')
    def assert_that_delivery_to_address_is_checked(self):
        self.assert_that_method_is_checked()
        self.assert_that_element_is_invisible(self.ALZA_BOX_CHECKBOX)
        self.assert_that_element_is_invisible(self.SHOWROOM_CHECKBOX)
        self.assert_that_element_is_invisible(self.MARKET_CHECKBOX)
        self.assert_that_element_is_invisible(self.MARKETS_AND_BOXES_CHECKBOX)
