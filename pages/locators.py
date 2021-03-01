from selenium.webdriver.common.by import By

# class MainPageLocators:
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
