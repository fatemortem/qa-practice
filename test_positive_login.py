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

@pytest.mark.positive
def test_login_succes(browser):
    browser.get("https://the-internet.herokuapp.com/login")

    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
    browser.find_element(By.ID, "username").send_keys("tomsmith")
    browser.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.radius")))
    browser.find_element(By.CSS_SELECTOR, "button.radius").click()

    message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "flash"))
    ).text

    assert "You logged into a secure area!" in message, "Успешный вход не прошёл"