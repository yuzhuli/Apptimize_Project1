import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import uuid

# Open Apptimize Page
driver = webdriver.Chrome('./chromedriver') 
driver.get("https://apptimize.com/")
time.sleep(1)

# Sign up for free trial
driver.find_element_by_link_text('TRY FOR FREE').click()

# Fill the form and submit
fname = driver.find_element_by_id('fname')
fname.send_keys("myFirstName")
lname = driver.find_element_by_id('lname')
lname.send_keys("myLastName")
email = driver.find_element_by_id('email')
emailAdd = "liyuzhumail+" + str(uuid.uuid4()) + "@gmail.com"
email.send_keys(emailAdd)
company = driver.find_element_by_id("company")
company.send_keys("Apptimize Candidate")
password = driver.find_element_by_id('password')
password.send_keys("TestTest1234!")
driver.find_element_by_id('eula').click()
driver.find_element_by_id("submit").click()
time.sleep(2)

# Create an iOS app
appName = driver.find_element_by_id("zet-app-name")
appName.send_keys("MyTestApp")
driver.find_element_by_id("zet-icon-ios").click()
driver.find_element_by_id("zet-create-app").click()
time.sleep(2)

# Sign out
driver.find_element_by_class_name('fa-caret-down').click()
time.sleep(2)
driver.find_element_by_id("zet-navbar-signout").click()

driver.close()
