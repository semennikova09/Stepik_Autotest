from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects2.html")
    number1 = browser.find_element_by_id("num1")
    num1 = number1.text
    number2 = browser.find_element_by_id("num2")
    num2 = number2.text
    sum = int(num1) + int(num2)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    time.sleep(30)
    browser.quit()
    