from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com/")

#open tab
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 

# Load a page 
driver.get('http://stackoverflow.com/')


# Open a new window
driver.execute_script("window.open('https://www.flipkart.com/');")
# Switch to the new window and open new URL
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.google.co.in/')
# Switching to old tab
driver.switch_to.window(driver.window_handles[0])

# Load a page 
# driver.get('https://www.google.co.in/')
# Make the tests...

# # close the tab
# # (Keys.CONTROL + 'w') on other OSs.
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 


# driver.quit()