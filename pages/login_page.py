from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page) # Вызываем super, чтобы вызвать init родительского класса

        # Описываем атрибуты класса / элементы на странице
        self.email_input = page.get_by_test_id("login-form-email-input").locator('input')
        self.password_input = page.get_by_test_id("login-form-password-input").locator('input')
        self.login_button = page.get_by_test_id("login-page-login-button")
        self.registration_link = page.get_by_test_id("login-page-registration-link")
        self.wrong_email_or_password_alert = page.get_by_test_id("login-page-wrong-email-or-password-alert")


    # Метод заполнения форм с проверкой полей
    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    # Метод нажатия на кнопку логина
    def click_login_button(self):
        self.login_button.click()

    # Метод нажатия на ссылку регистрации
    def click_registration_link(self):
        self.registration_link.click()

    # Проверка алерта при невалидных данных
    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")

