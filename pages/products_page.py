from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products_link = "a[href='/products']"
        self.add_to_cart_p1 = "(//a[@data-product-id='1'])[1]"
        self.add_to_cart_p2 = "(//a[@data-product-id='2'])[1]"
        self.continue_btn = "button.close-modal"

    def add_two_products(self):
        self.click(self.products_link)
        self.page.hover("(//div[@class='single-products'])[1]")
        self.click(self.add_to_cart_p1)
        self.click(self.continue_btn)
        self.page.hover("(//div[@class='single-products'])[2]")
        self.click(self.add_to_cart_p2)
        self.click(self.continue_btn)
        self.page.goto("https://www.automationexercise.com/view_cart")