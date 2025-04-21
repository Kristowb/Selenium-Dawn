import os
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === CONFIG ===
BASE_DIR = r"D:\Code\AI\Automation\SeleniumDawn"
DAWN_EXTENSION_PATH = os.path.join(BASE_DIR, "1.1.5_0.crx")
DAWN_PLATFORM_URL = "https://www.dawninternet.com/"

# Check if the extension file exists
if not os.path.exists(DAWN_EXTENSION_PATH):
    raise FileNotFoundError(f"Extension file not found at {DAWN_EXTENSION_PATH}")

# === Chrome Options ===
options = Options()
options.add_extension(DAWN_EXTENSION_PATH)
options.add_argument('--disable-blink-features=AutomationControlled')

try:
    # === Launch Fresh Chrome Instance with Extension ===
    driver = uc.Chrome(options=options)

    print("Waiting for extension to initialize...")
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    print(f"Opening {DAWN_PLATFORM_URL}")
    driver.get(DAWN_PLATFORM_URL)

    # Wait for a specific element to load (example: body tag)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    print("Page loaded successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    input("Press Enter to close browser...")
    driver.quit()