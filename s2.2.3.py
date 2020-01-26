import math
import os
import time


from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
try:

    inputFirstName = browser.find_element_by_name("firstname").send_keys("Иван")
    inputLastName = browser.find_element_by_name("lastname").send_keys("Левштанов")
    inputEmail = browser.find_element_by_name("email").send_keys("Email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    element = browser.find_element_by_id("file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
