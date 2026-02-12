from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout(page):
    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    home.login("YOUR_REAL_EMAIL", "YOUR_REAL_PASSWORD")

    products.go_to_products()
    products.add_first_product()
    cart.go_to_cart()
    cart.click_checkout()
    checkout.place_order()

    assert "payment" in page.url
