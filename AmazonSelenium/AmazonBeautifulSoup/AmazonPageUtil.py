import time

from selenium.webdriver.firefox.webdriver import WebDriver

from AmazonSelenium.Constants import get_order_by_page, WAIT


def load_amazon_page(driver:WebDriver,pagenume: int):

    driver.get(get_order_by_page(pagenume))
    scroll_down(driver)
    WAIT(5)# wait for sometime
    return driver.page_source

def scroll_down(driver: WebDriver):
    scrollheight = driver.execute_script("return document.body.scrollHeight")
    if type(scrollheight) == str:
        scrollheight = int(scrollheight)
    ## lets finish the page scroll by 10 count
    scroll_amount = scrollheight / 10  ### not we might have some remainder
    for num in range(11):
        scrollable = scroll_amount * (num + 1)
        driver.execute_script(f"window.scrollTo(0, {scrollable});")
        time.sleep(0.3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
