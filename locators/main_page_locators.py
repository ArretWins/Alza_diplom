from selenium.webdriver.common.by import By


class MainLocators:
    FIRST_ITEM_BUTTON = (By.XPATH, '//button[@data-testid="itemButton"][1]')
    FIRST_ITEM_NAME = (By.XPATH, '//a[@class="carousel0-alz-34"][1]')
    ITEM_TO_BASKET = (By.XPATH, '//span[@class="carousel0-alz-43"]')
    PRIVACY_WINDOW = (By.XPATH, '//a[@data-action-id-value="0"]')

