from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\chromedriver.exe")
driver=webdriver.Firefox(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\geckodriver.exe")
#driver=webdriver.Ie(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\IEDriverServer.exe")

driver.get("abc")
