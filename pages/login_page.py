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

    def input_username_signup(self, name):
        self.browser.find_element(*LoginPageLocators.NAME_SIGNUP_INPUT).send_keys(name)

    def input_email_signup(self, email):
        self.browser.find_element(*LoginPageLocators.EMAIL_SIGNUP_INPUT).send_keys(email)

    def click_signup_button(self):
        self.browser.find_element(*LoginPageLocators.SIGNUP_BUTTON).click()

    def input_email_login(self, email):
        self.browser.find_element(*LoginPageLocators.EMAIL_LOGIN_INPUT).send_keys(email)

    def input_password_login(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD_LOGIN_INPUT).send_keys(password)

    def click_login_button(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_incorrect_email_or_password_message(self):
        error_message = self.browser.find_element(*LoginPageLocators.INCORRECT_EMAIL_OR_PASSWORD_LABEL).text
        assert error_message == "Your email or password is incorrect!", f"Ошибка! Ожидается текст 'Your email or password is incorrect!', а выводится {error_message}."

    def should_be_email_address_already_exist_message(self):
        error_message = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_ALREADY_EXIST_LABEL).text
        assert error_message == "Email Address already exist!", f"Ошибка! Email Address already exist!', а выводится {error_message}."