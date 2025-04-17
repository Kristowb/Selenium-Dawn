import os
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time

# === CONFIG ===
DAWN_EXTENSION_PATH = r"D:\Code\AI\Automation\SeleniumDawn\1.1.5_0.crx"
DAWN_PLATFORM_URL = "https://www.dawninternet.com/"

# Check if the extension file exists
if not os.path.exists(DAWN_EXTENSION_PATH):
    raise FileNotFoundError(f"Extension file not found at {DAWN_EXTENSION_PATH}")

# === Chrome Options ===
options = Options()
options.add_extension(DAWN_EXTENSION_PATH)
options.add_argument('--disable-blink-features=AutomationControlled')

# === Launch Fresh Chrome Instance with Extension ===
driver = uc.Chrome(options=options)

print("Waiting for extension to initialize...")
time.sleep(5)  # give the extension time to activate

print(f"Opening {DAWN_PLATFORM_URL}")
driver.get(DAWN_PLATFORM_URL)

input("Press Enter to close browser...")
driver.quit()
