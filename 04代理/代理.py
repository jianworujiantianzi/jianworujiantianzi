import requests
"""==================================正常访问百度========================================"""
# url = "https://www.baidu.com"
# resp = requests.get(url)
# resp.encoding = "utf-8"
# print(resp.text)

"""======================================代理的一些相关信息============================"""
"""
proxy(谐音;跑费)意思就是代理的意思
代理有两种一般一种是http的代理
使用方法   "http":"http//后面写上代理ip和端口"
    然后下面写上"https":https//写上ip和端口    记得用:隔开案例看下面就行
    这个就是访问http的时候用http就行访问https的时候就直接会调用下面的https
    这两个都写上比较好一点
    但是两个都写的话刚刚测试了一下运行不了可能是老师教的有问题把我只弄了一个html是可以运行的
    还有可能是代理ip的
"""
url = "https://www.baidu.com"
proxy = {
"http":"http://183.247.221.119:30001"
}
"""
加上下面这样的一个操作就可以把代理ip加进去
"""
resp = requests.get(url, proxies=proxy)
resp.encoding = "utf-8"
print(resp.text)



"""
代理的弊端
1.
    慢
2.
    代理IP不好找好找的代理ip不好用   高级的还要收费
"""