from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_the_basket(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        add_to_cart_button.click()

    def should_be_success_message(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), "Success message doesn't correct"

    def should_be_message_product_added(self):
        product_name_on_the_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_THE_PAGE).text
        product_name_on_the_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_THE_MESSAGE).text
        assert product_name_on_the_page == product_name_on_the_message, "Product names don't match"

    def should_be_message_price_added(self):
        price_on_the_page = self.browser.find_element(*ProductPageLocators.PRICE_ON_THE_PAGE).text
        price_on_the_message = self.browser.find_element(*ProductPageLocators.PRICE_ON_THE_MESSAGE).text
        assert price_on_the_message == price_on_the_page, "Prices don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_the_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message should not disappear"
