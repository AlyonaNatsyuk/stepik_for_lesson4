from .pages.product_page import ProductPage
import time


def test_guest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_in_the_button()
    page.solve_quiz_and_get_code()

