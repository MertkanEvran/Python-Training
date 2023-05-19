from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.selenium.dev/documentation/webdriver/browsers/chrome/"
driver.get(url)

input()