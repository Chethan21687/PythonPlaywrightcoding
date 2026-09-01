"""Layer 6 — Pages: Checkout page."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def goto(self):
        self._page.goto("/checkout")
        self.wait_for_load()

    def verify_checkout_page(self):
        expect(self._page).to_have_url("/checkout")
