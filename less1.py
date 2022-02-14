import time
from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\YK\\pythonProject\\test_p\\chromedriver\\chromedriver.exe')
time.sleep(5)
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)
submit_button = driver.find_elements_by_css_selector(".submit-submission")
submit_button.click()
time.sleep(5)
driver.quit()
