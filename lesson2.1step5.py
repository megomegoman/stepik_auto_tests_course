from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    elements = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = elements.get_attribute("valuex")
    inp = browser.find_element(By.CSS_SELECTOR, "#answer")
    inp.send_keys(calc(x))
    chekbox = browser.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    chekbox.click()
    radiobut = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobut.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла