from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

driver.get("C:\Users\USERi\Desktop\SAL")

napp = driver.find_element_by_name("choice")
val = 2
napp.send_keys(val)