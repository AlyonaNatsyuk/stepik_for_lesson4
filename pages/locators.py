from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    EMAIL_LOGIN = (By.CSS_SELECTOR, "input[id='id_login-username']")
    PASS_LOGIN = (By.CSS_SELECTOR, "input[id='id_login-password']")
    EMAIL_REG = (By.CSS_SELECTOR, "input[id='id_registration-email']")
    PASS_REG1 = (By.CSS_SELECTOR, "input[id='id_registration-password1']")
    PASS_REG2 = (By.CSS_SELECTOR, "input[id='id_registration-password2']")
