# from .base_page import BasePage
# import random

# class SignupPage(BasePage):

#     # Step 1
#     NAME_INPUT = "input[data-qa='signup-name']"
#     EMAIL_INPUT = "input[data-qa='signup-email']"
#     SIGNUP_BUTTON = "button[data-qa='signup-button']"

#     # Step 2
#     TITLE = "#id_gender1"
#     PASSWORD = "#password"
#     DAY = "#days"
#     MONTH = "#months"
#     YEAR = "#years"

#     FIRST_NAME = "#first_name"
#     LAST_NAME = "#last_name"
#     ADDRESS = "#address1"
#     COUNTRY = "#country"
#     STATE = "#state"
#     CITY = "#city"
#     ZIPCODE = "#zipcode"
#     MOBILE = "#mobile_number"

#     CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"
#     ACCOUNT_CREATED_TEXT = "h2[data-qa='account-created']"

#     def generate_email(self):
#         return f"test{random.randint(1000,9999)}@gmail.com"

#     def register_user(self, name: str):
#         email = self.generate_email()

#         # Step 1
#         self.fill(self.NAME_INPUT, name)
#         self.fill(self.EMAIL_INPUT, email)
#         self.click(self.SIGNUP_BUTTON)

#         # Step 2
#         self.click(self.TITLE)
#         self.fill(self.PASSWORD, "Test12345")

#         self.page.select_option(self.DAY, "1")
#         self.page.select_option(self.MONTH, "1")
#         self.page.select_option(self.YEAR, "2000")

#         self.fill(self.FIRST_NAME, "Test")
#         self.fill(self.LAST_NAME, "User")
#         self.fill(self.ADDRESS, "Tashkent")
#         self.page.select_option(self.COUNTRY, "India")
#         self.fill(self.STATE, "TestState")
#         self.fill(self.CITY, "Tashkent")
#         self.fill(self.ZIPCODE, "100000")
#         self.fill(self.MOBILE, "998901234567")

#         self.click(self.CREATE_ACCOUNT_BUTTON)

#     def is_account_created(self):
#         return self.is_visible(self.ACCOUNT_CREATED_TEXT)
from .base_page import BasePage
import random

class SignupPage(BasePage):

    # Step 1
    NAME_INPUT = "input[data-qa='signup-name']"
    EMAIL_INPUT = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"

    # Step 2
    TITLE = "#id_gender1"
    PASSWORD = "#password"
    DAY = "#days"
    MONTH = "#months"
    YEAR = "#years"

    FIRST_NAME = "#first_name"
    LAST_NAME = "#last_name"
    ADDRESS = "#address1"
    COUNTRY = "#country"
    STATE = "#state"
    CITY = "#city"
    ZIPCODE = "#zipcode"
    MOBILE = "#mobile_number"

    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"
    ACCOUNT_CREATED_TEXT = "h2[data-qa='account-created']"

    def generate_email(self):
        return f"test{random.randint(1000,9999)}@gmail.com"

    def register_user(self, name: str):
        email = self.generate_email()

        # Step 1
        self.fill(self.NAME_INPUT, name)
        self.fill(self.EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

        # Step 2
        self.click(self.TITLE)
        self.fill(self.PASSWORD, "Test12345")

        self.page.select_option(self.DAY, "1")
        self.page.select_option(self.MONTH, "1")
        self.page.select_option(self.YEAR, "2000")

        self.fill(self.FIRST_NAME, "Test")
        self.fill(self.LAST_NAME, "User")
        self.fill(self.ADDRESS, "Tashkent")
        self.page.select_option(self.COUNTRY, "India")
        self.fill(self.STATE, "TestState")
        self.fill(self.CITY, "Tashkent")
        self.fill(self.ZIPCODE, "100000")
        self.fill(self.MOBILE, "998901234567")

        self.click(self.CREATE_ACCOUNT_BUTTON)

    def is_account_created(self):
        return self.is_visible(self.ACCOUNT_CREATED_TEXT)