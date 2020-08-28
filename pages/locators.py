from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    #locators for login form
    LOGIN_FORM = (By.CSS_SELECTOR, "login_form")
    #locators for registerion form
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

