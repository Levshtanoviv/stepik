import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome(executable_path='C:/SDET/chromedriver/chromedriver.exe')
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
try:

    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    button = browser.find_element_by_tag_name("button")
    input = browser.find_element_by_id("answer").send_keys(y)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']").click()

    button.click()
    assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
