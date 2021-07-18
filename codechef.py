from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# SPECIFIES PATH TO THE EXE FILE FOR AUTOMATION TO WORK
driver = webdriver.Chrome(r'E:\Coding,Development\HusseinPrivate\Automation\Drivers')
# WILL .get METHOD WILL OPEN THE URL SPECIFIED IN THE DOUBLE INVERTED COMMA
driver.get("https://codechef.com")
# WILL RETURN TITLE OF THE PAGE OF ABOVE URL
# print(driver.title)
# print(driver.current_url) # url of current page
username = driver.find_element_by_id("edit-name")
password = driver.find_element_by_id("edit-pass")
username.send_keys("username")
password.send_keys("password")

driver.find_element_by_id("edit-submit").click()
# driver.findElement(By.xpath("//*[@id=;edit-name']")).sendKeys(hussein);

# driver.close() #closes one parent tab

# driver.quit() # closes all tabs that is the full window
