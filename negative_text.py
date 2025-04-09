from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service("E:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("wronguser")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

sleep(2)

message = driver.find_element(By.ID, "flash").text
print("Сайт ответил:", message)

if "Your username is invalid!" in message:
    print("Тест пройден - ошибка отображается правильно")
else:
    print("Тест провален - сообщение не соответствует ожиданиям")

    driver.quit()