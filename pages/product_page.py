from base.base_page import BasePage
from locators.locators import product_locators
from pages.cart_page import CartPage

CART_URL = 'https://cart.payments.ebay.com/'


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cart = CartPage(self.driver)

    def add_to_cart(self):
        self.switch_to_next_window()
        cart_val = 0
        if self.try_click_element(product_locators.ADD_TO_CART):
            if self.wait_for_url(CART_URL):
                cart_val = self.cart.cart_val()
        self.close_and_go_back_window()
        return cart_val
