from .base_page import BasePage

class CartPage(BasePage):

    CART_ITEMS = ".cart_description"

    def get_cart_items_count(self):
        return self.page.locator(self.CART_ITEMS).count()