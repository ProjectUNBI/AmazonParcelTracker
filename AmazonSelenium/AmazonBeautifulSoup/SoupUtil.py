from bs4 import Tag


def assertSingleSoupTag(souptagparent, can_be_zero=False) -> Tag:
    souptagparent = list(souptagparent)
    souptagparent_size=len(souptagparent)
    if souptagparent_size!= 1:
        if souptagparent_size > 1:
            raise Exception('Multiple elements...')
        if souptagparent_size < 1:
            if not can_be_zero:
                raise Exception('No elements...')
            else:
                return None
    return souptagparent[0]


def assertSingleSoupChildren(children)->Tag:
    children_list=list(children)
    returnable=None
    for child in children_list:
        if type(child)==Tag:
            if returnable != None:
                raise Exception("Too much child in children list")
            returnable=child
    if returnable==None:
        raise Exception("here is no child in children")
    return returnable
