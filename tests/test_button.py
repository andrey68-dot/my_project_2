from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_button_exits(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()