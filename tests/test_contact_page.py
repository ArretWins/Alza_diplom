import time
import allure
from elements import HeaderElement
from pages.contact_page import ContactPage
from pages.main_page import MainPage


@allure.feature('Contact page')
def test_contact_page(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.go_to_contacts()
    contact_page = ContactPage(driver)
    contact_page.assert_that_contact_page_is_opened()


@allure.feature('Contact page')
def test_answer(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()
    main_page.go_to_contacts()
    contact_page = ContactPage(driver)
    contact_page.click_product()
    contact_page.search_input()
    contact_page.search_discussion()
    contact_page.click_post()
    contact_page.assert_answer()


@allure.feature('Contact page')
def test_alza_plus(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()
    main_page.go_to_contacts()
    contact_page = ContactPage(driver)
    contact_page.click_service()
    contact_page.click_alza_plus()
    contact_page.scroll()
    contact_page.click_alza_list()
    contact_page.click_alza_href()
    contact_page.assert_that_alza_plus_page_is_opened()
