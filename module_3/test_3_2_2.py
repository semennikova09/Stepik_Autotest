import unittest
from selenium import webdriver
import time

class TestWeb(unittest.TestCase):
    def test_webSite1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        element1 = browser.find_element_by_css_selector("div.first_block input.first")
        element1.send_keys("Ans")
        element2 = browser.find_element_by_css_selector("div.first_block input.second")
        element2.send_keys("Ans")
        element3 = browser.find_element_by_css_selector("div.first_block input.third")
        element3.send_keys("Ans")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Messages should be equal")

        time.sleep(20)
        browser.quit()

    def test_webSite2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        element1 = browser.find_element_by_css_selector("div.first_block input.first")
        element1.send_keys("Ans")
        element2 = browser.find_element_by_css_selector("div.first_block input.second")
        element2.send_keys("Ans")
        element3 = browser.find_element_by_css_selector("div.first_block input.third")
        element3.send_keys("Ans")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Messages should be equal")

        time.sleep(20)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
