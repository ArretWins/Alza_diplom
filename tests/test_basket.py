import time

import allure
from elements.header_element import HeaderElement
from pages.basket_page import BasketPage
from pages.main_page import MainPage


@allure.feature('Basket')
class TestBasket:

    @allure.title('Open basket')
    def test_basket(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        name_from_main = main_page.get_name_of_first_product()
        main_page.add_item_to_basket()
        main_page.assert_that_item_added()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.assert_that_names_are_equals(name_from_main)

    @allure.title('Price')
    def test_price(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        price_from_page = main_page.get_price_of_product()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        price_from_basket = basket_page.get_price_of_product()
        basket_page.assert_that_prices_are_equals(price_from_basket, price_from_page)

    @allure.title('Plus button')
    def test_plus_button(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.assert_plus_button_is_worked()

    @allure.title('Minus button')
    def test_minus_button(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.assert_minus_button_is_worked()

    @allure.title('Plus button')
    def test_disabled_plus_button(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        limit = basket_page.get_limit_of_product()
        time.sleep(1)
        if limit:
            basket_page.assert_disabled_plus_button()
        else:
            basket_page.assert_that_basket_is_not_empty()

    @allure.title('Delete product')
    def test_delete_product(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.click_minus_button()
        basket_page.delete_product()
        basket_page.assert_that_product_deleted()

    @allure.title('Cancel of deleting product')
    def test_cancel_of_deleting_product(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.click_minus_button()
        basket_page.cancel_delete_product()
        basket_page.assert_that_basket_is_not_empty()
