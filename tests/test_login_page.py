import allure
from elements import HeaderElement
from pages.login_page import LoginPage
from pages.main_page import MainPage


@allure.feature('Login Page')
class TestLogin:

    @allure.title('Invalid login form')
    def test_invalid_login_form(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()
        main_page.get_context_menu()

        header_element = HeaderElement(driver)
        header_element.open_login()

        login_page = LoginPage(driver)
        login_page.assert_fill_invalid_login_form()

    @allure.title('Correct login')
    def test_correct_login(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()
        main_page.get_context_menu()

        header_element = HeaderElement(driver)
        header_element.open_login()

        login_page = LoginPage(driver)
        login_page.send_email()
        login_page.send_password()
        login_page.login()
        main_page.get_context_menu()
        header_element.assert_that_login_correct()

    @allure.title('Miss password')
    def test_miss_password_login_form(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()
        main_page.get_context_menu()

        header_element = HeaderElement(driver)
        header_element.open_login()

        login_page = LoginPage(driver)
        login_page.assert_miss_password_login_form()

    @allure.title('Miss email')
    def test_miss_email_login_form(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()
        main_page.get_context_menu()

        header_element = HeaderElement(driver)
        header_element.open_login()

        login_page = LoginPage(driver)
        login_page.assert_miss_email_login_form()

    @allure.feature('Social buttons login')
    def test_social_buttons(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()
        main_page.get_context_menu()

        header_element = HeaderElement(driver)
        header_element.open_login()

        login_page = LoginPage(driver)
        login_page.assert_login_social_buttons()

    @allure.feature('Work of social buttons')
    def test_work_of_social_buttons(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()
        main_page.get_context_menu()

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
