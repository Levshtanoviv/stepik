import math
import time


from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
try:
    button = browser.find_element_by_css_selector("button.btn").click()

    confirm = browser.switch_to_alert()
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    input = browser.find_element_by_id("answer").send_keys(y)

    button = browser.find_element_by_css_selector("button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
