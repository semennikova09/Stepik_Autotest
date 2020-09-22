from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    ans = browser.find_element_by_id("answer")
    ans.send_keys(y)
    
    robotCheck = browser.find_element_by_id("robotCheckbox")
    robotCheck.click()
    
    robotRadio = browser.find_element_by_id("robotsRule")
    robotRadio.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    time.sleep(30)
    browser.quit()
    
    