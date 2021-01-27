from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    time.sleep(4)
    page.book_with_correct_name_and_price_should_be_in_the_basket()
