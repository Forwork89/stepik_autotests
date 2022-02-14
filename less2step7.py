from selenium import webdriver
import time
import math
import os
from selenium.webdriver.common.by import By

"""Использовался драйвер Хрома"""

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name('firstname').send_keys('Ivan')
    browser.find_element_by_name('lastname').send_keys('Ivanov')
    browser.find_element_by_name('email').send_keys('@ivanov.com')
    element = browser.find_element_by_id('file')
    element.send_keys('C:\\Users\\YK\\pythonProject\\test_p\\fist.txt')
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
finally:
    time.sleep(3)
    browser.quit()
