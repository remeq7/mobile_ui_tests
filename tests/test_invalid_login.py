from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import init_driver
import time

def test_invalid_login():
    driver = init_driver("apk/TheApp.apk")
    wait = WebDriverWait(driver, 5)

    # Przejście do ekranu logowania
    wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Login Screen"))).click()

    # Wypełnienie formularza
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "username").send_keys("admin")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "password").send_keys("password")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "loginBtn").click()

    # Sprawdzenie komunikatu błędu
    alert = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/message")))
    assert alert.text == "Invalid login credentials, please try again"

    driver.quit()

if __name__ == "__main__":
    test_invalid_login()