from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from MyConfig.Config import CHROME_PROFILE, CHROME_DIR, FIREFOX_PROFILE


def getChromiumDriver() -> WebDriver:
    chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # chromeOptions.add_argument("--no-sandbox")
    # chromeOptions.add_argument("--disable-setuid-sandbox")
    # chromeOptions.add_argument("--remote-debugging-port=9222")  # this
    # chromeOptions.add_argument("--disable-dev-shm-using")
    # chromeOptions.add_argument("--disable-extensions")
    # chromeOptions.add_argument("--disable-gpu")
    # chromeOptions.add_argument("start-maximized")
    # chromeOptions.add_argument("disable-infobars")
    # chromeOptions.add_argument('--no-sandbox')
    # chromeOptions.add_argument('--disable-dev-shm-usage')
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument(f"--user-data-dir={CHROME_DIR}")
    chromeOptions.add_argument(f"--profile-directory={CHROME_PROFILE}")
    driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chromeOptions)
    return driver

def getFireFoxDriver()->WebDriver:
    return webdriver.Firefox(firefox_profile=FIREFOX_PROFILE)



