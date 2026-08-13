from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_block_on_page()
        self.should_be_registration_block_on_page()


    def should_be_login_url(self):
        print("Текущий URL: ", self.browser.current_url)
        assert "login" in self.browser.current_url, "Не найдено слово 'login' в текущем URL открытой страницы"

    def should_be_login_block_on_page(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Логин форма не найдена. Не найден локатор LOGIN_FORM"

    def should_be_registration_block_on_page(self):
        assert self.is_element_present(*LoginPageLocators.SIGNUP_FORM), "Логин форма не найдена. Не найден локатор SIGNUP_FORM"

    def input_username(self, name):
        self.browser.find_element(*LoginPageLocators.INPUT_NAME).send_keys(name)

    def input_email(self, email):
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(email)

    def click_signup_button(self):
        self.browser.find_element(*LoginPageLocators.BUTTON_SIGNUP).click()
