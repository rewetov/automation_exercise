import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import time

def test_guest_signup(browser):
    link = "https://automationexercise.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_login_page()

    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()
    time.sleep(5)
