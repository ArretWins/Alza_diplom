from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

        return element

    def click(self, locator,  force=False):
        element = self.get_element(locator)
        if force:
            self.driver.execute_script("arguments[0].click();", element)
        element.click()

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def fill(self, locator, text):
        element = self.get_element(locator)
        element.send_keys(text)

    def checkbox(self, locator):
        element = self.get_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.get_element(locator)
        element.send_keys(text)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def add_cookies(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie(cookie)

    def delete_cookies(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.remove_cookie(cookie)

    def get_cookies(self, name):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == name:
                return cookie['value']

    def select_by_visible_text(self, locator, text):
        select = Select(self.get_element(locator))
        select.select_by_visible_text(text)

    def select_by_value(self, locator, value):
        select = Select(self.get_element(locator))
        select.select_by_value(value)

