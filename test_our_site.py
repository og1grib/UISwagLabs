from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def open_page(driver, url):
    driver.get(url)

def element_send_keys_login(driver):
    input_username = driver.find_element(By.NAME, 'user-name')
    input_username.send_keys(USERNAME)

def element_send_keys_password(driver):
    input_password = driver.find_element(By.NAME, 'password')
    input_password.send_keys(PASSWORD)

def click_button_login(driver):
    button_login = driver.find_element(By.XPATH, '//input [@ type="submit"]')
    button_login.click()

driver = get_driver()
open_page(driver, URL)
element_send_keys_login(driver)
element_send_keys_password(driver)
click_button_login(driver)
driver.quit()