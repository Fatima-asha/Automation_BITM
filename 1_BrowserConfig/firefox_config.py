from selenium import webdriver


def firefox_launch():
    driver = webdriver.Firefox(executable_path="G:\\SQA Class\\geckodriver-v0.32.2-win64"
                                               "\\geckodriver.exe")

    driver.close()


firefox_launch()
