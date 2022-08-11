from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestUniqSelectors(unittest.TestCase):
    def test_uniq1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        element1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input")
        element1.send_keys("Mark")
        element2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input")
        element2.send_keys("Ruffalo")
        element3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input")
        element3.send_keys("Mark@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "no registered")

    def test_uniq2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        element1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input")
        element1.send_keys("Mark")
        element2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input")
        element2.send_keys("Ruffalo")
        element3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input")
        element3.send_keys("Mark@yandex.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "no registered")

if __name__ == '__main__':
    unittest.main()
