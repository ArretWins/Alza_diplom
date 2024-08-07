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
    delivery_page.open_alza_box()
    time.sleep(2)
    delivery_page.assert_that_delivery_is_opened()
