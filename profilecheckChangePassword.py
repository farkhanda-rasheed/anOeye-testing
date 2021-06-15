from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\geckodriver.exe")
browser.get('https://anoeye.com/login')

browser.find_element_by_name('email').send_keys("engrfarkhanda6@gmail.com")
browser.find_element_by_name('password').send_keys("haneen32303")
browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[5]/button').click()
print("Logged in Successfully")
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div[4]/div[1]/div/span[2]").click()
time.sleep(3)

browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div[4]/div[2]/div[2]/a/div[2]/div").click()
time.sleep(2)
print("profile page appears")
browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div[2]/a[2]/span/span[2]").click()
browser.find_element_by_name("old_password").send_keys("haneen32303")
browser.find_element_by_name("password").send_keys("pak1234")
browser.find_element_by_name("confirm_password").send_keys("pak1234")
browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/form/div[2]/div/div/div[2]/button[1]").click()

print("password changed")

