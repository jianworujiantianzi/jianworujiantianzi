""""""
"""
需求拿到最新影片推荐里面的电影
分布操作 
    第一步:先拿到最新影片推荐的那一整个的东西
        先编写正则
    第二部:拿到之后在进行接着查找
"""

import requests
import re

url = "https://www.dytt.to/"
qing = requests.post(url)
qing.encoding = "gbk"

a = qing.text

obj = re.compile(r'最新影片推荐</p></div>(?P<quanbu>.*?)</div>', re.S)

a1 = obj.search(a)


quanbu = a1.group("quanbu")
#print(quanbu)



# obj2 = re.compile(r"<a href='(?P<fen>.*?)'>2022",re.S)
# a2 = obj2.finditer(quanbu)
# for f1 in a2:
#
#
#
#     fen = f1.group("fen")
#     print(fen)

obj3 = re.compile(r"<a href='(?P<fenzhi1>.*?).html'>",re.S)
a3 = obj3.finditer(quanbu)
for f2 in a3:
    fenzhi1 = f2.group("fenzhi1")
    nei = url.strip("/")+fenzhi1+".html"
    # print(nei)
    # print("https://www.dytt.to/"+fenzhi1+".html")
    # zsici = requests.get(nei)
    # zsici1 = zsici.text
    # zsici1.encode("utf-8")
    # print(zsici1)
    # break
    """"""
    zua1 = requests.get(nei)
    zua1.encoding = "gbk"
    zua2 = zua1.text
    # zuaobj = re.compile(r'<div id="Zoom">(?P<lianjie>.*?)译　　名', re.S)
    zuaobj = re.compile(r'<a target="_blank" href=(?P<lianjie>.*?)<strong><font ', re.S)
    zuaxin = zuaobj.finditer(zua2)
    for xinxi in zuaxin:
        lianjie = xinxi.group("lianjie")
        zuihou = lianjie + ".jpg"
        print(zuihou)
