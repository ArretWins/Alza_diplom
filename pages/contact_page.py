import time

from pages.base_page import BasePage
from locators.contact_locators import ContactLocators
from selenium.webdriver.common.action_chains import ActionChains

import allure


class ContactPage(BasePage, ContactLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Click product button')
    def click_product(self):
        self.click(self.PRODUCT)

    @allure.step('Click order button')
    def click_order(self):
        self.click(self.ORDER)

    @allure.step('Click claims button')
    def click_claims(self):
        self.click(self.CLAIMS)

    @allure.step('Click service button')
    def click_service(self):
        self.click(self.SERVICE)

    @allure.step('Click other button')
    def click_other(self):
        self.click(self.OTHER)

    @allure.step('Click post button')
    def click_post(self):
        self.click(self.POST_CONTAINER)

    @allure.step('Click alza plus span')
    def click_alza_plus(self):
        self.click(self.ALZA_PLUS)

    @allure.step('Click alza plus list')
    def click_alza_list(self):
        self.click(self.ALZA_PLUS_LIST)

    @allure.step('Click alza plus href')
    def click_alza_href(self):
        self.click(self.ALZA_PLUS_HREF)

    @allure.step('Scroll')
    def scroll(self):
        action = ActionChains(self.driver)
        action.scroll_to_element(self.MESSAGE_AREA)

    @allure.step('Search product')
    def search_input(self):
        self.fill(self.PRODUCT_INPUT, "Macbook m1 vesm")
        self.click(self.CHOOSE_PRODUCT)

    @allure.step('Search discussion')
    def search_discussion(self):
        self.fill(self.DISCUSSION_SEARCH, "Minecrat")
        time.sleep(3)

    @allure.step('Assert that contact page is opened')
    def assert_that_contact_page_is_opened(self):
        assert self.get_element(self.PRODUCT)
        assert self.get_element(self.ORDER)
        assert self.get_element(self.CLAIMS)
        assert self.get_element(self.SERVICE)
        assert self.get_element(self.OTHER)

    @allure.step('Assert answer')
    def assert_answer(self):
        assert self.get_element(self.ANSWER)

    @allure.step("Assert that alza+ page is opened")
    def assert_that_alza_plus_page_is_opened(self):
        assert self.get_element(self.ALZA_PLUS_PAGE)
