import time

import allure
from elements.header_element import HeaderElement
from pages.basket_page import BasketPage
from pages.delivery_page import DeliveryPage
from pages.main_page import MainPage


@allure.feature('Delivery')
def test_that_delivery_page_is_opened(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.open_delivery_page()
    delivery_page = DeliveryPage(driver)
    delivery_page.close_dialog_window()
    delivery_page.assert_that_delivery_is_opened()


@allure.feature('Delivery')
def test_alzabox(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.open_delivery_page()
    delivery_page = DeliveryPage(driver)
    delivery_page.close_dialog_window()
    delivery_page.open_alzabox()
    delivery_page.buy_alza_box()
    delivery_page.assert_that_method_is_checked()


@allure.feature('Delivery')
def test_showroom(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.open_delivery_page()
    delivery_page = DeliveryPage(driver)
    delivery_page.close_dialog_window()
    delivery_page.open_showroom()
    delivery_page.confirm_showroom()
    delivery_page.assert_that_method_is_checked()


@allure.feature('Delivery')
def test_markets(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.open_delivery_page()
    delivery_page = DeliveryPage(driver)
    delivery_page.close_dialog_window()
    delivery_page.open_markets()
    delivery_page.buy_in_market()
    delivery_page.assert_that_method_is_checked()


@allure.feature('Delivery')
def test_markets_and_boxes(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.open_delivery_page()
    delivery_page = DeliveryPage(driver)
    delivery_page.close_dialog_window()
    delivery_page.open_markets_and_boxes()
    delivery_page.buy_in_markets_and_boxes()
    delivery_page.assert_that_method_is_checked()


@allure.feature('Delivery')
def test_delivery_to_address(driver):
    main_page = MainPage(driver)
    main_page.buy_first_product()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.open_delivery_page()
    delivery_page = DeliveryPage(driver)
    delivery_page.close_dialog_window()
    delivery_page.open_delivery_to_address()
    delivery_page.choose_address()
    delivery_page.confirm_delivery_time()
    delivery_page.assert_that_method_is_checked()
