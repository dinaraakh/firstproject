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
search_field.send_keys('помидор')
search_field.send_keys(Keys.RETURN)

time.sleep(8)
assert "Помидор – описание, польза и вред, калорийность ..." in driver.page_source
time.sleep(5)
driver.close()

pass
