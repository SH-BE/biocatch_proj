import pytest
from pages.checkout_page import CheckoutPage
from pages.search_items_page import SearchedItemsPage
from pages.home_page import HomePage

URL = 'https://www.ebay.com/'


@pytest.mark.usefixtures('setup')
class Test_ebay:
    @pytest.fixture()
    def go_to_ebay(self):
        self.driver.get(URL)
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_buy_until_five_hundred_dollars(self, go_to_ebay):
        home_page = HomePage(self.driver)
        searched_items = SearchedItemsPage(self.driver)
        checkout = CheckoutPage(self.driver)
        home_page.choose_category('Books')
        home_page.search('Harry Potter')
        searched_items.set_max_price(100)
        cart_val = searched_items.add_to_cart_until_amount(500)
        searched_items.go_to_checkout()
        assert checkout.is_url_checkout(), "web page is not checkout page"
        assert cart_val == checkout.get_checkout_amount(), "checkout amount is not correct"
