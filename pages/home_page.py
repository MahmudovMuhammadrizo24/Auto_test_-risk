from .base_page import BasePage

class HomePage(BasePage):

    SIGNUP_LOGIN_BUTTON = "a[href='/login']"

    def go_to_signup(self):
        self.click(self.SIGNUP_LOGIN_BUTTON)
