from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    name = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    name.send_keys("Dmitryiy")
    last_name = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    last_name.send_keys("Rykov")
    my_email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    my_email.send_keys('dr@yandex.ru')
    file = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    pathabs = os.path.abspath(os.path.dirname(__file__))
    pathfile = os.path.join(pathabs, "output.txt")
    file.send_keys(pathfile)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить
