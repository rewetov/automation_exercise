import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.signup_page import SignUpPage
from .pages.account_created_page import AccountCreatedPage
from .pages.account_deleted_page import AccountDeletedPage
import time

def test_guest_signup(browser):
    link = "https://automationexercise.com/"
    firstname = "Alex" + str(time.time())
    lastname = "Guest"
    email = str(time.time()) + "@fakemail.org"
    password = "Rojer101"
    birthday = "7"
    birthmonth = "July"
    birthyear = "1989"
    company = "apple"
    address = "main street 1"
    country = "Singapore"
    state = "Singapore"
    city = "Samara"
    zipcode = "123456"
    mobile_number = "+9 999 999 99 99"


    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_login_page()

    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()
    time.sleep(2)

    login_page.input_username(firstname)
    login_page.input_email(email)
    login_page.click_signup_button()

    signup_page = SignUpPage(browser, link)
    signup_page.select_mr()
    signup_page.input_password(password)
    signup_page.select_date_of_birth(birthday, birthmonth, birthyear)
    signup_page.select_checkbox_for_newsletters()
    signup_page.select_checkbox_for_special_offers()
    signup_page.input_firstname(firstname)
    signup_page.input_lastname(lastname)
    signup_page.input_company(company)
    signup_page.input_address(address)
    signup_page.select_country(country)
    signup_page.input_state(state)
    signup_page.input_city(city)
    signup_page.input_zip(zipcode)
    signup_page.input_mobile_number(mobile_number)
    time.sleep(2)
    signup_page.create_account()

    account_created_page = AccountCreatedPage(browser, link)
    account_created_page.should_be_account_created_page()
    account_created_page.click_continue_button()

    main_page.should_be_loged_in(firstname)
    main_page.delete_account()

    account_deleted_page = AccountDeletedPage(browser, link)
    account_deleted_page.should_be_account_deleted()
    account_deleted_page.click_continue_button()

    main_page.should_be_main_page()
    time.sleep(2)



