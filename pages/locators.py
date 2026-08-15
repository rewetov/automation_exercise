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
    SUBSCRIPTION_LABEL = (By.CSS_SELECTOR, "#footer h2")
    SUBSCRIPTION_EMAIL_INPUT = (By.CSS_SELECTOR, ".searchform #susbscribe_email")
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, ".searchform button")
    SUBSCRIBED_SUCCESSFULLY_MESSAGE_VISIBLE = (By.CSS_SELECTOR, "#success-subscribe")
    SUBSCRIBED_SUCCESSFULLY_MESSAGE_INVISIBLE = (By.CSS_SELECTOR, ".col-md-9.form-group.hide")

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

class ContactUsPageLocators():
    GET_IN_TOUCH_LABEL = (By.CSS_SELECTOR, ".contact-form h2")
    NAME_INPUT = (By.CSS_SELECTOR, "[name='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='email']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "[name='subject']")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "[name='message']")
    UPLOAD_FILE = (By.CSS_SELECTOR, "[name='upload_file']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='submit']")
    SUCCESS_LABEL = (By.CSS_SELECTOR, ".status.alert.alert-success")
    HOME_BUTTON = (By.CSS_SELECTOR, ".btn-success")

class ProductsPageLocators():
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".products")
    FIRST_PRODUCT_VIEW_BUTTON = (By.CSS_SELECTOR, "a[href*='/product_details/1']")
    #PRODUCT_NAME = (By.CSS_SELECTOR, f".col-sm-4:nth-child({}) .productinfo.text-center p")
    SEARCH_PRODUCT_INPUT = (By.CSS_SELECTOR, "input#search_product")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#submit_search.btn.btn-default.btn-lg")


class ProductDetailsPageLocators():
    PRODUCT_NAME_LABEL = (By.CSS_SELECTOR, ".product-information h2")
    PRODUCT_CATEGORY_LABEL = (By.CSS_SELECTOR, ".product-information p:nth-child(3)") #не нашел другого селектора, кроме как по порядковому номеру
    PRODUCT_PRICE_LABEL = (By.CSS_SELECTOR, ".product-information > span > span")
    PRODUCT_AVAILABILITY_LABEL = (By.CSS_SELECTOR, ".product-information p:nth-child(6) b") #не нашел другого селектора, кроме как по порядковому номеру
    PRODUCT_CONDITION_LABEL = (By.CSS_SELECTOR, ".product-information p:nth-child(7) b")
    PRODUCT_BRAND_LABEL = (By.CSS_SELECTOR, ".product-information p:nth-child(8) b")