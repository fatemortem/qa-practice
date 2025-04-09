import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from test_project.pages.login_page import LoginPage

CHROME_PATH = "E:/driver/chromedriver.exe"

@pytest.fixture
def browser():
    service = Service(CHROME_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_login_success(browser):
    login = LoginPage(browser)
    login.open()
    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    message = login.get_message()
    assert "logged into a secure area!" in message

def test_login_invalid_credentials(browser):
    login = LoginPage(browser)
    login.open()
    login.enter_username("wronguser")
    login.enter_password("wrongpassword")
    login.click_login()

    message = login.get_message()
    assert "invalid" in message

def test_login_empty_field(browser):
    login = LoginPage(browser)
    login.open()
    login.click_login()

    message = login.get_message()
    assert "invalid" in message

def test_login_only_username(browser):
    login = LoginPage(browser)
    login.open()
    login.enter_username("tomsmith")
    login.click_login()

    message = login.get_message()
    assert "invalid" in message

def test_login_only_password(browser):
    login = LoginPage(browser)
    login.open()
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    message = login.get_message()
    assert "invalid" in message