import time

import allure
from elements.header_element import HeaderElement
from pages.basket_page import BasketPage
from pages.main_page import MainPage


@allure.feature('Basket')
def test_basket(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    name_from_main = main_page.get_name_of_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    name_from_basket = basket_page.get_name_of_main_product()
    basket_page.assert_that_names_are_equals(name_from_main, name_from_basket)


@allure.feature('Basket')
def test_price(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    price_from_page = main_page.get_price_of_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    price_from_basket = basket_page.get_price_of_product()
    basket_page.assert_that_prices_are_equals(price_from_basket, price_from_page)


@allure.feature('Basket')
def test_plus_button(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.assert_plus_button_is_worked()


@allure.feature('Basket')
def test_minus_button(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.assert_minus_button_is_worked()


@allure.feature('Basket')
def test_disabled_plus_button(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    limit = basket_page.get_limit_of_product()
    time.sleep(1)
    if limit:
        basket_page.assert_disabled_plus_button()
    else:
        basket_page.assert_that_basket_is_not_empty()


@allure.feature('Basket')
def test_delete_product(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.click_minus_button()
    basket_page.delete_product()
    basket_page.assert_that_product_deleted()


@allure.feature('Basket')
def test_cancel_of_delete_product(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.click_minus_button()
    basket_page.cancel_delete_product()
    basket_page.assert_that_basket_is_not_empty()
