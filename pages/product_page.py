from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_on_the_button_add(self):
        link = self.is_element_present(*ProductPageLocators.BUTTON_ADD)
        link.click()
