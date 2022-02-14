from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver

try:
    driver = webdriver.Chrome('C:\\Users\\YK\\pythonProject\\test_p\\chromedriver\\chromedriver.exe')
    driver.get("https://suninjuly.github.io/find_xpath_form")
    wait = WebDriverWait(driver, 1)
    input1 = driver.find_element_by_xpath("/html/body/div/form/div[1]/input")
    input1.send_keys("Ivan")
    input2 = driver.find_element_by_xpath("/html/body/div/form/div[2]/input")
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_xpath('/html/body/div/form/div[3]/input')
    input3.send_keys("Smolensk")
    input4 = driver.find_element_by_xpath('//*[@id="country"]')
    input4.send_keys("Russia")
    button = driver.find_element_by_xpath('//button[@type="submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    driver.quit()

    # не забываем оставить пустую строку в конце файла
