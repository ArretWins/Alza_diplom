from selenium.webdriver.common.by import By


class MainLocators:
    FIRST_ITEM_BUTTON = (By.XPATH, '//button[@data-testid="itemButton"][1]')
    LAPTOPS = (By.XPATH, '//a[contains(text(), "a notebooky")]')
    # FIRST_ITEM_BUTTON = (By.XPATH, '//*[@id="ltp"]/div[2]/div/div/div[1]/'
    #                                'div/div/div/swiper-container/swiper-slide[3]/div/button')
    FIRST_ITEM_NAME = (By.XPATH, '//a[@class="carousel0-alz-34"][1]')
    ITEM_TO_BASKET = (By.XPATH, '//span[@class="carousel0-alz-43"]')
    PRIVACY_WINDOW = (By.XPATH, '//a[@data-action-id-value="0"]')
    LANGUAGE_SWITCHER = (By.XPATH, '//span[@data-testid="headerLanguageSwitcher"]')
    STATUS_LANGUAGE = (By.XPATH, '//h2[contains(@class,"header-alz-87")]')
    ENGLISH_BUTTON = (By.XPATH, '//span[text()="English"]')
    SLOVAK_BUTTON = (By.XPATH, '//span[contains(text(), "Sloven")]')
    CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(), "Confirm")]')
    MOBILY = (By.XPATH, '//a[contains(text(),"Mobily")]')
    PHONES = (By.XPATH, '//a[contains(text(),"Phones, Smart Watches")]')
    FIRST_PRODUCT = (By.XPATH, '//div[@class="carousel0-alz-35"]')
