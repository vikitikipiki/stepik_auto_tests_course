from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5) 

 # open get-in.com
browser.get('http://suninjuly.github.io/cats.html')

 # log in get-in.com
browser.find_element_by_id("button").click()
