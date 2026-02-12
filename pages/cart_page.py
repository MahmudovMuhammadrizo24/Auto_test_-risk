import allure
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.proceed_to_checkout = ".check_out"
        self.message_input = "textarea[name='message']"
        self.place_order_btn = "a[href='/payment']"

    @allure.step("Savatni tekshirish va to'lovga o'tish")
    def proceed_to_buy(self):
        self.click_element(self.proceed_to_checkout)
        self.enter_text(self.message_input, "Iltimos, tezroq yetkazing.")
        self.click_element(self.place_order_btn)