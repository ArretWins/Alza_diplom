import time
import allure
from elements import HeaderElement
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature('Login Page')
def test_invalid_login_form(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()
    header_element = HeaderElement(driver)
    header_element.open_login()
    login_page = LoginPage(driver)
    login_page.assert_fill_invalid_login_form()


@allure.feature('Login Page')
def test_miss_password_login_form(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()
    header_element = HeaderElement(driver)
    header_element.open_login()
    login_page = LoginPage(driver)
    login_page.assert_miss_password_login_form()
    # login_page.save_screenshot("empty_password.png")


@allure.feature('Login Page')
def test_miss_email_login_form(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()
    header_element = HeaderElement(driver)
    header_element.open_login()
    login_page = LoginPage(driver)
    login_page.assert_miss_email_login_form()
    # login_page.save_screenshot("empty_mail.png")


@allure.feature('Login Page')
def test_social_buttons(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()
    header_element = HeaderElement(driver)
    header_element.open_login()
    login_page = LoginPage(driver)
    login_page.assert_login_social_buttons()


@allure.feature('Login Page')
def test_work_of_social_buttons(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()
    header_element = HeaderElement(driver)
    header_element.open_login()
    login_page = LoginPage(driver)
    login_page.login_by_google()
    login_page.assert_that_google_login_works()
    login_page.back_button()
    login_page.login_by_apple()
    login_page.assert_that_apple_login_works()
    login_page.back_button()
    login_page.assert_login_social_buttons()
