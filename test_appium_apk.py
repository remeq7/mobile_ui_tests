from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException

desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "automationName": "UiAutomator2",
    "app": r"C:\Users\Remek\Desktop\mobile_ui_tests\TheApp.apk",
    "autoGrantPermissions": True
}

driver = webdriver.Remote("http://localhost:4723", desired_caps)

# Kliknij "Echo Box"
echo_box = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                               'new UiSelector().text("Echo Box")')
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
result_text = driver.find_element(AppiumBy.ID, "android:id/message").text
assert test_message in result_text, f"Expected message not found! Got: {result_text}"

print("✅ Test zakończony sukcesem.")

# Poczekaj chwilę i zakończ
time.sleep(2)
driver.quit()
