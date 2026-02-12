import allure
from pages.home_page import HomePage
from pages.signup_page import SignupPage

@allure.feature("Registration")
@allure.story("User Registration Test")
def test_user_registration(page):

    home = HomePage(page)
    signup = SignupPage(page)

    home.open("https://www.automationexercise.com/")
    home.go_to_signup()

    signup.register_user("TestUser")

    assert signup.is_account_created()