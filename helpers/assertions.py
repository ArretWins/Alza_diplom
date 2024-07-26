from selenium.webdriver.common.by import By


class Assertions:

    def __init__(self, driver):
        self.driver = driver

    def assert_that_text_is_visible(self, locator, text, by=By.XPATH):
        el = self.driver.find_element(by, locator)
        assert el.text == text

    def assert_that_element_is_visible(self, locator, by=By.XPATH):
        assert self.driver.find_element(by, locator)

    def assert_that_attribute_is_visible(self, locator, attribute, value, by=By.XPATH):
        el = self.driver.find_element(by, locator)
        assert el.get_attribute(attribute) == value

    def assert_that_attribute_class_is_visible(self, locator, value, by):
        self.assert_that_attribute_is_visible(locator, 'class', value, by)