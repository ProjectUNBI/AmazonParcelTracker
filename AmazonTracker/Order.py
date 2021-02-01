import traceback
from datetime import datetime

from AmazonTracker.AlertManager import Alert
from AmazonTracker.TrackSoupUtil import track


class Order:
    def __init__(self, order_id: str, order_url: str, where_to_deliver, loaded_time_of_url: int,
                 order_product_name: str = ""):
        self.order_id = order_id
        self.order_name = order_product_name  ### we are not using this
        self.tracking_url = order_url
        self.loaded_time_of_url = loaded_time_of_url
        ######################
        self.loaded_time_of_url_human_readable = self.get_mili_to_date(self.loaded_time_of_url)
        #####################
        self.where_to_deliver = where_to_deliver
        self.is_out_for_deliver = False

        self.track_progress = {}
        self.has_error_loading = True
        self.loaded_time = 0
        self.loaded_time_human_readable = 0

        self.flag_load_counter = 0
        self.MAX_LOAD_COUNTER = 10

    def get_mili_to_date(self, timemilli):
        date = datetime.fromtimestamp(timemilli / 1000.0)
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        return date

    def load_order_progress(self):
        if not self.has_error_loading:
            return
        while True:
            try:
                self.track_progress, self.is_out_for_deliver = track(self.tracking_url)
                now = datetime.now()
                self.loaded_time = now.timestamp() * 1000
                self.loaded_time_human_readable = now.strftime("%Y-%m-%d %H:%M:%S")
                self.has_error_loading = False
            except:
                self.has_error_loading = True
                traceback.print_exc()
                print("Error in tracking order...")
            if not self.has_error_loading:
                break
            else:
                self.flag_load_counter += 1
                if self.flag_load_counter > self.MAX_LOAD_COUNTER:
                    break
        if self.has_error_loading:
            Alert("Error in loading data")
