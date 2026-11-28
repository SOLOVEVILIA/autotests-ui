from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent



class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page) # Вызываем super, чтобы вызвать init родительского класса

        self.registration_form = RegistrationFormComponent(page)