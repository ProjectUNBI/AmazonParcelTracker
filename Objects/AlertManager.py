import threading
import time

from Objects.FliteTTS.FliteTextToSpeeach import FliteTTS


class AlertMananager:
    def __init__(self):
        self.alert_text = ""
        self.is_alert = False
        self.is_out_for_delivery = False
        self.out_for_delivery_cooldown = 0
        self.tts = FliteTTS()

    def start(self):
        thread = threading.Thread(target=self.threadedAlert)
        thread.start()

    def threadedAlert(self):
        while True:
            try:
                if self.alert_text:
                    self.tts.speak(self.alert_text)
                time.sleep(5)
                if self.is_out_for_delivery:
                    print("Out of delivery")
                    self.tts.speak("Amazon will deliver something")
                    self.tts.speak("Today")
                time.sleep(5)
            except:
                print("Error in Flite TTS", flush=True)
                pass

    def current_second_time(self):
        return time.time()

    def Alert(self, alert_text, url):
        print(url)
        self.alert_text = alert_text
        self.is_alert = True

    def AlertOutOfDelivery(self, ):
        time = self.current_second_time()
        if self.out_for_delivery_cooldown > time:
            return
        self.is_out_for_delivery = True

    def DisEngageAllAlert(self):
        self.DisEngageAlert()
        self.DisEngageOutOfDeliveryAlert()

    def DisEngageAlert(self):
        self.is_alert = False
        print("Alert is turning off ringing")


    def DisEngageOutOfDeliveryAlert(self):
        self.out_for_delivery_cooldown = self.current_second_time() + 12 * 60 * 60  # 12hour cooldown
        self.is_out_for_delivery = False
        print("Out off delivery is turning off")

# alertmanager = AlertMananager()
# # alertmanager.AlertOutOfDelivery()
# alertmanager.Alert("Error occur","url")
# time.sleep(40)
# print("Disengaging...")
# # alertmanager.DisEngageOutOfDeliveryAlert()
# alertmanager.DisEngageAllAlert()
# time.sleep(40)
# print("Finish...")
# time.sleep(10)
