import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("step", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_aliens(step, browser):
    link = f"https://stepik.org/lesson/{step}/step/1"
    browser.get(link)
    browser.find_element(By.)