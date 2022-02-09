from base.base_page import BasePage
from locators.locators import searched_items_locators
from pages.cart_page import CartPage
from pages.product_page import ProductPage


class SearchedItemsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.product = ProductPage(self.driver)
        self.cart = CartPage(self.driver)

    def set_max_price(self, price):
        self.send_keys_element_with_enter(searched_items_locators.MAX_PRICE, str(price))

    def add_to_cart_until_amount(self, limit):
        items = self.locate_elements(searched_items_locators.ITEMS)[1:]
        cart_sum = 0
        for item in items:
            self.click_element_instance(item)
            cart_sum = self.product.add_to_cart()
            if cart_sum >= limit:
                break
        return cart_sum

    def go_to_checkout(self):
        self.click_element(searched_items_locators.ICON)
        self.cart.checkout_as_guest()