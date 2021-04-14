from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_not_be_items_in_basket()
        self.should_be_message_about_empty_basket()

    def should_not_be_items_in_basket(self):
       assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Your basket contains some items!"


    def should_be_message_about_empty_basket(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        assert basket_message, "Your basket is not empty!"
        