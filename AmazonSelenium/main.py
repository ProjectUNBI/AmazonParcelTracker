import jsonpickle

from AmazonSelenium.SeleniumAmazon.AmazonSelenium import AmazonSelenium
from AmazonSelenium.Util import writeText
from MyConfig.Config import AMAZON_ORDERS

amazonselenium=AmazonSelenium()
amazonselenium.loadAmazonOrders()
jsontext=writeText(AMAZON_ORDERS, jsonpickle.encode(amazonselenium, indent=4))
