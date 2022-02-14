from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

try:
    driver = webdriver.Edge('C:\\Users\\YK\\pythonProject\\test_p\\edgedriver\\msedgedriver.exe')
    driver.get("http://suninjuly.github.io/simple_form_find_task.html")

    input1 = driver.find_element_by_class_name("form-control")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_id('country')
    input4.send_keys("Russia")
    button = driver.find_element_by_id("submit_button")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
