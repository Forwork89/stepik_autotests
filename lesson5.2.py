from random import random

import letters as letters
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("input[type=text]")
    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
