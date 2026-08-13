from .base_page import BasePage
from .locators import AccountCreatedPageLocators


class AccountCreatedPage(BasePage):
    def should_be_account_created_page(self):
        self.should_account_created_text()

    def should_account_created_text(self):
        congratulation_text = self.browser.find_element(*AccountCreatedPageLocators.ACCOUNT_CREATED_TEXT).text
        assert congratulation_text == "ACCOUNT CREATED!", f"Ошибка! Ожидается текст 'ACCOUNT CREATED!', а выводится {congratulation_text}." #не правильно завязываться на текст, но в тесткейсе это явно указано

    def click_continue_button(self):
        self.browser.find_element(*AccountCreatedPageLocators.CONTINUE_BUTTON).click()