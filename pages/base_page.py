import allure

class BasePage:
    def __init__(self, page):
        self.page = page

    def open_url(self, url):
        with allure.step(f"Sahifani ochish: {url}"):
            self.page.goto(url)

    def click(self, selector):
        with allure.step(f"Elementni bosish: {selector}"):
            self.page.wait_for_selector(selector)
            self.page.click(selector)

    def fill(self, selector, text):
        with allure.step(f"Matn kiritish: {text}"):
            self.page.wait_for_selector(selector)
            self.page.fill(selector, text)