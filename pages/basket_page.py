from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ON_THE_BASKET), \
            "The basket isn't empty"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items on the basket"
