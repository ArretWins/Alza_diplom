import time

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

    @allure.step('Take href of first product in main page')
    def get_href_of_first_product(self):
        return self.get_href(self.FIRST_ITEM_NAME)

    @allure.step('Click comment button')
    def click_comment_button(self):
        self.click(self.COMMENT_BUTTON)

    @allure.step('Click to delivery title')
    def click_to_delivery(self):
        self.click(self.DELIVERY_TITLE)

    @allure.step('Click photos button')
    def click_photos(self):
        self.click(self.ALL_PHOTOS)

    @allure.step('Click discussions button')
    def click_discussions(self):
        self.click(self.DISCUSSION_POSTS)

    @allure.step('Click to answer button')
    def click_to_answer(self):
        self.click(self.ANSWER_SPAN)

    @allure.step('Click to compare button')
    def click_to_compare(self):
        self.click(self.COMPARE_ITEMS)

    @allure.step('Fill the discussions input field')
    def fill_discussions_input(self):
        self.fill(self.DISCUSSION_INPUT, 'GB')
        self.driver.implicitly_wait(2)

    @allure.step('Open product photos')
    def open_photos(self):
        self.click(self.PHOTO_LAB)

    @allure.step('Search address for delivery')
    def search_address(self):
        self.fill(self.DELIVERY_INPUT, '040 11')
        time.sleep(2)

    @allure.step('Choose address for delivery')
    def choose_address(self):
        self.fill(self.DELIVERY_INPUT, Keys.ARROW_DOWN)
        self.fill(self.DELIVERY_INPUT, Keys.ENTER)
        self.driver.implicitly_wait(1)

    @allure.step('Buy products')
    def buy_product(self):
        self.click(self.BUY_BUTTON)
        try:
            self.click(self.CLOSE_DIALOG_BUTTON)
        except Exception as e:
            print(f"Dialog box did not appear: {e}")

    @allure.step('Assert product page is opened')
    def assert_that_productpage_is_opened(self):
        assert self.get_element(self.PRODUCT_NAME)
        assert self.get_element(self.PRODUCT_PRICE)
        assert self.get_element(self.PRODUCT_RATING)
        assert self.get_element(self.PRODUCT_GALLERY)
        assert self.get_element(self.PRODUCT_DESCRIPTION)

    @staticmethod
    @allure.step('Assert product names are equals')
    def assert_that_names_are_equals(name_1, name_2):
        assert name_1 == name_2

    @allure.step('Assert cross sell page')
    def assert_cross_sell_page(self):
        assert self.get_element(self.CROSS_SELL_MESSAGE)

    @allure.step('Assert login is opened')
    def assert_that_login_is_opened(self):
        assert self.get_element(self.EMAIL_FIELD)
        assert self.get_element(self.PASSWORD_FIELD)
        assert self.get_element(self.LOGIN_BUTTON)

    @allure.step('Assert dialog window is opened')
    def assert_dialog_window_is_opened(self):
        assert self.get_element(self.DETAIL_DIALOG)

    @allure.step('Assert that delivery search works')
    def assert_that_delivery_search_works(self):
        assert self.get_element(self.DELIVERY_INFO)

    @allure.step('Assert that photos are opened')
    def assert_that_photos_are_opened(self):
        assert self.get_element(self.FANCY_BOX)

    @allure.step("Assert that discussions are opened")
    def assert_that_discussions_are_opened(self):
        assert self.get_element(self.DISCUSSION_POSTS)

    @allure.step('Assert that answers are opened')
    def assert_that_answer_is_opened(self):
        assert self.get_element(self.EXPERT_IMAGE)

    @allure.step('Assert compare message')
    def assert_compare_message(self):
        assert self.get_element(self.SUCCESS_COMPARE_ITEMS)

    @allure.step('Get product name')
    def get_product_name(self):
        time.sleep(1)
        return self.get_text(self.PRODUCT_NAME)
