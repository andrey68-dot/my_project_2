from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture()
def browser():
    option = Options()
    option.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=option)
    return chrome_browser

def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()

#Всем привет 11111