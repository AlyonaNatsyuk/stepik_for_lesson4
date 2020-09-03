import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Word-login isn't in the url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Page hasn't login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Page hasn't register form"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        email_for_reg = self.browser.find_element(*LoginPageLocators.EMAIL)
        email = email + str(time.time()) + "@test.com"
        email_for_reg.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password = password + "Nats1996*"
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        password2.send_keys(password)
        button_reg = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        button_reg.click()
