from .base_page import BasePage


class CartPage(BasePage):
    def should_be_cart_page(self):
        self.should_be_cart_link()

    def should_be_cart_link(self):
        assert "view_cart" in self.browser.current_url, f"Текущая ссылка {self.browser.current_url}, а ожидается 'https://automationexercise.com/view_cart'"

