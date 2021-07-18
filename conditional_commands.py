from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "E:\HusseinPrivate\Automation\Drivers\chromedriver.exe")

driver.get("https://facebook.com")

# username = driver.find_element_by_name("email")
# print(username.is_displayed()) # returns true or false based on element status

# print(username.is_enabled()) 

driver.find_element_by_css_selector("input[name=email]").send_keys("9372593491")

driver.find_element_by_name("pass").send_keys("Hussein7860@#")

driver.find_element_by_xpath("//*[@id='u_0_b']").click()