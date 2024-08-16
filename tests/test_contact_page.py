import time
import allure
from elements import HeaderElement
from pages.contact_page import ContactPage
from pages.main_page import MainPage


@allure.feature('Contact page')
def test_invalid_login_form(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.go_to_contacts()
    contact_page = ContactPage(driver)
    contact_page.assert_that_contact_page_is_opened()
