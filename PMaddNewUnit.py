from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\geckodriver.exe")
browser.get('https://anoeye.com/login')
browser.find_element_by_name('email').send_keys("engrfarkhanda6@gmail.com")
browser.find_element_by_name('password').send_keys("shaheer32303")
browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[5]/button').click()
print("Logged in Successfully")
browser.get("https://anoeye.com/")
property_management = browser.find_element_by_class_name('kt-portlet__body')
if property_management.is_displayed:
    property_management.click()
    print('now switch to add unit page')
    browser.get('https://anoeye.com/PropertyManagement')
    add_unit=browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[3]/div/div/div[4]/h3")
    if add_unit.is_displayed():
        add_unit.click()
        unit_name= 1
        unit_type= "Commercial"
        unit_size = 1000
        unit_rent = 234
        browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[4]/div/form/div/div[2]/div[1]/div[1]/div/input').send_keys(unit_name)
        browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[4]/div/form/div/div[2]/div[1]/div[2]/div/select').send_keys(unit_type)
        browser.find_element_by_id('unit_size').send_keys(unit_size)
        browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[4]/div/form/div/div[2]/div[2]/div[1]/div/input').send_keys(unit_rent)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[4]/div/form/div/div[3]/button[1]").click()
        print("unit added")

