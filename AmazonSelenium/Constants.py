import time

ORDER_FIRST_PAGE:str="https://www.amazon.in/gp/css/order-history?ref_=nav_orders_first"
ORDER_SECOND_PAGE:str="https://www.amazon.in/gp/your-account/order-history/ref=ppx_yo_dt_b_pagination_1_2?ie=UTF8&orderFilter=months-3&search=&startIndex=10"
ORDER_THIRD_PAGE:str="https://www.amazon.in/gp/your-account/order-history/ref=ppx_yo_dt_b_pagination_1_3?ie=UTF8&orderFilter=months-3&search=&startIndex=20"

def get_order_by_page(pagenum:int) -> str:
    if pagenum==1:
        return  ORDER_FIRST_PAGE
    return f"https://www.amazon.in/gp/your-account/order-history/ref=ppx_yo_dt_b_pagination_1_{pagenum}?ie=UTF8&orderFilter=months-3&search=&startIndex={pagenum-1}0"

def WAIT(sec:int):
    time.sleep(sec)


ATTR_SINGLE_ORDER='a-box-group a-spacing-base order'
ATTR_ORDER_PAGE='a-row'

######classs########

CLASS_A_PAGINTION="a-pagination"
CLASSS_ORDER_CONTAINER_LEFT="a-fixed-right-grid-col.*?a-col-left"
CLASSS_ORDER_CONTAINER_RIGHT="a-fixed-right-grid-col.*?a-col-right"
CLASS_VALUE_ORDER_ID="[^a-z]value"
CLASS_NONTRACKABLE="a-button-base"
CLASS_TRACKABLE="a-button-primary"
CLASS_TRACK_BUTTON="track-package-button"

DATA_POP_OVER_ADDR="data-a-popover"
###########ID########
ID_ORDERCONTAINER="ordersContainer"


#######################

ORDER_INFO="order-info"
SHIPMENT="shipment"
SHIPMENT_PRODUCT_NAME="a-link-normal"

# print(get_order_by_page(1))
# print(get_order_by_page(2))
# print(get_order_by_page(3))
# print(get_order_by_page(4))
# print(get_order_by_page(5))