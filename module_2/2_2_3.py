from selenium import webdriver
import math
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    elem_name = browser.find_element_by_name("firstname")
    elem_name.send_keys("Ans")
    elem_last = browser.find_element_by_name("lastname")
    elem_last.send_keys("Ans")
    elem_email = browser.find_element_by_name("email")
    elem_email.send_keys("Ans")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'New.txt')
    
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    time.sleep(20)
    browser.quit()
    