from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


website = 'https://www.scconline.com/'
path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(website)

search = driver.find_elements(by=By.LINK_TEXT , value='LOGIN')

search[0].click()

