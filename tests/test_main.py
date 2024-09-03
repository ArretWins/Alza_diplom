import allure

from elements import HeaderElement
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_page import OrdersPage


@allure.feature('Main page')
class TestMain:

    @allure.title('Open main page')
    def test_open_website(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()

    @allure.title('Open orders')
    def test_open_orders(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()

        header_element = HeaderElement(driver)
        header_element.open_orders()

        orders_page = OrdersPage(driver)
        orders_page.assert_that_orderspage_is_opened()

    @allure.title('Open basket')
    def test_open_basket(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.assert_that_basket_is_opened()

    @allure.title('Open context menu')
    def test_context_menu(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()
        main_page.click_context_menu()
        main_page.assert_context_menu()

    @allure.title('Open login')
    def test_login(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.assert_that_mainpage_is_opened()

        main_page.click_context_menu()
        header_element = HeaderElement(driver)
        header_element.open_login()
        login_page = LoginPage(driver)
        login_page.assert_that_login_is_opened()

    @allure.title('Change language')
    def test_change_language(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.change_language()
        main_page.assert_that_mainpage_is_opened()

    @allure.story('Back change of language')
    def test_that_language_is_changed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.change_language()
        main_page.assert_that_language_switched_to_english()
        main_page.change_language()
        main_page.assert_that_language_switched_to_slovak()
