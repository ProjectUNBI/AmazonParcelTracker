import threading
import traceback

import requests


class FliteTTS:
    def __init__(self):
        self.threadLock = threading.Lock()
        self.audiodirectory="/home/pi/Desktop/voices/voicearchives/"

    def speakfromflite(self,text: str):
        #curl -X POST -d "Morning" http://192.168.29.251:6767/speak --header "Content-Type:text/xml"
        url = 'http://192.168.29.251:6767/speak'
        headers = {
            "Content-Type": "text/xml",
        }
        try:
            r = requests.post(url, data=text, headers=headers)
            print(r.content)
        except:
            traceback.print_exc()
            return False


    def speak(self, texttospeak, printable=True):
        with self.threadLock:
            if printable:
                print(texttospeak)
            self.speakfromflite(texttospeak)




