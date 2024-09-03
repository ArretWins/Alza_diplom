import time

from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from selenium.webdriver.common.keys import Keys

import allure


class LoginPage(BasePage, LoginLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Login by google')
    def login_by_google(self):
        self.click(self.GOOGLE_LOGIN)
        self.driver.implicitly_wait(1)

    @allure.step('Login by apple')
    def login_by_apple(self):
        self.click(self.APPLE_LOGIN)
        self.driver.implicitly_wait(1)

    @allure.step('Click on "forgot password" button')
    def forgot_password(self):
        self.click(self.FORGOT_PASSWORD)

    @allure.step('Send email')
    def send_email(self):
        self.fill(self.EMAIL_FIELD, 'alzatestuser@gmail.com')

    @allure.step('Send password')
    def send_password(self):
        self.fill(self.PASSWORD_FIELD, 'testuser02')

    @allure.step('Click on "Login" button')
    def login(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step('Check if login is opened')
    def assert_that_login_is_opened(self):
        assert self.get_element(self.EMAIL_FIELD)
        assert self.get_element(self.PASSWORD_FIELD)
        assert self.get_element(self.LOGIN_BUTTON)

    @allure.step('Fill in invalid login form')
    def assert_fill_invalid_login_form(self):
        self.fill(self.EMAIL_FIELD, 'wrong@@mail.com')
        self.fill(self.PASSWORD_FIELD, '123456789qawsed')
        self.login()
        assert self.get_element(self.LOGIN_BUTTON)

    @allure.step('Fill login form without password')
    def assert_miss_password_login_form(self):
        self.fill(self.EMAIL_FIELD, 'wrong@@mail.com')
        self.login()
        assert self.get_element(self.EMPTY_FORM)

    @allure.step('Fill login form without email')
    def assert_miss_email_login_form(self):
        self.fill(self.PASSWORD_FIELD, '123456789qawsed')
        self.login()
        assert self.get_element(self.EMPTY_FORM)

    @allure.step('Assert that Google and Apple buttons exists')
    def assert_login_social_buttons(self):
        assert self.get_element(self.GOOGLE_LOGIN)
        assert self.get_element(self.APPLE_LOGIN)

    @allure.step('Assert that Google login works')
    def assert_that_google_login_works(self):
        assert self.get_element(self.GOOGLE_CHOOSE_PAGE)

    @allure.step('Assert that Apple login works')
    def assert_that_apple_login_works(self):
        assert self.get_element(self.APPLE_CHOOSE_PAGE)

