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
