from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
  link = "http://suninjuly.github.io/execute_script.html"
  browser = webdriver.Chrome()
  browser.get(link)

 # Считать значение для переменной x
  def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

  x_element = browser.find_element_by_css_selector('#input_value')
  x = x_element.text
  y = calc(x)
  
  # Мой код, который заполняет поле
  input1 = browser.find_element_by_css_selector('#answer')
  input1.send_keys(y)  
  time.sleep(2)  
  # Мой код, который скролит
  button = browser.find_element_by_tag_name("button")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  button.click()

  # Мой код, который отмечает чекбокс    
  option1 = browser.find_element_by_css_selector("#robotCheckbox")
  option1.click()
  # Мой код, который отмечает радиобатн
  option1 = browser.find_element_by_css_selector("#robotsRule")
  option1.click()

  # Отправляем заполненную форму
  button = browser.find_element_by_xpath("/html/body/div/form/button")
  button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()