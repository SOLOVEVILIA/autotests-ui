from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page) # Вызываем super, чтобы вызвать init родительского класса

        # Передаём компоненты navbar и sidebar
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        # Описываем атрибуты класса / элементы на странице
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

        self.scores_chart = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart = ChartViewComponent(page, "courses", "pie")
        self.students_chart = ChartViewComponent(page, "students", "bar")
        self.activities_chart = ChartViewComponent(page, "activities", "line")
