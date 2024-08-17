import time

import allure
from elements.header_element import HeaderElement
from pages.product_page import ProductPage
from pages.main_page import MainPage


@allure.feature('Product page')
def test_product_page(driver):
    main_page = MainPage(driver)
    main_page.to_product_page()
    product_page = ProductPage(driver)
    product_page.assert_that_productpage_is_opened()


@allure.feature('Product page')
def test_product_name(driver):
    main_page = MainPage(driver)
    name_from_main_page = main_page.to_product_page()
    product_page = ProductPage(driver)
    name_from_product_page = product_page.get_product_name()
    product_page.assert_that_names_are_equals(name_from_main_page, name_from_product_page)


@allure.feature('Product page')
def test_comment_button(driver):
    main_page = MainPage(driver)
    main_page.to_product_page()
    product_page = ProductPage(driver)
    product_page.close_privacy_window()
    product_page.click_comment_button()
    # time.sleep(1)
    product_page.assert_that_login_is_opened()


@allure.feature('Product page')
def test_buy_button(driver):
    main_page = MainPage(driver)
    main_page.to_product_page()
    product_page = ProductPage(driver)
    product_page.buy_product()
    product_page.assert_cross_sell_page()


@allure.feature('Product page')
def test_delivery_search(driver):
    main_page = MainPage(driver)
    main_page.to_product_page()

    product_page = ProductPage(driver)
    product_page.click_to_delivery()
    product_page.search_address()
    product_page.choose_address()
    product_page.assert_that_delivery_search_works()


@allure.feature('Product page')
def test_compare_items(driver):
    main_page = MainPage(driver)
    main_page.to_product_page()

    product_page = ProductPage(driver)
    product_page.click_to_compare()
    product_page.assert_compare_message()


@allure.feature('Product page')
def test_photos(driver):
    main_page = MainPage(driver)
    main_page.to_product_page()

    product_page = ProductPage(driver)
    product_page.click_photos()
    product_page.open_photos()
    product_page.assert_that_photos_are_opened()


@allure.feature('Product page')
def test_discussions(driver):
    main_page = MainPage(driver)
    main_page.to_product_page()

    product_page = ProductPage(driver)
    product_page.click_discussions()
    product_page.assert_that_discussions_are_opened()


@allure.feature('Product page')
def test_answers(driver):
    main_page = MainPage(driver)
    main_page.to_product_page()

    product_page = ProductPage(driver)
    product_page.click_discussions()
    product_page.fill_discussions_input()
    product_page.click_to_answer()
    product_page.assert_that_answer_is_opened()