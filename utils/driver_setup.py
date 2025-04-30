from appium import webdriver

def init_driver(apk_path):
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "app": apk_path,
        "autoGrantPermissions": True
    }
    return webdriver.Remote("http://localhost:4723", desired_caps)
