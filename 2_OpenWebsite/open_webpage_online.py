from selenium import webdriver


def open_webpage_online():
    driver = webdriver.Firefox(executable_path="G:\\SQA Class\\geckodriver-v0.32.2-win64"
                                               "\\geckodriver.exe")
    driver.get("https://google.com")
    driver.close()


open_webpage_online()
