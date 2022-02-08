from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.__driver = driver

    def locate_element(self, locator=None, timeout=5):
        wait = WebDriverWait(self.__driver, timeout)
        element = None
        if locator[0] == "id":
            element = wait.until(lambda x: x.find_element_by_id(locator[1]))
        elif locator[0] == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locator[1]))
        elif locator[0] == "accessibility_id":
            element = wait.until(lambda x: x.find_element_by_accessibility_id(locator[1]))
        elif locator[0] == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath(locator[1]))
        elif locator[0] == "css_selector":
            element = wait.until(lambda x: x.find_element_by_css_selector(locator[1]))
        elif locator[0] == "link_text":
            element = wait.until(lambda x: x.find_element_by_link_text(locator[1]))
        elif locator[0] == "partial_link_text":
            element = wait.until(lambda x: x.find_element_by_partial_link_text(locator[1]))
        elif locator[0] == "name":
            element = wait.until(lambda x: x.find_element_by_name(locator[1]))
        elif locator[0] == "tag_name":
            element = wait.until(lambda x: x.find_element_by_tag_name(locator[1]))
        elif locator[0] == "ios_class_chain":
            element = wait.until(lambda x: x.find_element_by_ios_class_chain(locator[1]))
        elif locator[0] == "ios_predicate_string":
            element = wait.until(lambda x: x.find_element_by_ios_predicate(locator[1]))
        return element

    def locate_select_element(self, locator):
        return Select(self.locate_element(locator))