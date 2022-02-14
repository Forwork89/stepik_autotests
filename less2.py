import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome(executable_path='C:\\Users\\YK\\pythonProject\\test_p\\chromedriver\\chromedriver.exe')
    browser.get(link)
    button = browser.find_element(By.XPATH, '//*[@id="submit_button"]')
    button.click()

finally:
    time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
