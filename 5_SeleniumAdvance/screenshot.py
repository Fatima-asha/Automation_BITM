from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(4)
driver.get("https://google.com")

driver.get_screenshot_as_file("G:\\SQA Class\\Automation all\\Automation\\Screenshot\\Google.png")

driver.close()

