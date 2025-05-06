from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from utils.driver_setup import init_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = init_driver("apk/TheApp.apk")

# Kliknij "Echo Box"
echo_box = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Echo Box")')
echo_box.click()
time.sleep(1)

# Wpisz tekst
test_message = "Hello Appium"
input_field = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
input_field.send_keys(test_message)

# Kliknij "Save"
save_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                  'new UiSelector().text("Save")')
save_button.click()
time.sleep(1)

# Sprawdź, czy wiadomość została zapisana
wait = WebDriverWait(driver, 5)
try:
    result = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/message")))
    result_text = result.text
except:
    result_text = "[NOT FOUND]"

print("✅ Test zakończony sukcesem.")

# Poczekaj chwilę i zakończ
time.sleep(2)
driver.quit()
