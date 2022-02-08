from time import sleep
import pytest

from base.basePage import BasePage
from pages.home_page import HomePage


@pytest.mark.usefixtures('setup')
class Test_ebay:
    @pytest.fixture()
    def before(self):
        pass

    def test_one(self, before):
        home_page = HomePage(self.driver)
        home_page.choose_category('Art')
        sleep(5)
