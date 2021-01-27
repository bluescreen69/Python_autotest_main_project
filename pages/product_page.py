from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        print("button=", button)
        button.click()
    
    def book_with_correct_name_and_price_should_be_in_the_basket(self):
        message = self.browser.find_elements(*ProductPageLocators.MESSAGE)
        book_name = self.browser.find_element(*ProductPageLocators.NAME)
        print(book_name.text)
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        book_name_in_the_basket = message[0]
        basket_price = message[2]
        print(book_name_in_the_basket.text)
        assert book_name.text in book_name_in_the_basket.text, "Book name is not correct!"
        assert price.text in basket_price.text, "Book price is not correct!"
