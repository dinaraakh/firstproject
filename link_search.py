import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path="./chromedriver"
)
options = Options()

driver.get("https://www.google.ru")

search_field = driver.find_element(By.NAME, "q")
search_field.send_keys('https://www.ikea.com/ru/ru/')
search_field.send_keys(Keys.RETURN)

assert "ИКЕА - официальный интернет-магазин мебели - IKEA" in driver.page_source
time.sleep(2)
driver.close()

pass