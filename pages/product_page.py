from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_to_basket_btn.click()

    def get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def get_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def wait_adding_alerts(self):
        WebDriverWait(driver=self.browser, timeout=20).until(EC.presence_of_element_located((ProductPageLocators.INNER_ALERTS)))

    def check_added_book_name(self, name):
        added_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED).text
        assert name == added_name, "Name of added book different from book tha was chosen"

    def check_added_book_price(self, price):
        added_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ADDED).text
        assert price == added_price, "Price of added book different from book tha was chosen"

    def is_not_success_message_presented(self):
        return self.is_not_element_present(*ProductPageLocators.INNER_ALERTS)

    def is_success_message_disappiared(self):
        return self.is_disappeared(*ProductPageLocators.INNER_ALERTS)