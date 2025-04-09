from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service("E:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

sleep(2)

message = driver.find_element(By.ID, "flash").text
print("Результат входа:", message)

driver.quit()

