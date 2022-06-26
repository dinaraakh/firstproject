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

# search_field = driver.find_element(By.NAME, "q")
# time.sleep(5)
# search_field.send_keys('помидор')
# time.sleep(10)

search_botton = driver.find_element(By.NAME, "btnK")
time.sleep(10)
search_botton.click()


# assert "Помидор – описание, польза и вред, калорийность ..." in driver.page_source
driver.close()

pass