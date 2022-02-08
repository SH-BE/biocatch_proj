from time import sleep

from selenium.webdriver.support.select import Select

from base.basePage import BasePage
from locators.locators import home_locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def choose_category(self, text):
        self.locate_element(home_locators.CATEGORY_SHOP).click()
        sleep(5)
        x = self.locate_select_element(home_locators.CATEGORY_SHOP)
        pass