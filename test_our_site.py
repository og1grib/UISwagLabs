from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

driver.get(URL)

input_username = driver.find_element(By.NAME, 'user-name')
input_username.send_keys(USERNAME)

input_password = driver.find_element(By.NAME, 'password')
input_password.send_keys(PASSWORD)

button_login = driver.find_element(By.XPATH, '//input [@ type="submit"]')
button_login.click()

driver.quit()