# AmazonParcelTracker
AmazonParcelTracker

# Some points:

* I would like to know an alert when it my parcel is out for delivery
* It run on Raspberry pi.. but will work in PC
* Tested for "amazon.in" [i cannot confirm it work with amazon.com]
* I use Chromium browser as i am using in raspberry pi
# Steps:

1) Install Selemium---> Steps : https://raspberrypi.stackexchange.com/a/104886
2) Edit "/AmazonSelenium/SeleniumAmazon/SeleniumDriverBuilder.py" and comment out 'chromeOptions.add_argument("--headless")' so that chrome/chromium will run in desktop,not in background.[amazon website not work in firefox-esr of raspberry pi]
3) Test if selenium work by running "run_test_selenium" it will run "./tests/testSelenium.py". if it shows opening chrome,then it is okey.
4) Sign in to the amazon in Chromium browser
5) edit "./MyConfig/Config.py" and make sure your Proofile and Profile directory is set properly
6) AMAZON_LOADING_PAGE_LIMIT in ./MyConfig/Config.py is the number of page to check the order. Put it Zero if you want to check all page
7) AMAZON_ORDERS in in ./MyConfig/Config.py is the location where the extracted order detail is to be put.... 

# Final steps:
Lets undestand how it work......
* Your pc will run "run_order_list_maker" every day using crontab.So run the "run_order_list_maker" using crontab for everyday
* "run_order_list_maker" will put the extracted order detail in "AMAZON_ORDERS" [mention in ./MyConfig/Config.py]
* "runtracker" should be run. it will check the order trackings... and ist should be always run..
* "runtracker" also serve a Flask server, so that i can check order also from my other pc, as i connected at same network
* If you want the above feature, run "run_cleint_interface", modify the ip adress of for your one
* "./Objects/AlertManager.py" modify this to make alert of your own choice..





