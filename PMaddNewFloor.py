from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\geckodriver.exe")
browser.get('https://anoeye.com/login')

browser.find_element_by_name('email').send_keys("engrfarkhanda6@gmail.com")
browser.find_element_by_name('password').send_keys("pak1234")
browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[5]/button').click()
print("Logged in Successfully")
browser.get("https://anoeye.com/")
property_management = browser.find_element_by_class_name('kt-portlet__body')
if property_management.is_displayed:
    property_management.click()
    print('now switch to add floor page')
    browser.get('https://anoeye.com/PropertyManagement')
    add_floor=browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div/div/div/h3/strong")
    if add_floor.is_displayed():
        add_floor.click()
        floor_name = 4
        #floor_area = 45
        area_rent= 44
        floor_cam_area = 25
        floor_descp = 'Trying to test floor description'
        browser.find_element_by_name('floor_name').send_keys(floor_name)
        #browser.find_element_by_name('floor_area').send_keys(floor_area)
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[3]/div/form/div/div[2]/div[3]/div/div/label[2]/span").click()
        browser.find_element_by_name('floor_cam_area').send_keys(floor_cam_area)
        browser.find_element_by_name('common_area_rent').send_keys(area_rent)

        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[3]/div/form/div/div[2]/div[5]/div[2]/div/div/label[1]/span").click()
        browser.find_element_by_name('floor_descp').send_keys(floor_descp)

        floor_added=browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[3]/div/form/div/div[3]/button[2]")
        print("floor added")

