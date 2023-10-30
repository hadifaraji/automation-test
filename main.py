from selenium import webdriver
from time import sleep


url = "https://www.digikala.com/"
driver = webdriver.Chrome()
driver.get(url)
sleep(2)