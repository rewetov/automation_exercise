from time import time

from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        print("should_be_login_page")
        self.should_be_login_url()
        self.should_be_login_block_on_page()
        self.should_be_registration_block_on_page()


    def should_be_login_url(self):
        print("should_be_login_url")
        print("Текущий URL: ", self.browser.current_url)
        assert "login" in self.browser.current_url, "Не найдено слово 'login' в текущем URL открытой страницы"

    def should_be_login_block_on_page(self):
        print("should_be_login_block_on_page")
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Логин форма не найдена. Не найден локатор LOGIN_FORM"

    def should_be_registration_block_on_page(self):
        print("should_be_registration_block_on_page")
        assert self.is_element_present(*LoginPageLocators.SIGNUP_FORM), "Логин форма не найдена. Не найден локатор SIGNUP_FORM"

    def input_username(self, username):
        print("input_username")
        name = "Alex" + str(time.time())
        self.is_element_present(*LoginPageLocators.INPUT_EMAIL).send_keys(name)

    def input_email(self, email):
        print("input_email")
        email = str(time.time()) + "@fakemail.org"
        self.is_element_present(*LoginPageLocators.INPUT_EMAIL).send_keys(email)

    def click_signup_button(self):
        print("click_signup_button")
