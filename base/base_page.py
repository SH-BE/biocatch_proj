from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def locate_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_element(locator[0], locator[1]))

    def locate_element_until_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_url(self, url, timeout=5):
        self.driver.implicitly_wait(10)
        try:
            return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))
        except TimeoutException:
            return False

    def locate_elements(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(lambda x: x.find_elements(locator[0], locator[1]))

    def locate_select_element(self, locator):
        return Select(self.locate_element(locator))

    def send_keys_element(self, locator, value):
        element = self.locate_element(locator)
        element.send_keys(value)
        return element

    def send_keys_element_with_enter(self, locator, value):
        element = self.send_keys_element(locator, value)
        element.send_keys(Keys.ENTER)

    def click_element(self, locator):
        self.locate_element_until_clickable(locator).click()

    def click_element_instance(self, element):
        element.click()

    def try_click_element(self, locator):
        try:
            self.locate_element_until_clickable(locator).click()
            return True
        except TimeoutException:
            return False

    def get_element_text(self, locator):
        return self.locate_element_until_clickable(locator).text

    def switch_to_next_window(self):
        self.driver.implicitly_wait(10)
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_and_go_back_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def is_partial_url(self, partial_url, timeout=5):
        self.driver.implicitly_wait(10)
        try:
            return WebDriverWait(self.driver, timeout).until(EC.url_contains(partial_url))
        except TimeoutException:
            return False
