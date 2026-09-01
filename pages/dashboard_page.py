"""Layer 6 — Pages: Dashboard page."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def goto(self):
        self._page.goto("/dashboard")
        self.wait_for_load()

    def verify_dashboard(self):
        expect(self._page).to_have_url("/dashboard")
        expect(self._page).to_have_title("Dashboard")
