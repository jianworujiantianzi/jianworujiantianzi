"""
"""

import requests
import re
"""
csv文件就是数据文件  数据和数据之间用逗号隔开的文件
"""
f = open("top250.csv",mode="w",encoding='utf-8')
url = "https://movie.douban.com/top250?start=25&filter="

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
    f.write(f"{name},{daoyan},{nian},{pingfen},{pingfenrenshu}\n")
f.close()
a.close()
print("豆瓣Top250提取完毕")
