from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def get_text(self, locator: str):
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator: str):
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator: str):
        self.page.locator(locator).wait_for()
