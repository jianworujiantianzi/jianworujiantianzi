"""

"""
import requests


url = "https://fanyi.baidu.com/sug"

a= {
    "kw":input("请输入一个单词")
}
"""
因为这个请求是post请求所以后面是.post
然后post请求后面跟的参数是data所以后面要跟一个data=a这个a可以是任意数
然后这个a里面放的参数是
Form Data下面的一个字典 这里面的健是固定的值随便输入
详细的位置请看图片"Form Data位置.png"
"""
resp = requests.post(url,data=a)  #注意这个data是post请求里面的专属参数
"""
这样子返回的是一个json数据
.text拿到的是一个字符串正常人一般看不懂想要看懂就需要解码，解码方式如下下面的那一行
"""
#print(resp.text)   #拿到的是文本字符串
"""
使用.json()即可进行解码
这样子的话拿到的是一个字典  并且可以一层层的拿数据 比如说你只想要某一个列表里面的数据的话
你可以再后面加一个列表["想要的数据"]如果不加的话那只能拿到所有的数据了
下面展示一下如何拿到筛选出来的数据
"""
print(resp.json())  #这样子就只能拿到data这个列表里面的数据了

"""
post请求参数是放到data里面
"""