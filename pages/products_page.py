"""Layer 6 — Pages: Products page."""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def goto(self):
        self._page.goto("/products")
        self.wait_for_load()

    def verify_products_page(self):
        expect(self._page).to_have_url("/products")
