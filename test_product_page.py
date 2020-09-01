from .pages.product_page import ProductPage

def test_guest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_the_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_message_product_added()
    page.should_be_message_price_added()
