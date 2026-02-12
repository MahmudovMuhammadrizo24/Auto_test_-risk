class CheckoutPage:
    PLACE_ORDER_BTN = "a[href='/payment']"

    def __init__(self, page):
        self.page = page

    def place_order(self):
        self.page.wait_for_selector(self.PLACE_ORDER_BTN)
        self.page.click(self.PLACE_ORDER_BTN)
