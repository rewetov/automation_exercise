import pytest

from .pages.users import CorrectEmailUser
from .pages.cart_page import CartPage
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

@pytest.fixture(autouse=True, scope="function")
def setup(browser):
    link = "https://automationexercise.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_main_page()

def register_user(browser, user):
    main_page = MainPage(browser, browser.current_url)
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    time.sleep(2)

    login_page.input_username_signup(user.firstname)
    login_page.input_email_signup(user.email)
    login_page.click_signup_button()

    # вводим данные о пользователе
    signup_page = SignUpPage(browser, browser.current_url)
    signup_page.select_mr()
    signup_page.input_password(user.password)
    signup_page.select_date_of_birth(user.birthday, user.birthmonth, user.birthyear)
    signup_page.select_checkbox_for_newsletters()
    signup_page.select_checkbox_for_special_offers()
    signup_page.input_firstname(user.firstname)
    signup_page.input_lastname(user.lastname)
    signup_page.input_company(user.company)
    signup_page.input_address(user.address)
    signup_page.select_country(user.country)
    signup_page.input_state(user.state)
    signup_page.input_city(user.city)
    signup_page.input_zip(user.zipcode)
    signup_page.input_mobile_number(user.mobile_number)
    time.sleep(2)
    signup_page.create_account()

    account_created_page = AccountCreatedPage(browser, browser.current_url)
    account_created_page.should_be_account_created_page()
    account_created_page.click_continue_button()
    print(f"User_email: {user.email}, password: {user.password}, firstname: {user.firstname}", sep="\n")


#Test Case 1: Register User
def test_register_user(browser):
    user = CorrectEmailUser()
    register_user(browser, user)

    main_page = MainPage(browser, browser.current_url)
    main_page.should_be_logged_in(user.firstname)
    main_page.delete_account()

    account_deleted_page = AccountDeletedPage(browser, browser.current_url)
    account_deleted_page.should_be_account_deleted()
    account_deleted_page.click_continue_button()

    main_page.should_be_main_page()
    time.sleep(2)

#Test Case 2: Login User with correct email and password
def test_login_user_with_correct_email_and_password(browser):
    #регистрируем тестового пользователя
    user = CorrectEmailUser()
    register_user(browser, user)

    #разлогиниваемся
    main_page = MainPage(browser, browser.current_url)
    main_page.should_be_main_page()
    main_page.log_out_user()

    #возвращаемся на главную страницу после разлогина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.go_to_main_page()

    main_page = MainPage(browser, browser.current_url)
    main_page.should_be_main_page()

    #логинимся под зарегистрированным ранее пользователем
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

    login_page.input_email_login(user.email)
    login_page.input_password_login(user.password)
    login_page.click_login_button()

    #проверяем что залогинены под тестовым пользователем
    main_page = MainPage(browser, browser.current_url)
    main_page.should_be_main_page()
    main_page.should_be_logged_in(user.firstname)
    time.sleep(5)


#Test Case 6: Contact Us Form
def test_contact_us_form(browser):
    main_page = MainPage(browser, browser.current_url)
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
    main_page = MainPage(browser, browser.current_url)
    main_page.go_to_t_cases_page()

    test_cases_page = TCasesPage(browser, browser.current_url)
    test_cases_page.should_be_test_cases_page()

# Test Case 8: Verify All Products and product detail page
def test_verify_all_products_page(browser):
    main_page = MainPage(browser, browser.current_url)
    main_page.go_to_products_page()

    products_page = ProductsPage(browser, browser.current_url)
    products_page.should_be_products_page()
    products_page.click_view_product_button()

    product_details_page = ProductDetailsPage(browser, browser.current_url)
    product_details_page.should_be_product_details_page()

#Test Case 9: Search Product
def test_verify_search_products_page(browser):
    product_name = "Sleeveless Dress"

    main_page = MainPage(browser, browser.current_url)
    main_page.go_to_products_page()

    products_page = ProductsPage(browser, browser.current_url)
    products_page.should_be_products_page()
    products_page.search_product(product_name)
    products_page.should_be_the_same_names(product_name)

#Test Case 10: Verify Subscription in home page
def test_verify_subscription_in_home_page(browser):
    email = "test@gmail.com"

    main_page = MainPage(browser, browser.current_url)
    main_page.scroll_to_footer()
    main_page.should_be_subscription_label()
    main_page.subscribe(email)
    main_page.should_be_subscribed()

#Test Case 11: Verify Subscription in Cart page
def test_verify_subscription_in_cart_page(browser):
    email = "test@gmail.com"

    main_page = MainPage(browser, browser.current_url)
    main_page.go_to_cart_page()

    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()
    cart_page.scroll_to_footer()
    cart_page.should_be_subscription_label()
    cart_page.subscribe(email)
    cart_page.should_be_subscribed()

