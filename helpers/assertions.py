from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Assertions:

    def __init__(self, driver):
        self.driver = driver

    def assert_that_text_is_visible(self, locator, text, by=By.XPATH):
        el = self.driver.find_element(by, locator)
        assert el.text == text

    def assert_that_element_is_visible(self, locator, by=By.XPATH):
        assert self.driver.find_element(by, locator)

    def assert_that_element_is_invisible(self, locator):
        by, value = locator
        try:
            self.driver.find_element(by, value)
            assert False, f"Element with locator '{value}' was found, but it should be invisible."
        except NoSuchElementException:
            pass

    def assert_that_attribute_is_visible(self, locator, attribute, value, by=By.XPATH):
        el = self.driver.find_element(by, locator)
        assert el.get_attribute(attribute) == value

    def assert_that_attribute_class_is_visible(self, locator, value, by):
        self.assert_that_attribute_is_visible(locator, 'class', value, by)

    def assert_that_element_is_not_clickable(self, locator, by=By.XPATH):
        with allure.step("Check element is not clickable"):
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, locator)))
                assert False, "Element is clickable"
            except TimeoutException:
                element = self.driver.find_element(by, locator)
                assert not element.is_enabled() or not element.is_displayed(), "Element is still interactable"
