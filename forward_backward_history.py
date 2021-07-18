from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "E:\HusseinPrivate\Automation\Drivers\chromedriver.exe")

driver.get("https://facebook.com") #opens facebook.com

print(driver.title) #title of facebook.com page

driver.get("https://instagram.com") # opens instagram.com after facebook.com

print(driver.title)

driver.back() #navigates to the previous page
driver.forward() #navigates to the page forward

print(driver.title)
