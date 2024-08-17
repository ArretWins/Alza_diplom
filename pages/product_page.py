import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
            self.close_privacy_window()
            self.click(self.DELIVERY_TITLE)

    def click_photos(self):
        with allure.step('Click photos button'):
            self.close_privacy_window()
            self.click(self.ALL_PHOTOS)

    def click_discussions(self):
        with allure.step('Click discussions button'):
            self.click(self.DISCUSSION_POSTS)

    def click_to_answer(self):
        with allure.step('Click to answer button'):
            self.click(self.ANSWER_SPAN)

    def click_to_compare(self):
        with allure.step('Click to compare button'):
            self.close_privacy_window()
            self.click(self.COMPARE_ITEMS)

    def fill_discussions_input(self):
        with allure.step('Fill the discussions input field'):
            self.fill(self.DISCUSSION_INPUT, '16GB')
            time.sleep(2)

    def open_photos(self):
        with allure.step('Open product photos'):
            self.click(self.PHOTO_LAB)

    def search_address(self):
        with allure.step('Search address for delivery'):
            self.fill(self.DELIVERY_INPUT, '040 11')
            time.sleep(2)

    def choose_address(self):
        with allure.step('Choose address for delivery'):
            self.fill(self.DELIVERY_INPUT, Keys.ARROW_DOWN)
            self.fill(self.DELIVERY_INPUT, Keys.ENTER)
            time.sleep(1)

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

    @staticmethod
    def assert_that_names_are_equals(name_1, name_2):
        with allure.step('Assert product names are equals'):
            assert name_1 == name_2

    def assert_cross_sell_page(self):
        with allure.step('Assert cross sell page'):
            assert self.get_element(self.CROSS_SELL_MESSAGE)

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

    def assert_that_photos_are_opened(self):
        with allure.step('Assert that photos are opened'):
            assert self.get_element(self.FANCY_BOX)

    def assert_that_discussions_are_opened(self):
        with allure.step("Assert that discussions are opened"):
            assert self.get_element(self.DISCUSSION_POSTS)

    def assert_that_answer_is_opened(self):
        with allure.step('Assert that answers are opened'):
            assert self.get_element(self.EXPERT_IMAGE)

    def assert_compare_message(self):
        with allure.step('Assert compare message'):
            assert self.get_element(self.SUCCESS_COMPARE_ITEMS)

    def get_product_name(self):
        with allure.step('Get product name'):
            time.sleep(1)
            return self.get_text(self.PRODUCT_NAME)

