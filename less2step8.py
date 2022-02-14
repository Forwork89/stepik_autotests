import time
import math

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()
    browser.switch_to.alert.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
