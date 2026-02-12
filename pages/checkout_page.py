class CheckoutPage:

    PROCEED_TO_CHECKOUT = "a.check_out"
    PLACE_ORDER_BTN = "a[href='/payment']"
    NAME_ON_CARD = "input[name='name_on_card']"
    CARD_NUMBER = "input[name='card_number']"
    CVC = "input[name='cvc']"
    EXP_MONTH = "input[name='expiry_month']"
    EXP_YEAR = "input[name='expiry_year']"
    PAY_BUTTON = "button[data-qa='pay-button']"
    SUCCESS_MESSAGE = "p.alert-success"

    def __init__(self, page):
        self.page = page

    def proceed_to_checkout(self):
        self.page.click(self.PROCEED_TO_CHECKOUT)

    def place_order(self):
        self.page.click(self.PLACE_ORDER_BTN)

    def fill_payment_details(self):
        self.page.fill(self.NAME_ON_CARD, "Test User")
        self.page.fill(self.CARD_NUMBER, "4111111111111111")
        self.page.fill(self.CVC, "123")
        self.page.fill(self.EXP_MONTH, "12")
        self.page.fill(self.EXP_YEAR, "2030")

    def confirm_payment(self):
        self.page.click(self.PAY_BUTTON)

    def get_success_message(self):
        return self.page.locator(self.SUCCESS_MESSAGE).text_content()
