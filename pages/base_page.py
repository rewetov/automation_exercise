
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): 
        self.browser.get(self.url)

    #возвращает True или False в зависимости от того найден элемент или нет
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    #возвращает текст элемента или False в случае неудачи
    def is_element_text(self, how, what):
        try:
            textelement = self.browser.find_element(how, what).text
        except (NoSuchElementException):
            return False
        return textelement

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.SIGNUP_LOGIN_NAVBAR_BUTTON).click()

    def should_be_loged_in(self, name):
        username = self.browser.find_element(*BasePageLocators.LOGGED_IN_AS).text
        assert username == name, f"Ошибка! Ожидалось имя {name}, а отображается {username}."

    def delete_account(self):
        self.browser.find_element(*BasePageLocators.DELETE_ACCOUNT_BUTTON).click()

    def go_to_contact_us_page(self):
        self.browser.find_element(*BasePageLocators.CONTACTUS_NAVBAR_BUTTON).click()

    def go_to_t_cases_page(self):
        self.browser.find_element(*BasePageLocators.TESTCASES_NAVBAR_BUTTON).click()

    def go_to_products_page(self):
        self.browser.find_element(*BasePageLocators.PRODUCT_NAVBAR_BUTTON).click()
