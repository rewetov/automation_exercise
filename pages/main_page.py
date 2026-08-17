from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_main_page(self):
        self.should_be_main_page_link()
        self.should_be_carousel_on_main_page()



    def should_be_main_page_link(self):
        browser_link = self.browser.current_url
        assert browser_link == "https://automationexercise.com/", f"Ссылка для главной страницы ожидается 'https://automationexercise.com/', а по факту {browser_link}"

    def should_be_carousel_on_main_page(self):
        assert self.is_element_present(*MainPageLocators.CAROUSEL), "ОШИБКА, элемент 'CAROUSEL' не найден. Не могу подтвердить, что открыта главная страница"


