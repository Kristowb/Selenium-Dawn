import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time

# === CONFIG ===
DAWN_EXTENSION_PATH = "/absolute/path/to/dawn_extension.crx"
DAWN_PLATFORM_URL = "https://dawn-platform.com"
PROXY = "http://your.proxy.address:port"  # format: http://ip:port

# === Chrome Options ===
options = Options()
options.add_extension(DAWN_EXTENSION_PATH)
options.add_argument(f'--proxy-server={PROXY}')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# === Launch Chrome ===
driver = uc.Chrome(options=options)

print("Waiting for extension to initialize...")
time.sleep(5)

print(f"Opening {DAWN_PLATFORM_URL}")
driver.get(DAWN_PLATFORM_URL)

time.sleep(10)

input("Press Enter to close browser...")
driver.quit()
