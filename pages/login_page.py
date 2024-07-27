from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage, LoginLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_login_is_opened(self):
        assert self.get_element(self.EMAIL_FIELD)
        assert self.get_element(self.PASSWORD_FIELD)
        assert self.get_element(self.LOGIN_BUTTON)

    def assert_fill_invalid_login_form(self):
        self.fill(self.EMAIL_FIELD, 'wrong@@mail.com')
        self.fill(self.PASSWORD_FIELD, '123456789qawsed')
        self.click(self.LOGIN_BUTTON)
        assert self.get_element(self.LOGIN_BUTTON)

    def assert_miss_password_login_form(self):
        self.fill(self.EMAIL_FIELD, 'wrong@@mail.com')
        self.click(self.LOGIN_BUTTON)
        assert self.get_element(self.EMPTY_FORM)

    def assert_miss_email_login_form(self):
        self.fill(self.PASSWORD_FIELD, '123456789qawsed')
        self.click(self.LOGIN_BUTTON)
        assert self.get_element(self.EMPTY_FORM)
