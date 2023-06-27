from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Google:

    def __init__(self, title) -> None:
        self.title = title
        self.url = "https://www.google.com.tr/?hl=tr"
        self.driver = webdriver.Chrome()
        self.git = self.driver.get(self.url)
        self.driver.maximize_window()

    def check_title(self):
        if self.driver.find_element(By.XPATH, "/html/head/title").text == self.title:
            print("Title is correct")
        else:
            print("Title is incorrect")


google = Google("Google")
google.check_title()
