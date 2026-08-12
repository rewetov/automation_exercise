from selenium.webdriver.common.by import By

class LoginPageLocators():
    INPUT_NAME = (By.CSS_SELECTOR, "[data-qa='signup-name']")
    INPUT_EMAIL = (By.CSS_SELECTOR, "[data-qa='signup-email']")
    BUTTON_SIGNUP = (By.CSS_SELECTOR, "[data-qa='signup-button']")
    SIGNUP_FORM = (By.CSS_SELECTOR, ".signup-form")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login-form")

class MainPageLocators():
    CAROUSEL = (By.CSS_SELECTOR, "#slider-carousel.carousel.slide")

class BasePageLocators():
    HOME_NAVBAR_BUTTON = (By.CSS_SELECTOR, ".nav.navbar-nav a[href*='/'] .fa.fa-home")
    PRODUCT_NAVBAR_BUTTON = (By.CSS_SELECTOR, ".nav.navbar-nav a[href*='/product']")
    CART_NAVBAR_BUTTON = (By.CSS_SELECTOR, ".nav.navbar-nav a[href*='/view_cart']")
    SIGNUP_LOGIN_NAVBAR_BUTTON = (By.CSS_SELECTOR, ".nav.navbar-nav a[href*='/login']")
    TESTCASES_NAVBAR_BUTTON = (By.CSS_SELECTOR, ".nav.navbar-nav a[href*='/test_cases']")
    APITESTING_NAVBAR_BUTTON = (By.CSS_SELECTOR, ".nav.navbar-nav a[href*='/api_list']")
    CONTACTUS_NAVBAR_BUTTON = (By.CSS_SELECTOR, ".nav.navbar-nav a[href*='/contact_us']")
    LOGGED_IN_AS = (By.CSS_SELECTOR, ".fa.fa-user + b")
    DELETE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".nav.navbar-nav a[href*='/delete_account']")

class SignUpPageLocators():
    ENTER_ACCOUNT_INFORMATION_TEXT = (By.CSS_SELECTOR, ".login-form h2:nth-child(1) b")
    MR_RADIOBUTTON = (By.CSS_SELECTOR, "#id_gender1")
    MRS_RADIOBUTTON = (By.CSS_SELECTOR, "#id_gender2")
    NAME_INPUT = (By.CSS_SELECTOR, "#name")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    DAY_SELECTOR = (By.CSS_SELECTOR, ".selector [data-qa='days']")
    MONTH_SELECTOR = (By.CSS_SELECTOR, ".selector [data-qa='months']")
    YEARS_SELECTOR = (By.CSS_SELECTOR, ".selector [data-qa='years']")
    NEWSLETTER_CHECKBOX = (By.CSS_SELECTOR, ".checkbox #uniform-newsletter input")
    SPECIAL_OFFERS_CHECKBOX = (By.CSS_SELECTOR, ".checkbox #uniform-optin input")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, ".form-control[data-qa='first_name']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, ".form-control[data-qa='last_name']")
    COMPANY_INPUT = (By.CSS_SELECTOR, ".form-control[data-qa='company']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, ".form-control[data-qa='address']")
    ADDRESS_2_INPUT = (By.CSS_SELECTOR, ".form-control[data-qa='address2']")
    COUNTRY_SELECTOR = (By.CSS_SELECTOR, ".form-control[data-qa='country']")
    STATE_INPUT = (By.CSS_SELECTOR, ".form-control[data-qa='state']")
    CITY_INPUT = (By.CSS_SELECTOR, ".form-control[data-qa='city']")
    ZIPCODE_INPUT = (By.CSS_SELECTOR, ".form-control[data-qa='zipcode']")
    MOBILE_INPUT = (By.CSS_SELECTOR, ".form-control[data-qa='mobile_number']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-qa='create-account']")

class AccountCreatedPageLocators():
    ACCOUNT_CREATED_TEXT = (By.CSS_SELECTOR, ".title.text-center b")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-qa='continue-button']")

class AccountDeletedPageLocators():
    ACCOUNT_DELETED_TEXT = (By.CSS_SELECTOR, ".title.text-center b")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-qa='continue-button']")
