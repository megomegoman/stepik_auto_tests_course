from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



class TestUniqSelectors():
    @pytest.mark.parametrize("site", ['1.html', '2.html'])
    def test_uniq1(self, browser, site):
        link = f"http://suninjuly.github.io/registration{site}"
        browser.get(link)
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
        assert welcome_text == "Congratulations! You have successfully registered!", "no registered"



if __name__ == '__main__':
    unittest.main()
