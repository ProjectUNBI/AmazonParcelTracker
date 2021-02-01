import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup, Tag


def assertSoup(souptagparent, can_be_zero=False) -> Tag:
    souptagparent = list(souptagparent)
    souptagparent_size = len(souptagparent)
    if souptagparent_size != 1:
        if souptagparent_size > 1:
            raise Exception('Multiple elements...')
        if souptagparent_size < 1:
            if not can_be_zero:
                raise Exception('No elements...')
            else:
                return None
    return souptagparent[0]


def track(url: str):
    url = "https://www.amazon.in" + url
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    # ("div", {"class": re.compile(CLASSS_ORDER_CONTAINER_LEFT)}))

    primarysatus = assertSoup(soup.findAll("span", {"id": "primaryStatus"}))
    primarysatus_text = primarysatus.text.strip()
    tracksummary = {}

    flag_outfor_delivery = False

    if "Delivered" in primarysatus_text:
        tracksummary[primarysatus_text] = True
        pass
    else:
        trackcontainer = assertSoup(soup.findAll("div", {"id": "progressTracker-container"}))
        track_children = list(trackcontainer.children)

        flag_outfor_delivery_counter = 0
        for track in track_children:
            if type(track) != Tag:
                continue
            point_order = track["data-start"]
            is_reach = track["data-reached"]
            if is_reach == "reached":
                tracksummary[point_order] = True
                flag_outfor_delivery_counter += 1
            elif is_reach == "notReached":
                tracksummary[point_order] = False
            else:
                raise Exception("Value error in order reach check")
        if flag_outfor_delivery_counter > 2:
            flag_outfor_delivery = True
        # print(json.dumps(tracksummary))

    return tracksummary, flag_outfor_delivery
