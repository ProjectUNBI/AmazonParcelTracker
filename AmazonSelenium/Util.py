


def readText(filedir:str):
    file=open(filedir,"r",encoding="UTF-8")
    content=file.read()
    file.close()
    return content


def writeText(filedir:str,content:str):
    file=open(filedir,"w",encoding="UTF-8")
    file.write(content)
    file.close()

