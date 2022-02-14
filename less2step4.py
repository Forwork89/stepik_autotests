import calc as calc
from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

"""Использовался драйвер Хрома"""

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    browser.execute_script("window.scrollBy(0, 150);")
    chekbox = browser.find_element_by_id('robotCheckbox')
    chekbox.click()
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
