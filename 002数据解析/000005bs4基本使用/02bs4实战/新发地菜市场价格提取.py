"""
网站改了爬不了了
"""

import requests
import re
from bs4 import BeautifulSoup
url = "https://www.dytt.to/"
qingqiu = requests.post(url)
qingqiu.encoding = "gbk"
qing = qingqiu.text
# print(qing)
#初始化BeautifulSoup对象
# page = BeautifulSoup(qing)
page = BeautifulSoup(qing, features="html.parser")

a1 = page.find("div",attrs={"class":"co_content2"})
# print(a)
a1.find_all("a")
for a2 in a1:
    a2.find("href")
    print(a2.text)
    print(a2)






