"""
"""

"""
第一步:先定好爬取的目标
    目标，电影名称 导演 还有多少人评价
第二部查看:
    是否数据再页面源代码里面
        如果是再:页面源代码里面只用拿到页面源代码然后用正则一个个提取就完事了
        如果不再:那就要用特使特殊的方法了
第三步:编写正则
第四步:保存数据
"""
import requests
import re

url = "https://movie.douban.com/top250"
"""进行一个小小的反爬"""
hdaders = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

"""请求一个网址返回一个响应a"""
a = requests.get(url,headers=hdaders)
"""
aa = a.encoding = "utf-8"   如果有乱码问题就用这个
"""
"""从响应里面拿到源代码赋值给一个变量"""
a1 = a.text
# print(a1)


"""
编写正则表达式
re.S        应为.是一个坑所以要用这个来把这个坑填上
    让正则里面的.可以匹配换行符
"""
"""预加载"""
obj = re.compile(' <div class="item">(?P<qq>.*?)<span '
                 'class="title">(?P<name>.*?)</span>.*?<p class="">'
                 '.*?导演:(?P<dao>.*?)&nbsp;<br>(?P<nian>.*?)&nbsp'
                 '.*?<span class="rating_num" property="v:average">'
                 '(?P<pingfen>.*?)</span>.*?'
                 '<span>(?P<duoshao>.*?)</span>',re.S)

ss = obj.finditer(a1)
for aa in ss:
    # aa1 = aa.group("name")
    # print(aa1)
    # aa2 = aa.group("qq")
    # print(aa2)
    # aa3 = aa.group("name2")
    # print(aa3)
    aa11 = aa.group("dao")
    print(aa11)
    aa111 = aa.group("nian")
    print(aa111)




















