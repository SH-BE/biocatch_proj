from base.base_page import BasePage
from locators.locators import home_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def choose_category(self, text):
        self.locate_select_element(home_locators.CATEGORY_LIST).select_by_visible_text(text)

    def search(self, value):
        self.send_keys_element_with_enter(home_locators.SEARCH_BOX, value)