import requests
import re

url = "https://movie.douban.com/top250"
"""进行一个小小的反爬"""
hdaders = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

"""请求一个网址返回一个响应a"""
a = requests.get(url,headers=hdaders)
print(a.text)

