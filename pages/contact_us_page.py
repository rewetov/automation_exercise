from .base_page import BasePage
from .locators import ContactUsPageLocators
import os


class ContactUsPage(BasePage):
    def should_be_contact_us_page(self):
        self.should_be_contact_us_link()
        self.should_be_text_label_visible()


    def should_be_contact_us_link(self):
        assert "contact_us" in self.browser.current_url, "Не найдено слово 'contact_us' в текущем URL открытой страницы"

    def should_be_text_label_visible(self):
        assert self.is_element_present(*ContactUsPageLocators.GET_IN_TOUCH_LABEL), "ОШИБКА, элемент 'GET_IN_TOUCH_LABEL' не найден. Не могу подтвердить, что открыта страница contact us"

    def should_be_success_message(self):
        assert self.is_element_present(*ContactUsPageLocators.SUCCESS_LABEL), "ОШИБКА, элемент 'SUCCESS_LABEL' не найден. Не могу подтвердить, что обращение отправлено успешно"

    def enter_name(self, name):
        self.browser.find_element(*ContactUsPageLocators.NAME_INPUT).send_keys(name)

    def enter_email(self, email):
        self.browser.find_element(*ContactUsPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_subject(self, subject):
        self.browser.find_element(*ContactUsPageLocators.SUBJECT_INPUT).send_keys(subject)

    def enter_message(self, message):
        self.browser.find_element(*ContactUsPageLocators.MESSAGE_INPUT).send_keys(message)

    def upload_file(self):
        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, "upload_files", "test.html")
        print("current_dir: ", current_dir)
        print("file_path: ", file_path)
        self.browser.find_element(*ContactUsPageLocators.UPLOAD_FILE).send_keys(file_path)

    def click_submit_button(self):
        self.browser.find_element(*ContactUsPageLocators.SUBMIT_BUTTON).click()

    def click_home_button(self):
        self.browser.find_element(*ContactUsPageLocators.HOME_BUTTON).click()

    def accept_alert(self):
        self.browser.switch_to.alert.accept()

