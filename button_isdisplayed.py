# button_isdisplayed.py
from lunch_zype import launch_app
from appium.webdriver.common.appiumby import AppiumBy
import time
def is_displayed(driver):
    try:
        create_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create Account").is_displayed()
        login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Log in").is_displayed()
        
        if create_button and login_button:
            print("Create button and Login button are displayed")
            return True
        else:
            print("Buttons not displayed")
            return False
        
    except Exception as e:
        print(f"Error finding buttons: {e}")
        return False
    

def swipe_by_coordinates(driver, start_x, start_y, end_x, end_y, direction, duration=800, percent=0.5):
    """
    Swipe using coordinates and a valid swipe area (Appium 2.x requirement).
    """
    # Get screen size
    size = driver.get_window_size()
    width = size["width"]
    height = size["height"]

    # Define full-screen swipe area
    left = 0
    top = 0
    swipe_width = width
    swipe_height = height

    driver.execute_script(
        "mobile: swipeGesture",
        {
            "left": left,
            "top": top,
            "width": swipe_width,
            "height": swipe_height,
            "direction": direction,   # mandatory
            "startX": start_x,
            "startY": start_y,
            "endX": end_x,
            "endY": end_y,
            "percent": percent,       # mandatory
            "speed": duration
        }
    )






if __name__=="__main__":
    driver=launch_app()
    is_displayed(driver)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Create Account").click()
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Read More...']").click()
    swipe_by_coordinates(driver,462,1972,462,1253,direction="up")
    driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Read Less...']").click()
    time.sleep(3)

    
    driver.quit()
