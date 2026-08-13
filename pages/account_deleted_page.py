from .base_page import BasePage
from .locators import AccountDeletedPageLocators


class AccountDeletedPage(BasePage):
    def should_be_account_deleted(self):
        self.should_account_deleted_text()

    def should_account_deleted_text(self):
        deleted_text = self.browser.find_element(*AccountDeletedPageLocators.ACCOUNT_DELETED_TEXT).text
        assert deleted_text == "ACCOUNT DELETED!", f"Ошибка! Ожидается текст 'ACCOUNT DELETED!', а выводится {deleted_text}."  # не правильно завязываться на текст, но в тесткейсе это явно указано

    def click_continue_button(self):
        self.browser.find_element(*AccountDeletedPageLocators.CONTINUE_BUTTON).click()