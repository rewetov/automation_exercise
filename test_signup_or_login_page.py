from .pages.contact_us_page import ContactUsPage
from .pages.product_details_page import ProductDetailsPage
from .pages.products_page import ProductsPage
from .pages.t_cases_page import TCasesPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.signup_page import SignUpPage
from .pages.account_created_page import AccountCreatedPage
from .pages.account_deleted_page import AccountDeletedPage
import time

#Test Case 1: Register User
def test_register_user(browser):
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

    #вводим данные о пользователе
    signup_page = SignUpPage(browser, browser.current_url)
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

    account_created_page = AccountCreatedPage(browser, browser.current_url)
    account_created_page.should_be_account_created_page()
    account_created_page.click_continue_button()

    main_page.should_be_loged_in(firstname)
    main_page.delete_account()

    account_deleted_page = AccountDeletedPage(browser, browser.current_url)
    account_deleted_page.should_be_account_deleted()
    account_deleted_page.click_continue_button()

    main_page.should_be_main_page()
    time.sleep(2)

#Test Case 6: Contact Us Form
def test_contact_us_form(browser):
    link = "https://automationexercise.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_contact_us_page()

    contact_us_page = ContactUsPage(browser, browser.current_url)
    contact_us_page.should_be_contact_us_page()
    contact_us_page.enter_name("Alex test")
    contact_us_page.enter_email("alex@gmail.com")
    contact_us_page.enter_subject("Test subject")
    contact_us_page.enter_message("Test message")
    contact_us_page.upload_file()
    contact_us_page.click_submit_button()
    contact_us_page.accept_alert()
    contact_us_page.should_be_success_message()
    contact_us_page.click_home_button()

    main_page.should_be_main_page()
    time.sleep(2)

# Test Case 7: Verify Test Cases Page
def test_verify_test_cases_page(browser):
    link = "https://automationexercise.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_t_cases_page()

    test_cases_page = TCasesPage(browser, browser.current_url)
    test_cases_page.should_be_test_cases_page()

# Test Case 8: Verify All Products and product detail page
def test_verify_all_products_page(browser):
    link = "https://automationexercise.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_products_page()

    products_page = ProductsPage(browser, browser.current_url)
    products_page.should_be_products_page()
    products_page.click_view_product_button()

    product_details_page = ProductDetailsPage(browser, browser.current_url)
    product_details_page.should_be_product_details_page()



