# import allure
# from pages.home_page import HomePage
# from pages.products_page import ProductsPage
# from pages.cart_page import CartPage

# @allure.feature("Cart")
# @allure.story("Add 2 Products to Cart")
# def test_add_two_products_to_cart(page):

#     home = HomePage(page)
#     products = ProductsPage(page)
#     cart = CartPage(page)

#     home.open("https://www.automationexercise.com/")
#     products.go_to_products()

#     products.add_first_two_products()
#     products.go_to_cart()

#     assert cart.get_cart_items_count() == 2
import allure
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@allure.feature("Cart")
@allure.story("Add 2 Products to Cart")
def test_add_two_products_to_cart(page):

    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    home.open("https://www.automationexercise.com/")
    products.go_to_products()

    products.add_first_two_products()
    products.go_to_cart()

    assert cart.get_cart_items_count() == 2