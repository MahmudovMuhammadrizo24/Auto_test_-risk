from pages.base_page import BasePage

class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_link = "a[href='/login']"
        self.name_input = "input[data-qa='signup-name']"
        self.email_input = "input[data-qa='signup-email']"
        self.signup_btn = "button[data-qa='signup-button']"
        self.create_btn = "button[data-qa='create-account']"

    def register(self, name, email):
        self.click(self.login_link)
        self.fill(self.name_input, name)
        self.fill(self.email_input, email)
        self.click(self.signup_btn)
        self.page.check("#id_gender1")
        self.fill("#password", "Pass12345")
        self.fill("#first_name", name)
        self.fill("#last_name", "Automation")
        self.fill("#address1", "Navoi St 1")
        self.fill("#state", "Tashkent")
        self.fill("#city", "Tashkent")
        self.fill("#zipcode", "100000")
        self.fill("#mobile_number", "998901234567")
        self.click(self.create_btn)