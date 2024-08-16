from selenium.webdriver.common.by import By


class ContactLocators:
    PRODUCT = (By.XPATH, '//a[@class="navigationItem commodity ajax"]')
    ORDER = (By.XPATH, '//a[@class="navigationItem order"]')
    CLAIMS = (By.XPATH, '//a[@class="navigationItem reclamation"]')
    SERVICE = (By.XPATH, '//a[@class="navigationItem service ajax"]')
    OTHER = (By.XPATH, '//a[@class="navigationItem other ajax"]')

