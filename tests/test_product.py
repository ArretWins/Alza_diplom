import allure

from pages.product_page import ProductPage
from pages.main_page import MainPage


@allure.feature('Product page')
class TestProduct:

    @allure.title('Open product page')
    def test_product_page(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.open_first_product()

        product_page = ProductPage(driver)
        product_page.assert_that_productpage_is_opened()

    @allure.title('Test of product name')
    def test_product_name(self, driver):
        main_page = MainPage(driver)
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        name_from_main_page = main_page.get_name_of_first_product()
        main_page.open_first_product()

        product_page = ProductPage(driver)
        name_from_product_page = product_page.get_product_name()
        product_page.assert_that_names_are_equals(name_from_main_page, name_from_product_page)

    @allure.title('Test comment button')
    def test_comment_button(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.open_first_product()

        product_page = ProductPage(driver)
        product_page.click_comment_button()
        product_page.assert_that_login_is_opened()

    @allure.title('Test buy button')
    def test_buy_button(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.open_first_product()

        product_page = ProductPage(driver)
        product_page.buy_product()
        product_page.assert_cross_sell_page()

    @allure.title('Test delivery search button')
    def test_delivery_search(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.open_first_product()

        product_page = ProductPage(driver)
        product_page.click_to_delivery()
        product_page.search_address()
        product_page.choose_address()
        product_page.assert_that_delivery_search_works()

    @allure.title('Test of compare')
    def test_compare_items(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.open_first_product()

        product_page = ProductPage(driver)
        product_page.click_to_compare()
        product_page.assert_compare_message()

    @allure.title('Test of photos')
    def test_photos(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.open_first_product()

        product_page = ProductPage(driver)
        product_page.click_photos()
        product_page.open_photos()
        product_page.assert_that_photos_are_opened()

    @allure.title('Test of discussions')
    def test_discussions(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.open_first_product()

        product_page = ProductPage(driver)
        product_page.click_discussions()
        product_page.assert_that_discussions_are_opened()

    @allure.title('Test of answers')
    def test_answers(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_laptops()
        main_page.open_first_product()

        product_page = ProductPage(driver)
        product_page.click_discussions()
        product_page.fill_discussions_input()
        product_page.click_to_answer()
        product_page.assert_that_answer_is_opened()
