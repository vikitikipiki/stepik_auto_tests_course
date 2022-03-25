from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), text_="$100"))

#нажимаем на кнопку после того как цена 100
button = browser.find_element_by_css_selector("#book")
button.click()

#решаем пример
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

# Мой код, который заполняет поле
input1 = browser.find_element_by_css_selector('#answer')
input1.send_keys(y)

#нажимаем на кнопку
button = browser.find_element_by_css_selector("#solve")
button.click()
