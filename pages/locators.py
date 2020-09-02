from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    #locators for login form
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    #locators for registerion form
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success:nth-child(1)')
    PRODUCT_NAME_ON_THE_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) > .alertinner strong')
    PRODUCT_NAME_ON_THE_PAGE = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE_ON_THE_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) > .alertinner strong')
    PRICE_ON_THE_PAGE = (By.CSS_SELECTOR, 'p.price_color')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators:
    BUTTON_BASKET = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    TEXT_ON_THE_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
