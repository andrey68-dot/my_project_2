import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture()
def browser():
    option = Options()
    option.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=option)
    return chrome_browser
#11111
