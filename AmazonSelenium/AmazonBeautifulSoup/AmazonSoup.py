from bs4 import BeautifulSoup, Tag

from AmazonSelenium.AmazonBeautifulSoup.AmazonOrder import AmazonOrder
from AmazonSelenium.Constants import ATTR_SINGLE_ORDER, ATTR_ORDER_PAGE, CLASS_A_PAGINTION, ID_ORDERCONTAINER
from AmazonSelenium.AmazonBeautifulSoup.SoupUtil import assertSingleSoupTag


class AmazonSoup:
    def __init__(self, htmlcontent: str):
        ###We are rendering the first page#### from this we will able to know how much page is there and order detail of first page
        first_page = self.parse_page(htmlcontent)
        self.pages: list = first_page["pagecount"]
        self.orders: list = first_page["orders"]

    def parse_page(self, htmlcontent: str) -> dict:
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        html_order_container = assertSingleSoupTag(soup.findAll("div", {"id": ID_ORDERCONTAINER}))
        html_order_container_children = list(html_order_container.children)
        returnable = {"orders": [], "pagecount": []}
        for html_order_container_child in html_order_container_children:
            if type(html_order_container_child) != Tag:
                continue
            html_order_container_child: Tag = html_order_container_child
            if not html_order_container_child.has_attr("class"):
                continue

            ###now check the attributes####
            class_attr_value_str = " ".join(html_order_container_child["class"])
            if class_attr_value_str == ATTR_SINGLE_ORDER:
                returnable["orders"].append(AmazonOrder(html_order_container_child))
            if class_attr_value_str == ATTR_ORDER_PAGE:
                returnable["pagecount"].extend(self.get_page_count(html_order_container_child))
        if len(returnable["pagecount"]) == 0:
            raise Exception("Order page is null can have some error in parsing")
        return returnable

    def get_page_count(self, pagecount_tag: Tag):
        pagecount_tag_list = list(
            assertSingleSoupTag(pagecount_tag.findAll("ul", {"class": CLASS_A_PAGINTION})).children)
        flag_pagecounter = 0
        pages = []
        for pagecount_tag_child in pagecount_tag_list:
            if type(pagecount_tag_child) != Tag:
                continue
            if not pagecount_tag_child.has_attr("class"):
                continue
            class_pagecount_tag_child = " ".join(pagecount_tag_child["class"])
            if class_pagecount_tag_child in ["a-normal", "a-selected"]:
                flag_pagecounter += 1
                pages.append(flag_pagecounter)
        return pages

    def render(self, nth_page_content: str):
        nth_page = self.parse_page(nth_page_content)
        self.orders.extend(nth_page["orders"])

    def default(self, o):
        return o.__dict__
