import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_existence_button(browser):
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "Button not found"
    time.sleep(5)
