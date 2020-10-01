import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
 
@pytest.mark.parametrize('url', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_find_answer(browser, url):
    link = f"https://stepik.org/lesson/236{url}/step/1"
    browser.get(link)
    time.sleep(7)
    answer = str(math.log(int(time.time())))
    area = browser.find_element_by_css_selector("textarea")
    area.send_keys(answer)
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    time.sleep(3)
    res = browser.find_element_by_css_selector("pre.smart-hints__hint")
    if res != "Correct!":
        text = res.text
        print(text)