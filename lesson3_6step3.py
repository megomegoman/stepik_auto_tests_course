import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.mark.parametrize("step", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_aliens(step, browser):
    link = f"https://stepik.org/lesson/{step}/step/1"
    browser.get(link)
    browser.find_element(By.TAG_NAME, "textarea").send_keys(math.log(int(time.time())))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))).click()
    answer = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    assert answer.text == "Correct!", "'Correct!' not in feedback"

