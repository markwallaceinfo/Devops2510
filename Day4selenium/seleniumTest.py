import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://translate.google.com")

print(driver.current_url)
print(driver.title)
# print(driver.page_source)
driver.close()  # This will close your current browser
driver.quit()  # This will close all your windows that are open
driver.back()
driver.refresh()

time.sleep(5)
driver.find_element(By.CLASS_NAME, value="er8xn").send_keys("you")
driver.find_element(By.CLASS_NAME, value="er8xn").send_keys(Keys.ARROW_DOWN)
driver.find_element(By.CLASS_NAME, value="er8xn").click()
ele = driver.find_element(By.CLASS_NAME, value="er8xn")
ele.click()

ele.send_keys("yuiu")
ele.clear()
if ele.is_enabled():
    ele.click()




# driver.find_element(By.XPATH)
# //*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]

# driver = webdriver.Chrome(service=Service("/Users/danielgotlieb/Downloads/chromedriver"))
