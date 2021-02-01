import json
import re

from bs4 import Tag, BeautifulSoup, NavigableString

from AmazonSelenium.Constants import CLASSS_ORDER_CONTAINER_LEFT, ORDER_INFO, SHIPMENT, CLASS_VALUE_ORDER_ID, \
    CLASSS_ORDER_CONTAINER_RIGHT, DATA_POP_OVER_ADDR, CLASS_TRACK_BUTTON, CLASS_NONTRACKABLE, CLASS_TRACKABLE, \
    SHIPMENT_PRODUCT_NAME
from AmazonSelenium.AmazonBeautifulSoup.SoupUtil import assertSingleSoupTag, assertSingleSoupChildren


class AmazonOrder:
    def __init__(self, order_tag: Tag):
        self.where_to_deliver = ""
        # self.price_of_order = 0
        self.order_id = ""
        self.order_track_url_list = []
        self.is_trackable = False
        ##########Parse the order tag##############
        self.parse(order_tag)

    def parse(self, order_tag: Tag):

        order_tag_children = order_tag.children
        for order_tag_child in order_tag_children:
            if type(order_tag_child) != Tag:
                continue
            order_tag_child: Tag = order_tag_child
            if not order_tag_child.has_attr("class"):
                continue

            class_attr = order_tag_child["class"]
            if ORDER_INFO in class_attr:
                left_div = assertSingleSoupTag(
                    order_tag_child.findAll("div", {"class": re.compile(CLASSS_ORDER_CONTAINER_LEFT)}))
                right_div = assertSingleSoupTag(
                    order_tag_child.findAll("div", {"class": re.compile(CLASSS_ORDER_CONTAINER_RIGHT)}))
                self.order_id = self.parse_order_id(right_div)
                ##################
                left_div_child = assertSingleSoupChildren(left_div.children)
                address_tag = assertSingleSoupTag(left_div_child.findAll("span", {DATA_POP_OVER_ADDR: re.compile(
                    "..")}),
                                                  True)
                if address_tag is not None:
                    address: str = address_tag[DATA_POP_OVER_ADDR]
                    self.where_to_deliver = BeautifulSoup(json.loads(address)['inlineContent'],
                                                          'html.parser').text.strip()
            if SHIPMENT in class_attr:
                ########Extracting product name########
                shipment_product_detail_list = list(order_tag_child.findAll("a", {"class": SHIPMENT_PRODUCT_NAME}))
                productname = []
                for pdct in shipment_product_detail_list:
                    content_list = pdct.contents
                    flag_isproductname = True
                    for content in content_list:
                        if type(content) == NavigableString:
                            pass
                        else:
                            flag_isproductname = False
                            break
                    if flag_isproductname:
                        productname.append(pdct.text.strip())
                ########################################
                track_button = assertSingleSoupTag(
                    order_tag_child.findAll("span", {"class": re.compile(CLASS_TRACK_BUTTON)}), True)
                if track_button==None:
                    continue
                button_class: list = track_button["class"]
                if CLASS_NONTRACKABLE in button_class:
                    is_in_transit = False
                elif CLASS_TRACKABLE in button_class:
                    is_in_transit = True
                else:
                    raise Exception("Ccannot dettermine button type")
                if track_button is not None:
                    self.is_trackable = True
                    track_url = assertSingleSoupTag(track_button.findAll("a"))
                    self.order_track_url_list.append(
                        {
                            "in_transit": is_in_transit,
                            "url": track_url['href'],
                            "productname":productname
                        }
                    )

        pass

    def parse_order_id(self, right_div):
        value = assertSingleSoupTag(right_div.findAll("span", {"class": re.compile(CLASS_VALUE_ORDER_ID)}))
        return value.text.replace("\n", "")

    def default(self, o):
        return o.__dict__
