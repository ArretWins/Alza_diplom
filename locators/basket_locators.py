from selenium.webdriver.common.by import By


class BasketLocators:
    BASKET_STEPS = (By.XPATH, '//div[@data-testid="basketSteps"]')
    BASKET_TAB = (By.XPATH, '//div[@class="basketTab"]')
    BACK_TO_MAIN_BUTTON = (By.XPATH, '//a[@class="btnx normal grey arrowedLeft"]')
    EMPTY_BASKET = (By.XPATH, '//div[@id="blocke"]')
    MAIN_ITEM_NAME = (By.XPATH, '//a[@class="mainItem"]')

    PLUS_BUTTON = (By.XPATH, '//div[@class="countPlus"]')
    MINUS_BUTTON = (By.XPATH, '//div[@class="countMinus"]')
    EDIT_FIELD = (By.XPATH, '//div[@class="countEdit"]')
    LAST_PRICE = (By.XPATH, '//span[@class="last price"]')

    PLUS_DISABLED = (By.XPATH, '//div[@class="countPlus disabled"]')
    DELETE_PRODUCT = (By.XPATH, '//span[@class="btnx normal green ok"]')
    CANCEL_DELETE_PRODUCT = (By.XPATH, '//span[@class="btnx normal grey storno"]')

    EMPTY_IMAGE = (By.XPATH, '//img[@class="emptyImage"]')

    CONTINUE_BUTTON = (By.XPATH, '//div[@id="blockBtnRight"]')
