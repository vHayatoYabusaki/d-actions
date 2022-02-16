import time

from playwright.sync_api import Page


class TestUserAgent:
    def test_useragent(self, page: Page):
        page.goto("http://whatsmyuseragent.org/")
        time.sleep(10)
