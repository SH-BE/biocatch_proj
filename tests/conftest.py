import os
import pytest as pytest
from selenium import webdriver


def set_chrome_options():
    options = webdriver.ChromeOptions()
    # to make the automation undetectable
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return options


@pytest.fixture(scope="class")
def setup(request):
    path = os.path.join(os.path.dirname(os.path.abspath('')), 'assets\\chromedriver.exe')
    driver = webdriver.Chrome(executable_path=path, chrome_options=set_chrome_options())
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
