from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    chekbox = browser.find_element_by_id('robotCheckbox')
    chekbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.get_attribute("robots")
    radiobutton.click()
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
