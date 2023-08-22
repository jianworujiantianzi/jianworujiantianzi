import requests
ss = input("请输入你要查找的内容")
"""
gat请求参数直接放在后面就可以了
"""
url = "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd={}".format(ss)

"""
headers"通常指的是HTTP请求或响应中的头部信息。
HTTP协议是一种用于传输Web数据的通信协议。HTTP请求和响应都包含头部信息和主体内容。
"""
#处理了一个小小的反爬
a = {
    #添加一个请求头信息。UA
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

}
"""
这个headers=a是处理一个反爬的一个功能
然后这个a里面放的是一个字典字典的健是 User-Agent:字典的值是User-Agent后面跟的一些东西
这个User(谐音：有色：用户)-Agent(a真他)就是你用户用的什么助手的意思在这里就是指的是
用户用的什么设备发送的网络请求然后字典的后面就写你用的什么设备
其实这些就在谷歌浏览器F12里面的Notwork里面的Headers里面的最后一行就能找到
复制过来或者用别的设备上面都行
"""
resp = requests.get(url,headers=a)
resp.encoding = "utf-8"
print(resp.text)
#注意用下面的这一行的时候要把上面的一些给注释掉
#print(resp.request.headers)#可查看请求头信息   也就是对你的设备的一个查看
#这个headers(谐音:嗨的思)  请求头的意思