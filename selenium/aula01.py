from selenium import webdriver
from icecream import ic

driver = webdriver.Chrome()

driver.get('http://phptest.test/selenium01.php')
ic(driver.title)

driver.close()