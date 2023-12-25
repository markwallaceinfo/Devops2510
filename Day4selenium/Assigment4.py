import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Question1
driver = webdriver.Chrome()
driver1 = webdriver.firefox()
driver.get("https://www.amazon.com")
driver1.get("https://www.ebay.com")

#Question2
title = driver.title
print(title)
driver.refresh()
if title == driver.title:
    print("the title is the same")
else:
    print("wrong title")

#Question3
# Yes all the element is the same in all browser


#Question4
driver.get("https://translate.google.com")
driver.find_element(By.ID,value="").send_keys("")

#Question5
driver.get("https://www.youtube.com/")
ele = driver.find_element(By.ID,value='')
ele.click()


driver.get("")
song = driver.find_element(By.ID,value="")
song.send_keys("")

song1 = driver.find_element(By.ID,value="")
song1.send_keys("")
song1.click()


#Question6
driver.get("https://translate.google.com/")
a = driver.find_element(By.CLASS_NAME,value='')
c = driver.find_element(By.XPATH,value='')
d = driver.find_element(By.LINK_TEXT,value='')

#Question7
driver.get('https://www.facebook.com/')
email_field = driver.find_element(By.NAME,value='email')
email_field.send_keys('email_address')
pass_word = driver.find_element(By.ID,value='passContainer')
pass_word.send_keys('xyz')
login_button = driver.find_element(By.NAME, value='login')
login_button.click()


#Question8 challeges
driver.get('https://www.facebook.com/')
driver.delete_all_cookies()
el = driver.get_cookies()
print(el)

#Question9
driver.get('https://github.com/')
user_name = driver.find_element(By.ID,value='login')
user_name.send_keys('adbd')
pass_word = driver.find_element(By.ID,value='password')
pass_word.send_keys('ad')
sign_button = driver.find_element(By.NAME, value='commit')
sign_button.click()
repo_search = driver.find_element(By.CLASS_NAME,value='mt-2 mb-3')
repo_search.send_keys('selenium')
repo_search.send_keys(Keys.ENTER)


















