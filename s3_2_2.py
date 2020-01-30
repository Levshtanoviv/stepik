import unittest

from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(executable_path='C:/SDET/chromedriver/chromedriver.exe')
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        inputFirstName = browser.find_element_by_css_selector(".form-group:nth-child(1) input[type]")
        inputFirstName.send_keys("fff")

        inputLastName = browser.find_element_by_css_selector(".form-group:nth-child(2) input[type]")
        inputLastName.send_keys("fff")

        inputEmailName = browser.find_element_by_css_selector(".form-group:nth-child(3) input[type]")
        inputEmailName.send_keys("fff")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        # time.sleep(10)
        # # закрываем браузер после всех манипуляций
        # browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(executable_path='C:/SDET/chromedriver/chromedriver.exe')
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        inputFirstName = browser.find_element_by_css_selector(".form-group:nth-child(1) input[type]")
        inputFirstName.send_keys("fff")

        inputLastName = browser.find_element_by_css_selector(".form-group:nth-child(2) input[type]")
        inputLastName.send_keys("fff")

        inputEmailName = browser.find_element_by_css_selector(".form-group:nth-child(3) input[type]")
        inputEmailName.send_keys("fff")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        # time.sleep(10)
        # # закрываем браузер после всех манипуляций
        # browser.quit()
if __name__ == "__main__":
    unittest.main()