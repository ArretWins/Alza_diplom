import allure
from elements.header_element import HeaderElement
from pages.basket_page import BasketPage
from pages.delivery_page import DeliveryPage
from pages.main_page import MainPage


@allure.feature('Delivery')
class TestDelivery:

    @allure.title("Open delivery page")
    def test_that_delivery_page_is_opened(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.open_delivery_page()
        delivery_page = DeliveryPage(driver)
        delivery_page.assert_that_delivery_is_opened()

    @allure.title('Test alzabox')
    def test_alzabox(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.open_delivery_page()
        delivery_page = DeliveryPage(driver)
        delivery_page.open_alzabox()
        delivery_page.buy_alza_box()
        delivery_page.assert_that_alzabox_is_checked()

    @allure.title('Test showroom')
    def test_showroom(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.open_delivery_page()
        delivery_page = DeliveryPage(driver)
        delivery_page.open_showroom()
        delivery_page.confirm_showroom()
        delivery_page.assert_that_showroom_is_checked()

    @allure.title('Test markets')
    def test_markets(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.open_delivery_page()
        delivery_page = DeliveryPage(driver)
        delivery_page.open_markets()
        delivery_page.buy_in_market()
        delivery_page.assert_that_market_is_checked()

    @allure.title('Test markets and boxes')
    def test_markets_and_boxes(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.open_delivery_page()
        delivery_page = DeliveryPage(driver)
        delivery_page.open_markets_and_boxes()
        delivery_page.buy_in_markets_and_boxes()
        delivery_page.assert_that_markets_and_boxes_is_checked()

    @allure.title('Test delivery')
    def test_delivery_to_address(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.add_item_to_basket()

        header_element = HeaderElement(driver)
        header_element.open_basket()

        basket_page = BasketPage(driver)
        basket_page.open_delivery_page()
        delivery_page = DeliveryPage(driver)
        delivery_page.open_delivery_to_address()
        delivery_page.choose_address()
        delivery_page.confirm_delivery_time()
        delivery_page.assert_that_delivery_to_address_is_checked()
