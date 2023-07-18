from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Chrome()
url=("https://www.instagram.com/")
browser.get(url)
time.sleep(3)
inpusername=browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
inppassword=browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

inpusername.send_keys("USERNAME")

inppassword.send_keys("PASSWORD")
login=browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]")
login.click()
time.sleep(7)
time.sleep(150)
browser.close()