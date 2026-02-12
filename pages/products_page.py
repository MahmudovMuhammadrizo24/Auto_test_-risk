from .base_page import BasePage

class ProductsPage(BasePage):

    PRODUCTS_BUTTON = "a[href='/products']"
    PRODUCT_CARDS = ".product-image-wrapper"
    CONTINUE_SHOPPING_BUTTON = "button[data-dismiss='modal']"
    VIEW_CART_BUTTON = "u"

    def go_to_products(self):
        self.click(self.PRODUCTS_BUTTON)

    def add_first_two_products(self):
        products = self.page.locator(self.PRODUCT_CARDS)

        # ---------- FIRST PRODUCT ----------
        first_product = products.nth(0)
        first_product.hover()

        first_product.locator("a.add-to-cart").first.click(force=True)
        self.page.wait_for_selector(self.CONTINUE_SHOPPING_BUTTON)
        self.click(self.CONTINUE_SHOPPING_BUTTON)

        # ---------- SECOND PRODUCT ----------
        second_product = products.nth(1)
        second_product.hover()

        second_product.locator("a.add-to-cart").first.click(force=True)
        self.page.wait_for_selector(self.VIEW_CART_BUTTON)

    def go_to_cart(self):
        self.click(self.VIEW_CART_BUTTON)