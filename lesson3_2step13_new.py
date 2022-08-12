from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest
import time

@pytest.fixture
def test_page():
    browser = webdriver.Chrome()
    yield browser

    browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input").send_keys("Mark")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input").send_keys("Ruffalo")
    browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input").send_keys("Mark@yandex.ru")

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "no registered")


class TestUniqSelectors():
    def test_uniq1(self, browser):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

    def test_uniq2(self, browser):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)


if __name__ == '__main__':
    unittest.main()
