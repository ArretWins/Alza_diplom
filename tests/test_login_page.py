import time

from elements import HeaderElement
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_invalid_login_form(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()
    header_element = HeaderElement(driver)
    header_element.open_login()
    login_page = LoginPage(driver)
    login_page.assert_fill_invalid_login_form()


def test_miss_password_login_form(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()
    header_element = HeaderElement(driver)
    header_element.open_login()
    login_page = LoginPage(driver)
    login_page.assert_miss_password_login_form()
    login_page.save_screenshot("empty_password.png")


def test_miss_email_login_form(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()
    header_element = HeaderElement(driver)
    header_element.open_login()
    login_page = LoginPage(driver)
    login_page.assert_miss_email_login_form()
    login_page.save_screenshot("empty_mail.png")
