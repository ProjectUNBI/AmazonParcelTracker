import json
import time
from threading import Thread

import jsonpickle

from Objects.Order import Order
from AmazonTracker.UserInteraaction import updatedataToUser
from MyConfig.Config import AMAZON_ORDERS

READ_FILE_DELAY = 5 * 60 * 60
LOAD_TRACK_DELAY = 1 * 60 * 60
RETRY_TRACK_DELAY = 10 * 60
DELAY_PER_ORDER_CHECK = 30
TRACK_PORT = 63666


def read_amazon_orders(loop):
    global ORDER_DETAIL, READ_FILE_DELAY
    while True:
        file = open(AMAZON_ORDERS, "r")
        print("Reading data")
        text = file.read()
        file.close()
        try:
            ORDER_DETAIL = json.loads(text)
        except:
            print("Error in parsing the file to jso")
        if not loop:
            return
        time.sleep(READ_FILE_DELAY)


def make_track_order_url(order, loadtime) -> list:
    if not order["is_trackable"]:
        return []
    orderid = order["order_id"]
    where_to_deliver = order["where_to_deliver"]
    url_list = order["order_track_url_list"]
    real_trackeble_url = []
    for url in url_list:
        # if url["in_transit"]:
        real_trackeble_url.append(
            Order(orderid, url["url"], where_to_deliver, loadtime, url["productname"])
        )
    if len(real_trackeble_url) == 0:
        return []
    return real_trackeble_url


def handle_order_tracker():
    global ORDER_DETAIL, LOAD_TRACK_DELAY, DUMP_DATA
    while True:
        has_no_error = ORDER_DETAIL["has_no_error"]
        if not has_no_error:
            time.sleep(LOAD_TRACK_DELAY)
            continue
        orderlist = ORDER_DETAIL["amazon_order"]
        loadtime = ORDER_DETAIL["loadedtime"]

        ###############
        # Todo check time is not from yesteday time differenece ELSE allert a lot
        ###############

        trackable_order = []
        for order in orderlist:
            trackable_order.extend(make_track_order_url(order, loadtime))
        for order in trackable_order:
            order: Order = order
            order.load_order_progress()
            time.sleep(DELAY_PER_ORDER_CHECK)  # not to block by amazon srever
        DUMP_DATA = jsonpickle.encode(trackable_order)
        updatedataToUser(trackable_order)  ########We update here
        time.sleep(LOAD_TRACK_DELAY)


################Flask Server############
from flask import Flask

myflask = Flask(__name__)


@myflask.route('/amazon')
def getdump():
    global DUMP_DATA
    return DUMP_DATA


def serve():
    global TRACK_PORT
    myflask.run(host="0.0.0.0", port=TRACK_PORT)


#############################################


ORDER_DETAIL = {}
read_amazon_orders(False)
DUMP_DATA = "[]"
if __name__ == "__main__":
    thread1 = Thread(target=read_amazon_orders, args=(True,))
    thread1.start()
    thread2 = Thread(target=handle_order_tracker)
    thread2.start()
    thread3 = Thread(target=serve)
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    print("thread finished...exiting")
