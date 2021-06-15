from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\geckodriver.exe")
browser.get('abc')

browser.find_element_by_name('email').send_keys("xyz")
browser.find_element_by_name('password').send_keys("pak1234")
#browser.find_element_by_xpath('//button').click()
browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[5]/button').click()
print("Logged in Successfully")

browser.get("https://anoeye.com/")
browser.find_element_by_id("basic-addon1").click()
print("Add new property form is being opened")
browser.find_element_by_name('building_name').send_keys("echelonone")
browser.find_element_by_name('property_area').send_keys("5000")
browser.find_element_by_name('building_address').send_keys("USA")
browser.find_element_by_name('city').send_keys("xyz")
browser.find_element_by_name('state').send_keys("abc")
browser.find_element_by_name('zipcode').send_keys("30")

browser.find_element_by_class_name("kt-input-icon").click()
browser.find_element_by_id("sbmtbtn").click()

print("New property is added successfully")
