from selenium.webdriver.common.by import By


class ContactLocators:
    PRODUCT = (By.XPATH, '//a[@class="navigationItem commodity ajax"]')
    ORDER = (By.XPATH, '//a[@class="navigationItem order"]')
    CLAIMS = (By.XPATH, '//a[@class="navigationItem reclamation"]')
    SERVICE = (By.XPATH, '//a[@class="navigationItem service ajax"]')
    OTHER = (By.XPATH, '//a[@class="navigationItem other ajax"]')

    PRODUCT_INPUT = (By.XPATH, '//input[@id="commodityToFind"]')
    CHOOSE_PRODUCT = (By.XPATH, '//span[@class="commodityName"]')
    DISCUSSION_SEARCH = (By.XPATH, '//input[@id="commodityDiscussionSearchText"]')
    POST_CONTAINER = (By.XPATH, '//p[contains(text(), "schopny otvorit")]')
    ANSWER = (By.XPATH, '//p[contains(text(), "ho na tomto MacBooku")]')
