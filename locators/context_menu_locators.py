from selenium.webdriver.common.by import By


class ContextMenuLocators:
    CONTEXT_LOGIN = (By.XPATH, '//a[@data-testid="headerNavigationLogin"]')
    USER_LOGIN = (By.XPATH, '//span[text()="alzatestuser@gmail.com"]')
