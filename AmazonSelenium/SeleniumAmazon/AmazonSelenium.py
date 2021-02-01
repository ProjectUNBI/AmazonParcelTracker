import json
import time
import traceback

import jsonpickle

from AmazonSelenium.AmazonBeautifulSoup.AmazonPageUtil import load_amazon_page
from AmazonSelenium.AmazonBeautifulSoup.AmazonSoup import AmazonSoup
from AmazonSelenium.SeleniumAmazon.SeleniumDriverBuilder import getChromiumDriver
from AmazonSelenium.Util import writeText
from MyConfig.Config import AMAZON_LOADING_PAGE_LIMIT


class AmazonSelenium():
    def __int__(self):
        self.amazon_order: list = []
        self.has_no_error = False
        self.loadedtime = 0

    def loadAmazonOrders(self):
        driver = getChromiumDriver()
        try:
            first_page = load_amazon_page(driver, 1)
            amazon_soup = AmazonSoup(first_page)
            for page in amazon_soup.pages:
                if page == 1:  # skip as we already rendered this page
                    continue
                if AMAZON_LOADING_PAGE_LIMIT !=0 and page > AMAZON_LOADING_PAGE_LIMIT:
                    print("Reached page limits....")
                    break
                nth_page: str = load_amazon_page(driver, page)
                amazon_soup.render(nth_page)
            self.amazon_order = json.loads(jsonpickle.encode(amazon_soup.orders))
            self.has_no_error=True
        except Exception as e:
            traceback.print_exc()
            print(e)
            self.amazon_order=[]
            self.has_no_error=False
        time.sleep(2)
        self.loadedtime = int(round(time.time() * 1000))
        driver.quit()
