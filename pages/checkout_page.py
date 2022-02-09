from base.base_page import BasePage
from locators.locators import checkout_locators

CHECKOUT_URL = 'https://pay.ebay.com'


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_checkout_amount(self):
        price = self.get_element_text(checkout_locators.AMOUNT)
        if price is not None:
            return float(price.replace('Order total ', ''))
        else:
            return 0

    def is_url_checkout(self):
        return self.is_partial_url(CHECKOUT_URL)
