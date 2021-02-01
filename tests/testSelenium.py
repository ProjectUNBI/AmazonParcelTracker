from AmazonSelenium.Constants import WAIT
from AmazonSelenium.SeleniumAmazon.SeleniumDriverBuilder import getChromiumDriver

driver = getChromiumDriver()
driver.get("https://api.ipify.org")
print("It is working!!! and loaded:-> ", driver.page_source)
WAIT(30)  # wait for sometime
driver.quit()
