import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\chromedriver.exe")
browser=webdriver.Firefox(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\geckodriver.exe")
#driver=webdriver.Ie(executable_path="C:\\Users\\shehwar\\PycharmProjects\\SeleniumProject\\Drivers\\IEDriverServer.exe")

browser.get("https://")
browser.find_element_by_name('email').send_keys("tt@tt.com")
browser.find_element_by_name('password').send_keys("123456")
#browser.find_element_by_xpath('//button').click()
browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/div/div[2]/div[2]/form/div[5]/button').click()
print("Logged in Successfully")

browser.get("https://")
browser.find_element_by_id("basic-addon1").click()
print("Add new property form is being opened")
browser.find_element_by_name('building_name').send_keys("echelonone")
browser.find_element_by_name('property_area').send_keys("5000")
browser.find_element_by_name('building_address').send_keys("USA")
browser.find_element_by_name('city').send_keys("xyz")
browser.find_element_by_name('state').send_keys("abc")
browser.find_element_by_name('zipcode').send_keys("30")

browser.find_element_by_class_name("kt-input-icon").click()
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/form/div/div[3]/button[1]").click()

AddNewproperty="New property is added successfully"

result="web site is opened in all browsers"
fieldnames = ['Testcases', 'Actual Result']
# csv data
rows = [
    {'Testcases': result,
    'Actual Result': "Pass"},
    {'Testcases': AddNewproperty,
    'Actual Result': 'Pass'},
]

with open('count.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
f.close()
