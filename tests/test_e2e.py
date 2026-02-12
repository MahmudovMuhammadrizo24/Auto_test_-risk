import pytest
import allure
import time
from pages.signup_page import SignupPage
from pages.products_page import ProductsPage

@allure.feature("Full E2E Shopping")
def test_full_purchase_process(page):
    signup = SignupPage(page)
    products = ProductsPage(page)

    # 1. Registration
    signup.open_url("https://www.automationexercise.com/")
    email = f"user_{int(time.time())}@mail.com"
    signup.register("TestUser", email)
    page.click("a[data-qa='continue-button']")

    # 2. Add 2 products to Cart
    products.add_two_products()

    # 3. Check products in Cart
    with allure.step("Savatni tekshirish"):
        assert page.locator("tbody tr").count() == 2

    # 4. Buy all products
    with allure.step("Sotib olish"):
        page.click(".check_out")
        page.click("a[href='/payment']")
        page.fill("[name='name_on_card']", "Test Card")
        page.fill("[name='card_number']", "1111222233334444")
        page.fill("[name='cvc']", "311")
        page.fill("[name='expiry_month']", "12")
        page.fill("[name='expiry_year']", "2027")
        page.click("button[data-qa='pay-button']")
        assert page.locator("b:has-text('Order Placed!')").is_visible()