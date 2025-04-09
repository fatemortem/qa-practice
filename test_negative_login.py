import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_PATH = "E:/driver/chromedriver.exe"

@pytest.fixture()
def browser():
    service = Service(CHROME_PATH)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.mark.negative
def test_login_invalid_credentials(browser):
    browser.get("https://the-internet.herokuapp.com/login")

    browser.find_element(By.ID, "username").send_keys("wronguser")
    browser.find_element(By.ID, "password").send_keys("wrongpassword")
    browser.find_element(By.CSS_SELECTOR, "button.radius").click()

    error_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "flash"))
    ).text

    assert  "Your username is invalid" in error_message, "Ошибка входа не отобразилась"