import time

from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from selenium.webdriver.common.keys import Keys

import allure

class LoginPage(BasePage, LoginLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_by_google(self):
        with allure.step('Login by google'):
            self.click(self.GOOGLE_LOGIN)
            time.sleep(1)

    def login_by_apple(self):
        with allure.step('Login by apple'):
            self.click(self.APPLE_LOGIN)
            time.sleep(1)

    def forgot_password(self):
        with allure.step('Click on "forgot password" button'):
            self.click(self.FORGOT_PASSWORD)


    def assert_that_login_is_opened(self):
        with allure.step('Check if login is opened'):
            assert self.get_element(self.EMAIL_FIELD)
            assert self.get_element(self.PASSWORD_FIELD)
            assert self.get_element(self.LOGIN_BUTTON)

    def assert_fill_invalid_login_form(self):
        with allure.step('Fill in invalid login form'):
            self.fill(self.EMAIL_FIELD, 'wrong@@mail.com')
            self.fill(self.PASSWORD_FIELD, '123456789qawsed')
            self.click(self.LOGIN_BUTTON)
            assert self.get_element(self.LOGIN_BUTTON)

    def assert_miss_password_login_form(self):
        with allure.step('Fill login form without password'):
            self.fill(self.EMAIL_FIELD, 'wrong@@mail.com')
            self.click(self.LOGIN_BUTTON)
            assert self.get_element(self.EMPTY_FORM)

    def assert_miss_email_login_form(self):
        with allure.step('Fill login form without email'):
            self.fill(self.PASSWORD_FIELD, '123456789qawsed')
            self.click(self.LOGIN_BUTTON)
            assert self.get_element(self.EMPTY_FORM)

    def assert_login_social_buttons(self):
        with allure.step('Assert that Google and Apple buttons exists'):
            assert self.get_element(self.GOOGLE_LOGIN)
            assert self.get_element(self.APPLE_LOGIN)

    def assert_that_google_login_works(self):
        with allure.step('Assert that Google login works'):
            assert self.get_element(self.GOOGLE_CHOOSE_PAGE)

    def assert_that_apple_login_works(self):
        with allure.step('Assert that Apple login works'):
            assert self.get_element(self.APPLE_CHOOSE_PAGE)

