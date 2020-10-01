import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_add_to_basket(browser):
    browser.get(link)
    button_cart = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert button_cart > 0