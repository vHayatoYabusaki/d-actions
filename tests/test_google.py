from playwright.sync_api import Page


class TestGoogle:
    def test_google(self, page: Page):
        page.goto("https://www.google.com/")
        assert "google" in page.url
