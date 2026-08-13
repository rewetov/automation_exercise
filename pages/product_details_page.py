from .base_page import BasePage
from .locators import ProductDetailsPageLocators

class ProductDetailsPage(BasePage):
    def should_be_product_details_page(self):
        self.should_be_product_name_is_present()
        self.should_be_product_category_is_present()
        self.should_be_product_price_is_present()
        self.should_be_product_availability_is_present()
        self.should_be_product_condition_is_present()
        self.should_be_product_brand_is_present()


    def should_be_product_name_is_present(self):
        assert self.browser.find_element(*ProductDetailsPageLocators.PRODUCT_NAME_LABEL), "ОШИБКА, элемент 'PRODUCT_NAME_LABEL' не найден. Не могу подтвердить, что загружена страница товара"

    def should_be_product_category_is_present(self):
        assert self.browser.find_element(*ProductDetailsPageLocators.PRODUCT_CATEGORY_LABEL), "ОШИБКА, элемент 'PRODUCT_CATEGORY_LABEL' не найден. Не могу подтвердить, что загружена страница товара"

    def should_be_product_price_is_present(self):
        assert self.browser.find_element(*ProductDetailsPageLocators.PRODUCT_PRICE_LABEL), "ОШИБКА, элемент 'PRODUCT_PRICE_LABEL' не найден. Не могу подтвердить, что загружена страница товара"

    def should_be_product_availability_is_present(self):
        assert self.browser.find_element(*ProductDetailsPageLocators.PRODUCT_AVAILABILITY_LABEL), "ОШИБКА, элемент 'PRODUCT_AVAILABILITY_LABEL' не найден. Не могу подтвердить, что загружена страница товара"

    def should_be_product_condition_is_present(self):
        assert self.browser.find_element(*ProductDetailsPageLocators.PRODUCT_CONDITION_LABEL), "ОШИБКА, элемент 'PRODUCT_CONDITION_LABEL' не найден. Не могу подтвердить, что загружена страница товара"

    def should_be_product_brand_is_present(self):
        assert self.browser.find_element(*ProductDetailsPageLocators.PRODUCT_BRAND_LABEL), "ОШИБКА, элемент 'PRODUCT_BRAND_LABEL' не найден. Не могу подтвердить, что загружена страница товара"