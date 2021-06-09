from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\chromedriver.exe")

driver.get("https://anoeye.com/login")
driver.find_element_by_name("email").send_keys("engrfarkhanda6@gmail.com")
driver.find_element_by_name("password").send_keys("haneen32303")
driver.find_element_by_xpath("//*[@id='kt_login']/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[5]/button").click()
