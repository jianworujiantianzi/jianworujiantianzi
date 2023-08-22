"""
"""

import requests
import re

url = "https://movie.douban.com/top250"
"""进行一个小小的反爬"""
hdaders = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
a = requests.get(url,headers=hdaders)

a1 = a.text
# print(a1)
"""
编写正则表达式
"""
obj = re.compile(r'<div class="item">.*?<span class="title">'
                 r'(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?导演:'
                 r'(?P<daoyan>.*?)&nbsp'
                 r'.*?<br>'
                 r'(?P<nian>.*?)&nbsp'
                 r'.*?<span class="rating_num" property="v:average">'
                 r'(?P<pingfen>.*?)</span>'
                 r'.*?<span>(?P<pingfenrenshu>.*?)</span>',re.S)

ss = obj.finditer(a1)
for aa in ss:
    name = aa.group("name")
    daoyan = aa.group("daoyan")
    """
                            .strip()去掉字符串左右两端的空白
    """
    nian = aa.group("nian").strip()
    pingfen = aa.group("pingfen")
    pingfenrenshu = aa.group("pingfenrenshu")
    print("电影名:",name)
    print("导演",daoyan)
    print("上架时间",nian)
    print("评分",pingfen)
    print(pingfenrenshu)


