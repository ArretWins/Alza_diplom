import time

from selenium.common import NoSuchElementException, TimeoutException

from helpers import BASE_URL
from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainLocators
from locators.product_locators import ProductLocators
import allure


class MainPage(BasePage, HeaderLocators, MainLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open main page')
    def open(self):
        self.open_page(BASE_URL)
        self.add_cookies('ALWCS', '0')
        self.add_cookies('CBARIH', '1')
        self.driver.refresh()

    @allure.step('Close privacy window')
    def close_privacy_window(self):
        try:
            self.click(self.PRIVACY_WINDOW)
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Could not close privacy window: {e}")
            assert False, f"Could not close privacy window: {e}"

    @allure.step('Open first product')
    def open_first_product(self):
        self.click(self.FIRST_PRODUCT)

    @allure.step('Open product page')
    def to_product_page(self):
        self.open()
        self.go_to_laptops()
        # self.close_privacy_window()
        name_from_main_page = self.get_name_of_first_product()
        self.open_first_product()
        return name_from_main_page

    # @allure.step('Buy first product')
    # def buy_first_product(self):
    #     self.add_item_to_basket_and_assert()

    @allure.step('Get name of first product')
    def get_name_of_first_product(self):
        return self.get_text(self.FIRST_PRODUCT)

    @allure.step('Getting price from main page')
    def get_price_of_product(self):
            return self.get_price(self.FINAL_PRICE)

    @allure.step('Assert main page is opened')
    def assert_that_mainpage_is_opened(self):
        assert self.get_element(self.MAIN_LOGO)
        assert self.get_element(self.PROFILE_FIELD)
        assert self.get_element(self.BASKET)

    def get_context_menu(self):
        self.click(self.PROFILE_FIELD)
        time.sleep(1)

    @allure.step('Go to contacts page')
    def go_to_contacts(self):
        # self.close_privacy_window()
        self.click(self.CONTACT_TITLE)

    @allure.step('Go to laptops page')
    def go_to_laptops(self):
        self.click(self.LAPTOPS)
        self.click(self.LAPTOPS_SPAN)

    @allure.step('Take item to basket')
    def add_item_to_basket(self):
        self.click(self.FIRST_ITEM_BUTTON)
        time.sleep(2)

    @allure.step('Change language')
    def change_language(self):
        self.click(self.LANGUAGE_SWITCHER)
        web = 'Alza.sk - Jazyk / Language'
        web2 = 'Alza.sk - Language'
        time.sleep(1)
        status_language_element = self.driver.find_element(*self.STATUS_LANGUAGE)
        status_language_text = status_language_element.text
        if web in status_language_text:
            with allure.step('Switch to english'):
                self.click(self.ENGLISH_BUTTON)
        if web2 in status_language_text:
            with allure.step('Switch to slovak'):
                self.click(self.SLOVAK_BUTTON)
        self.click(self.CONFIRM_BUTTON)

    @allure.step("Assert language is switched to English")
    def assert_that_language_switched_to_english(self):
        assert self.PHONES

    @allure.step("Assert language is switched to Slovak")
    def assert_that_language_switched_to_slovak(self):
        assert self.MOBILY

    @allure.step('Take item to basket')
    def assert_that_item_added(self):
        assert self.get_element(self.ITEM_TO_BASKET)
