from selenium.webdriver.common.by import By

from .base_page import BasePage


class CartPage(BasePage):
    def should_be_cart_page(self):
        self.should_be_cart_link()

    def should_be_cart_link(self):
        assert "view_cart" in self.browser.current_url, f"Текущая ссылка {self.browser.current_url}, а ожидается 'https://automationexercise.com/view_cart'"

    def should_be_right_parameters(self, product, index):
        self.should_be_right_price(product, index)
        self.should_be_right_quantity(product, index)
        self.should_be_right_total_price(product, index)

    #сравниваем цену в корзине и в экземпляре продукта, который создан на момент покупки
    def should_be_right_price(self, product, index):
        cart_product_price = self.extract_int(self.browser.find_element(By.CSS_SELECTOR, f"#product-{index} .cart_price").text)
        print(f"Цена товара на странице продуктов: '{product.product_price}', цена в корзине: '{cart_product_price}'.")
        assert product.product_price == cart_product_price, "Цена товара в корзине не соответствует цене товара на странице продуктов на момент покупки этого товара"

    # сравниваем количество в корзине и в экземпляре продукта, который создан на момент покупки
    def should_be_right_quantity(self, product, index):
        cart_product_quantity = int(self.browser.find_element(By.CSS_SELECTOR, f"#product-{index} .cart_quantity").text)
        print(f"Количество добавленных товаров: '{product.product_quantity}', количество в корзине: '{cart_product_quantity}'.")
        assert product.product_quantity == cart_product_quantity, "Количество товаров в корзине не соответствует количеству добавленных товаров на момент покупки"

    # сравниваем общую цену в корзине и в экземпляре продукта, который создан на момент покупки
    def should_be_right_total_price(self, product, index):
        cart_product_price = self.extract_int(self.browser.find_element(By.CSS_SELECTOR, f"#product-{index} .cart_price").text)
        cart_product_quantity = int(self.browser.find_element(By.CSS_SELECTOR, f"#product-{index} .cart_quantity").text)

        total_price_cart = int(cart_product_price) * int(cart_product_quantity)
        total_price_instance = int(product.product_price) * int(product.product_quantity)
        print(f"Общая цена в инстансе: '{total_price_instance}', общая цена в корзине: '{total_price_cart}'.", end="\n\n")
        assert total_price_cart == total_price_instance, "Общая цена товара в корзине не равна общей цене сохраненной на момент покупки"