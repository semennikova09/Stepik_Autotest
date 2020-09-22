from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    browser.execute_script("window.scrollBy(0, 100);")
    
    x_val = browser.find_element_by_id("input_value")
    x = x_val.text
    y = calc(x)
    
    ans = browser.find_element_by_id("answer")
    ans.send_keys(y)
    
    button = browser.find_element_by_id("solve")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()