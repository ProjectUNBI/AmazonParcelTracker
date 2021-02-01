from AmazonTracker.AlertManager import AlertOutOfDelivery
from AmazonTracker.Order import Order
from prettytable import PrettyTable


def updatedataToUser(data:list):
    flag_outfordelivery=False
    #######Print tabulated##########
    t = PrettyTable([
                 "Progress load time",
                 "Order Id",
                 "Order name",
                 "Url load time",
                 "Progress",
                 "Load status"
             ])
    for order in data:
        if order.is_out_for_deliver:
            flag_outfordelivery=True
        """
        self.order_id = order_id
        self.order_name = order_product_name  ### we are not using this
        self.tracking_url = order_url
        self.loaded_time_of_url = loaded_time_of_url
        ######################
        self.loaded_time_of_url_human_readable = self.get_mili_to_date(self.loaded_time_of_url)
        #####################
        self.where_to_deliver = where_to_deliver

        self.track_progress = []
        self.has_error_loading = True
        self.loaded_time = 0
        self.loaded_time_human_readable = 0
        """
        order: Order = order

        ######pruductname######
        names=""
        length = 30
        flagcounter=0
        for prductname in order.order_name:
            flagcounter+=1
            trunicated_name = (prductname[:length] + '......') if len(prductname) > length else prductname
            names=f"{names} {flagcounter}){trunicated_name}   \n"
        #####productptractprogress######
        progressstr=""
        for attribute, value in order.track_progress.items():
            if value:
                progressstr=f"{progressstr}{attribute} [X]---->"
            else:
                progressstr=f"{progressstr}{attribute} [ ]---->"
        if len(progressstr)>4:
            progressstr=progressstr[:-5]
        orderDetail=[
            order.loaded_time_human_readable,
            order.order_id,
            names,
            order.loaded_time_of_url_human_readable,
            progressstr,
            not order.has_error_loading

        ]
        t.add_row(orderDetail)
    print(t)
    if flag_outfordelivery:
        AlertOutOfDelivery()





