from selenium import webdriver
import time
import math

def y(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
# This is first example
    browser = webdriver.Chrome()
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")
    link = " http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_find = browser.find_element_by_id("input_value")
    x = x_find.text
    y = y(x)
    ans = browser.find_element_by_id("answer")
    ans.send_keys(y)
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 100);")
    
    
    robotCheck = browser.find_element_by_id("robotCheckbox")
    robotCheck.click()
    
    robotRadio = browser.find_element_by_id("robotsRule")
    robotRadio.click()
    
    button.click()
    
finally:
    time.sleep(20)
    browser.quit()