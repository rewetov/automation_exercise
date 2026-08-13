from .base_page import BasePage
from .locators import ProductsPageLocators


class ProductsPage(BasePage):
    def should_be_products_page(self):
        self.should_be_products_link()

    def should_be_products_link(self):
        assert "products" in self.browser.current_url, "Не найдено слово 'products' в текущем URL открытой страницы"

    #здесь захардкожена только первая карточка. Пока хз как сделать в коде, чтобы можно было любую карточку выбирать
    def click_view_product_button(self):
        self.browser.find_element(*ProductsPageLocators.FIRST_PRODUCT_VIEW_BUTTON).click()