from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@id="userName"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@id="btnLogin"]')
    WRONG_FORM = (By.XPATH, '//button[@class="btn btn-login mt-2 invalid"]')
    EMPTY_FORM = (By.XPATH, '//span[@class="validation-message"]')
