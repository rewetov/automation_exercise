import requests
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from .base_page import BasePage
from .locators import ProductsPageLocators


class ProductsPage(BasePage):
    def should_be_products_page(self):
        self.should_be_products_link()

    def should_be_products_link(self):
        assert "products" in self.browser.current_url, "Не найдено слово 'products' в текущем URL открытой страницы"

    #Здесь захардкожена только первая карточка. Пока хз как сделать в коде, чтобы можно было любую карточку выбирать
    def click_view_product_button(self):
        self.browser.find_element(*ProductsPageLocators.FIRST_PRODUCT_VIEW_BUTTON).click()

    def search_product(self, name):
        self.browser.find_element(*ProductsPageLocators.SEARCH_PRODUCT_INPUT).send_keys(name)
        self.browser.find_element(*ProductsPageLocators.SEARCH_BUTTON).click()

    #хз как в локаторах сделать возможность динамически выбирать номер элемента.
    #Поэтому пока вынес поиск элемента в описание страницы. Наверняка как то можно без этого, но пока хз как
    def should_be_the_same_name_by_index(self, index, name):
        element_text = self.browser.find_element(By.CSS_SELECTOR, f".col-sm-4:nth-child({index}) .productinfo.text-center p").text
        assert name in element_text, f"Имя продукта '{name}' не найдено в элементе с индексом {index}."

    #Поиск нужно как то отдельно тестить подробно. Здесь просто пробный тест. Выдача слишком отличается.
    #На поисковый запрос T-shirt выдаст и tshirt и Tshirt и TSHIRT и t-shirt, не понятно как это проверять асертами.
    def should_be_the_same_names(self, name):
        response = requests.get(self.browser.current_url)
        soup = BeautifulSoup(response.text, "html.parser")
        elements = soup.select(".single-products")
        elements_count = len(elements)
        print(f"Найдено {elements_count} элементов")
        for i in range(3, elements_count+3):
            print(f"Ищу подстроку '{name}' в элементе номер {i}")
            self.should_be_the_same_name_by_index(i, name)