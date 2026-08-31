"""Layer 6 — Pages: Login page."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = self.get_by_label('Username')
        self.password_input = self.get_by_label('Password')
        self.login_button = self.get_by_label('Login')

    def goto(self):
        self._page.goto('/login')
        self.wait_for_load()

    def login_with_valid_credentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.wait_for_load()
        expect(self._page).to_have_url('/dashboard')
        expect(self._page).to_have_title('Dashboard')