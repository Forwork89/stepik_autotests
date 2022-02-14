import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/selects1.html"

# link2 = "http://suninjuly.github.io/selects2.html"


try:
    browser.get(link)
    n = browser.find_element_by_css_selector('#num1').text
    t = browser.find_element_by_css_selector('#num2').text
    x = int(n) + int(t)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(x))
    button = browser.find_element_by_class_name("btn.btn-default").click()

# browser.get(link2)
# val = *спойлер спрятан*
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_visible_text(*спойлер спрятан*)
# browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.quit()
