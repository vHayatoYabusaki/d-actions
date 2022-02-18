from playwright.sync_api import Page


class TestYahoo:
    def test_yahoo(self, page: Page):
        page.goto("https://www.yahoo.com/")
        assert "yahoo" in page.url
