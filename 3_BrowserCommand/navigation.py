from selenium import webdriver
import time


def navigate():
    driver = webdriver.Firefox(executable_path="G:\\SQA Class\\geckodriver-v0.32.2-win64"
                                               "\\geckodriver.exe")
    driver.get("https://demo.opencart.com/index.php")
    time.sleep(3)

    driver.get("https://google.com/")
    time.sleep(3)

    driver.back()
    time.sleep(3)

    driver.forward()
    time.sleep(3)

    driver.refresh()

    driver.close()


navigate()
