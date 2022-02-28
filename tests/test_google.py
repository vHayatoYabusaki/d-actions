from playwright.sync_api import Page
import pytest


class TestGoogle:
    def test_google(self, page: Page):
        page.goto("https://www.google.com/")
        assert "google" in page.url

    def test_fail_google(self, page: Page):
        page.goto("https://www.google.com/")
        assert "google" not in page.url

    @pytest.mark.skip
    def test_skip_google(self, page: Page):
        page.goto("https://www.google.com/")
        assert "google" not in page.url
