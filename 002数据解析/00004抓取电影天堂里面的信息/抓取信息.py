import requests
import re

url = "https://www.dytt.to/html/gndy/dyzz/20221012/63053.html"
a=requests.get(url)
a.encoding="gbk"
a1 = a.text

# print(a1)
obj = re.compile(r'<div id="Zoom">(?P<lianjie>.*?)译　　名',re.S)
zua = obj.search(a1)
lianjie = zua.group("lianjie")
print(lianjie)