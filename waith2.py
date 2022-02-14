from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    time.sleep(2)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    static_message = "Verification was successful!"

    assert "Verification was successful!" in message.text, "Сообщение не то, что надо"

finally:
    time.sleep(2)
browser.quit()
