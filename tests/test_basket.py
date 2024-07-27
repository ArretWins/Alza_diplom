import time
import allure
from elements.header_element import HeaderElement
from pages.basket_page import BasketPage
from pages.main_page import MainPage


@allure.feature('Basket')
@allure.story('Exists')
def test_basket(driver):
    with allure.step('Open main page'):
        main_page = MainPage(driver)
        main_page.open()
    main_page.close_privacy_window()
    with allure.step('Get product to basket'):
        main_page.assert_item_to_basket()
        href_from_main = main_page.get_href_of_first_product()
    with allure.step('Open basket'):
        header_element = HeaderElement(driver)
        header_element.open_basket()

    basket_page = BasketPage(driver)
    href_from_basket = basket_page.get_href_of_main_product()
    with allure.step('Check that product is current'):
        assert href_from_main == href_from_basket


@allure.feature('Basket')
@allure.story('Exists')
def test_price(driver):
    with allure.step('Open main page'):
        main_page = MainPage(driver)
        main_page.open()
    main_page.close_privacy_window()
    with allure.step('Get product to basket'):
        main_page.assert_item_to_basket()
    with allure.step('Open basket'):
        header_element = HeaderElement(driver)
        header_element.open_basket()

    basket_page = BasketPage(driver)
    price = basket_page.get_price_of_product()
    with allure.step('Check that basket is not empty'):
        basket_page.assert_that_basket_is_not_empty()


@allure.feature('Basket')
@allure.story('Count')
def test_plus_button(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.close_privacy_window()
    main_page.assert_item_to_basket()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.assert_plus_button_is_worked()
    basket_page.save_screenshot('plus_button.png')


@allure.feature('Basket')
@allure.story('Count')
def test_minus_button(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.close_privacy_window()
    main_page.assert_item_to_basket()
    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.assert_minus_button_is_worked()
    # basket_page.save_screenshot('minus_button.png')
