from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page) # Вызываем super, чтобы вызвать init родительского класса

        # Описываем атрибуты класса / элементы на странице
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    # Метод проверки видимости и текста заголовка
    def check_visibility_and_text_dashboard_title(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')