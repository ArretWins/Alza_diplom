from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_TITLE = (By.XPATH, '//div[@class="login-title"]')
    EMAIL_FIELD = (By.XPATH, '//input[@id="userName"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@id="btnLogin"]')
    WRONG_FORM = (By.XPATH, '//button[@class="btn btn-login mt-2 invalid"]')
    EMPTY_FORM = (By.XPATH, '//span[@class="validation-message"]')
    FORGOT_PASSWORD = (By.XPATH, '//a[@id="forgotPasswordLink"]')
    GOOGLE_LOGIN = (By.XPATH, '//a[@data-tid="login-by-Google"]')
    APPLE_LOGIN = (By.XPATH, '//a[@data-tid="login-by-Apple"]')
    GOOGLE_CHOOSE_PAGE = (By.XPATH, '//h1[@id="headingText"]')
    APPLE_CHOOSE_PAGE = (By.XPATH, '//div[@class="ac-localnav-content"]')
