import time
import self as self
from selenium import webdriver
from selenium.webdriver.remote import webelement
from pages import base


driver = webdriver.Chrome('/Users/admin/drivers/chromedriver')
driver.get('https://ecos.am/en/user/login')
time.sleep(2)  # Let the user actually see something!
search_box = driver.find_element_by_name('email')
search_box.send_keys('ek@ecos.am')
search_box = driver.find_element_by_name('password')
search_box.send_keys('AsZxdc123')
driver.execute_script("document.getElementById('button--log-in').disabled = false")
#search_box = driver.find_element_by_id(id='button--log-in')
search_box = driver.find_element_by_id('button--log-in').click()
#search_box.submit()
time.sleep(2)  # Let the user actually see something!

driver.quit()