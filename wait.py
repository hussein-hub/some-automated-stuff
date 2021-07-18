from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "E:/HusseinPrivate/Automation/Drivers/chromedriver.exe")

driver.get("https://codechef.com")

# assert "Programming Competition,Programming Contest,Online Computer Programming" in driver.title

username = driver.find_element_by_name("name")
password = driver.find_element_by_name("pass")
username.send_keys("your username")
password.send_keys("your password")

driver.find_element_by_name("op").click()
driver.find_element_by_xpath("/html/body/section/div/div/ul/li[1]/span[2]/a").click()
driver.find_element_by_xpath("/html/body/section/div/div/ul/li[1]/span[2]/ul/li[1]/a").click()

