from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_the_basket(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        add_to_cart_button.click()

    def should_be_success_message(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), "Success message doesn't correct"

    def should_be_message_product_added(self):
        product_name_on_the_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_THE_PAGE)
        product_name_on_the_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_THE_MESSAGE)
        assert product_name_on_the_message == product_name_on_the_page, "Product names don't match"

    def should_be_message_price_added(self):
        price_on_the_page = self.browser.find_element(*ProductPageLocators.PRICE_ON_THE_PAGE)
        price_on_the_message = self.browser.find_element(*ProductPageLocators.PRICE_ON_THE_MESSAGE)
        assert price_on_the_message == price_on_the_page, "Prices don't match"
