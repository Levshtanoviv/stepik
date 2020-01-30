import math

from selenium import webdriver
import time


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome(executable_path='C:/SDET/chromedriver/chromedriver.exe')
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    xLabel = browser.find_element_by_css_selector("img[src]")
    x = xLabel.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

