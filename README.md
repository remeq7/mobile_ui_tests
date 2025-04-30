# 📱 mobile_ui_tests

Automated UI tests for mobile applications using Appium and Python.

## 🔧 Requirements

- Python 3.10+
- Appium Server
- Android Emulator (e.g., via Android Studio)
- ADB + Android SDK

## ▶️ Running the test

1. Start your emulator
2. Make sure Appium Server is running (`appium`)
3. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```
4. Run the test:
   ```bash
   python -m tests.test_appium_apk
   ```

## 🧪 Contents

- `TheApp.apk` – Another demo app for practice
- `test_appium_apk.py` – Example Python test script

## 📄 License

MIT
