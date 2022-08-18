from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login_function(username, password, driver):
    url = "https://instagram.com"
    driver.get(url)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Consenti cookie essenziali e facoltativi')]"))).click()
    name ="username"
    username_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, name)))
    username_input.send_keys(username)
    name= "password"
    username_input =WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, name)))
    username_input.send_keys(password)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Accedi')]"))).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Non ora')]"))).click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Non ora')]"))).click()
