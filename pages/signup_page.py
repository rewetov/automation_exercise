from selenium.webdriver.support.select import Select

from .base_page import BasePage
from .locators import SignUpPageLocators


class SignUpPage(BasePage):
    def should_be_signup_page(self):
        self.should_be_login_url()

    def should_be_signup_url(self):
        print("Текущий URL: ", self.browser.current_url)
        assert "signup" in self.browser.current_url, "Не найдено слово 'signup' в текущем URL открытой страницы"

    def select_mr(self):
        self.browser.find_element(*SignUpPageLocators.MR_RADIOBUTTON).click()

    def select_mrs(self):
        self.browser.find_element(*SignUpPageLocators.MRS_RADIOBUTTON).click()

    def input_password(self, password):
        self.browser.find_element(*SignUpPageLocators.PASSWORD_INPUT).send_keys(password)

    def select_date_of_birth(self, day, month, year):
        day_select = Select(self.browser.find_element(*SignUpPageLocators.DAY_SELECTOR))
        day_select.select_by_value(day)

        month_select = Select(self.browser.find_element(*SignUpPageLocators.MONTH_SELECTOR))
        month_select.select_by_visible_text(month)

        year_select = Select(self.browser.find_element(*SignUpPageLocators.YEARS_SELECTOR))
        year_select.select_by_visible_text(year)

    def select_checkbox_for_newsletters(self):
        self.browser.find_element(*SignUpPageLocators.NEWSLETTER_CHECKBOX).click()

    def select_checkbox_for_special_offers(self):
        self.browser.find_element(*SignUpPageLocators.SPECIAL_OFFERS_CHECKBOX).click()

    def input_firstname(self, firstname):
        self.browser.find_element(*SignUpPageLocators.FIRSTNAME_INPUT).send_keys(firstname)

    def input_lastname(self, lastname):
        self.browser.find_element(*SignUpPageLocators.LASTNAME_INPUT).send_keys(lastname)

    def input_company(self, company_name):
        self.browser.find_element(*SignUpPageLocators.COMPANY_INPUT).send_keys(company_name)

    def input_address(self, address):
        self.browser.find_element(*SignUpPageLocators.ADDRESS_INPUT).send_keys(address)

    def input_address_2(self, address2):
        self.browser.find_element(*SignUpPageLocators.ADDRESS_INPUT_2).send_keys(address2)

    def select_country(self, country):
        country_select = Select(self.browser.find_element(*SignUpPageLocators.COUNTRY_SELECTOR))
        country_select.select_by_value(country)

    def input_state(self, state):
        self.browser.find_element(*SignUpPageLocators.STATE_INPUT).send_keys(state)

    def input_city(self, city):
        self.browser.find_element(*SignUpPageLocators.CITY_INPUT).send_keys(city)

    def input_zip(self, zip_code):
        self.browser.find_element(*SignUpPageLocators.ZIPCODE_INPUT).send_keys(zip_code)

    def input_mobile_number(self, mobile_number):
        self.browser.find_element(*SignUpPageLocators.MOBILE_INPUT).send_keys(mobile_number)

    def create_account(self):
        self.browser.find_element(*SignUpPageLocators.CREATE_ACCOUNT_BUTTON).click()

