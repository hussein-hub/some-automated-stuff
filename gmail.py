from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path ='E:/HusseinPrivate/Automation/Drivers/chromedriver.exe')

driver.get("https://gmail.com")
time.sleep(3)
driver.find_element_by_name("identifier").send_keys("your email")
driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("your password")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id=':jm']/div/div").click()
time.sleep(3)
driver.find_element_by_name("to").send_keys("recievers email")
time.sleep(2)
driver.find_element_by_id(":px").send_keys("This is an automated mail sent using selenium")
time.sleep(4)
driver.find_element_by_xpath("//*[@id=':w0']").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/div[2]/div/a/img").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='gb_71']").click()
time.sleep(3)
driver.quit()