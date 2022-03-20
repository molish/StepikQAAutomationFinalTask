from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, 'a[href*="/basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_INPUT_PASSWORD1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_INPUT_PASSWORD2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "button[value='Register']")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BOOK_NAME_ADDED = (By.CSS_SELECTOR, "div.alertinner strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    BOOK_PRICE_ADDED = (By.CSS_SELECTOR, "div.alertinner p strong")
    INNER_ALERTS = (By.CSS_SELECTOR, "div.alertinner")


class BasketPageLocators():
    BASKET_IS_EMPTY_TEXT = (By.XPATH, '//div[@id="content_inner"]/p[contains(text(), "Ваша корзина пуста")]')
