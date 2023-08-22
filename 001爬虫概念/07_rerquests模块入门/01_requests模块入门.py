"""

"""
"""
优势 比urllib还要简单  并且处理各种请求都比较方便
"""
import requests
#爬取百度的源代码
url = "http://www.baidu.com"
"""先使用get请求 然后会给你一个响应为了标准化一点就用resp来返回"""
resp = requests.get(url)
"""
打印的是Response 对象和一个状态200
"""
#print(resp)
resp.encoding = "utf-8"
"""
如果想要拿到响应体 因为响应体里面放的才是页面源代码
只需要在后面加一个text(谐音:泰克斯他) 拿到相应里面的文本信息
"""
print(resp.text)#拿到页面源代码



