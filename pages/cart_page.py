from base.base_page import BasePage
from locators.locators import cart_locators

CART_URL = 'https://cart.payments.ebay.com/'


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def cart_val(self):
        price = self.get_element_text(cart_locators.TOTAL)
        if price is not None:
            return float(price.replace('US $', ''))
        else:
            return 0

    def checkout_as_guest(self):
        self.wait_for_url(CART_URL)
        self.click_element(cart_locators.GO_TO_CHECKOUT)
        self.click_element(cart_locators.CHECKOUT_AS_A_GUEST)
