import allure
import pytest
from playwright.sync_api import Page


class TestGoogle:
    def test_google(self, page: Page):
        page.goto("https://www.google.com/")
        allure.attach(page.screenshot(), attachment_type=allure.attachment_type.PNG)

    def test_fail_google(self, page: Page):
        page.goto("https://www.google.com/")
        assert "google" not in page.url

    @pytest.mark.skip
    def test_skip_google(self, page: Page):
        page.goto("https://www.google.com/")
        assert "google" not in page.url
