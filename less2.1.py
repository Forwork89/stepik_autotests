import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome('C:\\Users\\YK\\pythonProject\\test_p\\chromedriver\\chromedriver.exe')
browser = webdriver.Edge(executable_path='C:\\Users\\YK\\pythonProject\\test_p\\edgedriver\\msedgedriver.exe')
time.sleep(3)
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()
