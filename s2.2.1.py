import math
import time
from selenium.webdriver.support.ui import Select

from selenium import webdriver

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome(executable_path='C:/SDET/chromedriver/chromedriver.exe')
browser.get(link)


def calc(x, y):
    return str(int(x) + int(y))


try:
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    sum = calc(x, y)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(sum)
    # select.select_by_value("1")  # ищем элемент с текстом "Python"
    #
    # input = browser.find_element_by_id("answer")
    # input.send_keys(y)
    #
    # checkbox = browser.find_element_by_id("robotCheckbox")
    # checkbox.click()
    #
    # radiobutton = browser.find_element_by_id("robotsRule")
    # radiobutton.click()
    #
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
