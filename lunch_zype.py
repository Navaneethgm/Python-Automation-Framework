from appium import webdriver
from appium.options.android import UiAutomator2Options
import time


def launch_app():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version="14.0"
    options.device_name = "RZCX50MH9YE"
    options.app_package = "com.zype.mobile.stage"
    options.app_activity = "com.zype.mobile.MainActivity"
    options.no_reset= False
    options.automation_name="UiAutomator2"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    driver.implicitly_wait(10)
    print("App launched successfully")   
    return driver


# driver.find_element("accessibility id","Create Account").click()
# print("clicked on create button")
# Is_displayed=driver.find_element("class name","android.widget.EditText").is_displayed()

# driver.find_element("accessibility id","Next").click()
# error_msg=driver.find_element("xpath","//android.widget.TextView[@resource-id='testCheckErrorText']").is_displayed()
# if error_msg==True:
#     print("Error msg displayed")
# else:
#     print("Error msg not displayed")
# if Is_displayed==True:
#     print("Element present")
# else:
#     print("Element not present")

# time.sleep(25)

# driver.quit()


# import math

# print(math.floor(2406.7752))
# print(round(2046.7752))