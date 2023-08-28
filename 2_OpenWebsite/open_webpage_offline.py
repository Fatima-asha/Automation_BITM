from selenium import webdriver


def open_webpage_online():
    driver = webdriver.Firefox(executable_path="G:\\SQA Class\\geckodriver-v0.32.2-win64"
                                               "\\geckodriver.exe")
    driver.get("file:///G:/SQA Class/your store/Your Store.html")
    driver.close()




open_webpage_online()
