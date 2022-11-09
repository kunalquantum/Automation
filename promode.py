import time
import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('C:\chromedriver.exe')

browser.implicitly_wait(2)
browser.maximize_window()
browser.get('https://www.google.com/maps/@19.1168512,72.8858624,12z')
se=browser.find_element(By.XPATH,'//*[@id="searchbox"]')
se.click()
time.sleep(2)
se2=browser.find_element(By.XPATH,'//*[@aria-label="Search Google Maps"]')
se2.send_keys('new york')
time.sleep(2)
se3=browser.find_element(By.XPATH,'//button[@aria-label="Search"]')
se3.click()
time.sleep(2)
direction=browser.find_element(By.XPATH,'//button[@aria-label="Directions to New York"]')
direction.click()
time.sleep(2)
sour=browser.find_element(By.XPATH,'//input[@placeholder="Choose starting point, or click on the map..."]')
sour.send_keys('mumbai')
time.sleep(2)
flight=browser.find_element(By.XPATH,'//img[@aria-label="Flights"]')
flight.click()
layer=browser.find_element(By.XPATH,'//div[@class="scFIyc"]')
layer.click()

time.sleep(1)