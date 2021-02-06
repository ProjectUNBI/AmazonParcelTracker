#!/usr/bin/python3
import time

import jsonpickle
import requests
from texttable import Texttable


def updatedataToUser(data: list):
    data.reverse()
    #######Print tabulated##########
    if len(data) > 1:
        print("################ URL load time----> ", data[0].loaded_time_of_url_human_readable, " ################")

    tabulatedarray = []
    tabulatedarray.append([
        "Progress load time",
        "Order name",
        "Progress" + " & " +
        "Load status",
        "Address",
        "status"
    ])
    for order in data:
        ######pruductname######
        names = ""
        length = 15
        flagcounter = 0
        for prductname in order.order_name:
            flagcounter += 1
            trunicated_name = (prductname[:length] + '......') if len(prductname) > length else prductname
            names = f"{names} {flagcounter}){trunicated_name}   \n"
        #####productptractprogress######
        progressstr = ""
        for attribute, value in order.track_progress.items():
            if value:
                progressstr = f"{progressstr}{attribute} [X]---->"
            else:
                progressstr = f"{progressstr}{attribute} [ ]---->"
        order_last_location = "\n".join(order.last_tract_location)
        if len(progressstr) > 4:
            progressstr = progressstr[:-5]

        orderDetail = [
            order.loaded_time_human_readable,
            names,
            progressstr + "\n" +
            order_last_location,
            order.where_to_deliver,
            str(not order.has_error_loading)
        ]
        tabulatedarray.append(orderDetail)
    t = Texttable()
    t.add_rows(tabulatedarray)
    t.set_cols_width([19, 27, 90,19, 6])
    t.set_cols_align(["c", "c", "c","c", "c"])
    t.set_cols_valign(["m", "m", "m","m", "m"])
    print(t.draw())

counter=0
print("\033c", end="")
while True:
    req = requests.get('http://192.168.29.246:63666/amazon')
    orderarray = jsonpickle.decode(req.text)
    updatedataToUser(orderarray)
    counter+=1
    print(counter)
    time.sleep(120)
    print("\033c", end="")


