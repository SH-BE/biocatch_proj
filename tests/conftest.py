import os

import pytest as pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    path = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(path, "../assets/chromedriver")
    driver = webdriver.Chrome(executable_path=file)
    driver.maximize_window()
    driver.get('https://www.ebay.com/')
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
