# AmazonParcelTracker
AmazonParcelTracker

# How it work:
1) "run_order_list_maker" will load all your amazon order[tested for amazon.in but not for amazon.com] and export a json data which contain a lot of information about your orders. This script actually open your browser[can be open in headless,in background] using Selenium WebDriver. This script ideally should be run once a day using crontab.
2) "runtracker" will load the extracted json data and will tract down all the trackable order and will alert if something interesting is there
3) "runtracker" also run a Flask server so that you can check it from other pc in same network.run "run_cleint_interface" for this..

# Some points:

* I would like to know an alert when my parcel is out for delivery
* It run on Raspberry pi.. but will work in PC
* Tested for "amazon.in" [i cannot confirm it work with amazon.com]
* I use Chromium browser as i am using in raspberry pi
# Steps:

1) Install Selemium---> Steps : https://raspberrypi.stackexchange.com/a/104886
2) Edit "/AmazonSelenium/SeleniumAmazon/SeleniumDriverBuilder.py" and comment out 'chromeOptions.add_argument("--headless")' so that chrome/chromium will run in desktop,not in background.[amazon website not work in firefox-esr of raspberry pi]
3) Test if selenium work by running "run_test_selenium" it will run "./tests/testSelenium.py". if it shows opening chrome,then it is okey.
4) Sign in to the amazon in Chromium browser
5) edit "./MyConfig/Config.py" and make sure your Profile and Profile directory is set properly
6) AMAZON_LOADING_PAGE_LIMIT in ./MyConfig/Config.py is the number of page to check the order. Put as Zero if you want to check all page
7) AMAZON_ORDERS in in ./MyConfig/Config.py is the location where the extracted order detail is to be put.... 

# Final steps:
Lets undestand how it work......
* Your pc will run "run_order_list_maker" every day using crontab.So run the "run_order_list_maker" using crontab for everyday.eg `0 */4 * * * /home/pi/Desktop/AmazonParcelTracker/run_order_list_maker`

* "run_order_list_maker" will put the extracted order detail in "AMAZON_ORDERS" [mention in ./MyConfig/Config.py]
* "runtracker" should be run. it will check the order trackings... and ist should be always run..
* "runtracker" also serve a Flask server, so that i can check order also from my other pc, as i connected at same network
* If you want the above feature, run "run_cleint_interface", modify the ip adress of for your one
* "./Objects/AlertManager.py" modify this to make alert of your own choice..





