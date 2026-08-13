from pages.base_page import BasePage


class TestCasesPage(BasePage):
    def should_be_test_cases_page(self):
        self.should_be_test_cases_link()

    def should_be_test_cases_link(self):
        assert "test_cases" in self.browser.current_url, f"Текущая ссылка {self.browser.current_url}, а ожидается 'https://automationexercise.com/test_cases'"
