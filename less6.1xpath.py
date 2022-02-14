import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome(executable_path='C:\\Users\\YK\\pythonProject\\test_p\\chromedriver\\chromedriver.exe')

    driver.get(link)
    # time.sleep(20)
    input1 = driver.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_xpath("/html/body/div/form/div[2]/input")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_xpath('/html/body/div/form/div[3]/input')
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_xpath('//*[@id="country"]')
    input4.send_keys("Russia")
    button = driver.find_element_by_xpath('//*[@id="submit_button"]')
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(3)
    driver.quit()
