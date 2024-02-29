from selenium.webdriver.common.by import By
import allure


def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()

def test_button_exist2(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()

    #111