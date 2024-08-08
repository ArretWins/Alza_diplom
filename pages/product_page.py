import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.product_locators import ProductLocators
from locators.main_page_locators import MainLocators
from locators.login_locators import LoginLocators
import allure


class ProductPage(BasePage, ProductLocators, MainLocators, LoginLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_href_of_first_product(self):
        with allure.step('Take href of first product in main page'):
            return self.get_href(self.FIRST_ITEM_NAME)

    def click_comment_button(self):
        with allure.step('Click comment button'):
            self.click(self.COMMENT_BUTTON)

    def click_to_delivery(self):
        with allure.step('Click to delivery title'):
            self.click(self.DELIVERY_TITLE)

    def search_address(self):
        with allure.step('Search address for delivery'):
            self.fill(self.DELIVERY_INPUT, '040 11')

    def choose_address(self):
        with allure.step('Choose address for delivery'):
            self.fill(self.DELIVERY_INPUT, Keys.ARROW_DOWN)
            self.fill(self.DELIVERY_INPUT, Keys.ENTER)

    def close_privacy_window(self):
        with allure.step('Close privacy window'):
            try:
                self.click(self.PRIVACY_WINDOW)
            except (NoSuchElementException, TimeoutException) as e:
                pass

    def buy_product(self):
        with allure.step('Buy products'):
            self.close_privacy_window()
            # time.sleep(12)
            self.click(self.BUY_BUTTON)
            try:
                self.click(self.CLOSE_DIALOG_BUTTON)
            except Exception as e:
                print(f"Dialog box did not appear: {e}")

    def assert_that_productpage_is_opened(self):
        with allure.step('Assert product page is opened'):
            assert self.get_element(self.PRODUCT_NAME)
            assert self.get_element(self.PRODUCT_PRICE)
            assert self.get_element(self.PRODUCT_RATING)
            assert self.get_element(self.PRODUCT_GALLERY)
            assert self.get_element(self.PRODUCT_DESCRIPTION)

    def assert_that_names_are_equals(self, name_1, name_2):
        with allure.step('Assert product names are equals'):
            assert name_1 == name_2

    def assert_cross_sell_page(self):
        with allure.step('Assert cross sell page'):
            assert self.get_element(self.BACK_TO_PRODUCT_BUTTON)
            assert self.get_element(self.FORWARD_BUTTON)
            assert self.get_element(self.CAROUSEL_CONTENT)

    def assert_that_login_is_opened(self):
        with allure.step('Assert login is opened'):
            # self.driver.execute_script("arguments[0].focus();", self.LOGIN_TITLE)
            # self.click_comment_button()
            assert self.get_element(self.EMAIL_FIELD)
            assert self.get_element(self.PASSWORD_FIELD)
            assert self.get_element(self.LOGIN_BUTTON)

    def assert_dialog_window_is_opened(self):
        with allure.step('Assert dialog window is opened'):
            assert self.get_element(self.DETAIL_DIALOG)

    def assert_that_delivery_search_works(self):
        with allure.step('Assert that delivery search works'):
            assert self.get_element(self.DELIVERY_INFO)

    def get_product_name(self):
        with allure.step('Get product name'):
            time.sleep(1)
            return self.get_text(self.PRODUCT_NAME)

