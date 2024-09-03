from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        with allure.step("Open page"):
            self.driver.get(url)

    def get_element(self, locator):
        with allure.step("Get element"):
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            return element

    def click(self, locator,  force=False):
        with allure.step("Click element on element"):
            element = self.get_element(locator)
            if force:
                self.driver.execute_script("arguments[0].click();", element)
            element.click()

    def get_text(self, locator):
        with allure.step("Get text of element"):
            element = self.get_element(locator)
            return element.text

    def get_price(self, locator):
        with allure.step("Get price of element"):
            element = self.get_element(locator)
            text_element = element.text
            stripprice = text_element.split()
            stripprice.pop(-1)
            combined_string = ''.join(stripprice)
            result = int(combined_string)
            return result

    def get_href(self, locator):
        with allure.step("Get href of element"):
            return self.get_element(locator).get_attribute('href')

    def fill(self, locator, text):
        with allure.step("Fill element with text"):
            element = self.get_element(locator)
            element.send_keys(text)

    def checkbox(self, locator):
        with allure.step("Checkbox element"):
            element = self.get_element(locator)
            element.click()

    def input_text(self, locator, text):
        with allure.step("Input text of element"):
            element = self.get_element(locator)
            element.send_keys(text)

    def save_screenshot(self, name):
        with allure.step("Save screenshot"):
            self.driver.save_screenshot(name)

    def add_cookies(self, name, value):
        with allure.step("Add cookies"):
            cookie = {'name': name, 'value': value}
            self.driver.add_cookie(cookie)

    def delete_cookies(self, name, value):
        with allure.step("Delete cookies"):
            cookie = {'name': name, 'value': value}
            self.driver.remove_cookie(cookie)

    def get_cookies(self, name):
        with allure.step("Get cookies"):
            cookies = self.driver.get_cookies()
            for cookie in cookies:
                if cookie['name'] == name:
                    return cookie['value']

    def wait_for(self, locator, time_out=10):
        try:
            element = WebDriverWait(self.driver, time_out).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            assert False, f"Element {locator} does not find"

    def select_by_visible_text(self, locator, text):
        with allure.step("Select element by visible text"):
            select = Select(self.get_element(locator))
            select.select_by_visible_text(text)

    def select_by_value(self, locator, value):
        with allure.step("Select element by value"):
            select = Select(self.get_element(locator))
            select.select_by_value(value)

    def click_back_button(self):
        with allure.step('Navigate back'):
            self.driver.back()
