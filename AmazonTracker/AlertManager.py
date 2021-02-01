import time

from AmazonTracker.FliteTTS.FliteTextToSpeeach import FliteTTS


def Alert(alert_text,url):
    print(url)
    tts=FliteTTS()
    while True:
        tts.speak("There is some error")
        time.sleep(10)



def AlertOutOfDelivery():
    print("Out of delivery")
    tts=FliteTTS()
    while True:
        tts.speak("Amazon will deliver something")
        tts.speak("Today")
        time.sleep(10)


# Alert("","dasdsad")
# AlertOutOfDelivery()
