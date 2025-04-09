import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROME_PATH ="E:/driver/chromedriver.exe"

@pytest.fixture
def browser():
    service = Service(CHROME_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()