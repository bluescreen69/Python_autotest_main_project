from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators:
    BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-title")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages")
