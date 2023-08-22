""""""
"""
需求:
    抓取猪八戒网站里面的saas里面每一家商品对应的价格整体对应的名称和整体的需求
     以及他是那家公司的  以及对应的地区 等等一系列数据     
注意:先某而后动
"""
import requests
from lxml import etree
url = "https://www.zbj.com/search/service/?kw=saas&r=2"
wwww = "https://www.zbj.com/search/service/?kw=saas&r=2&l=0"
resp = requests.get(url)
resp.encoding="utf-8"
# print(resp.text)
#提取数据
et = etree.HTML(resp.text)
divs = et.xpath("//div[@class='search-result-list-service']/div")
for div in divs:
    #此时div就是一条数据了，对应一个商品信息
    div.xpath(".//div[@class='price']")
    a=div.xpath("./div[1]/div[3]/div[1]//span/text()")
    if not a:
        continue
    a = a[0]
    b = div.xpath("./div[1]/div[3]/div[2]//a/text()")
    if not b:
        continue
    b = b[0]
    c = a + b

    print(c)

# [div/div/a/div[3]/div/span]