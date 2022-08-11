from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    browser.execute_script("window.scrollBy(0, 200);")
    inp = browser.find_element(By.CSS_SELECTOR, "#answer")
    inp.send_keys(calc(int(x.text)))
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