"""
第一个引号里面的注释颜色有点浅先随便引一个
"""

"""
第一部，导入模块
form urllib(谐音:u爱哦利不).request(瑞快死他) import urlopen(谐音:ul欧喷)
翻译上面的意思  url( 网址)lib（跟网址相关的一个库）.request(这个库里面的一个
模块，翻译过来叫请求的意思)连起来就是再url里面有一个请求的模块然后这个请求的模块里
面有一个函数叫urlopen  url是网址open是打开   和起来就是大开一个网址
"""
from urllib.request import urlopen
"""      
第二部
    要把爬取的那个网址给他  
注意
    如果写的是http经过后面的操作直接跳转到源代码
    如果写的是https则跳转到http
"""
url = "http://www.baidu.com"

"""
第三步
    通过urlopen打开这个网址并用一个值来接收
"""
resp = urlopen(url)
"""
第四步
    把上面网址的数据的东西给打印出来
    直接打印的话看不到里面的东西 那该怎么办呢
    在后面加一个.read()[谐音:瑞的]就可以把里面的内容全部给读出来了
    
"""
# print(resp.read())

"""
第四步下
    因为上一行获取到的数据都数据是b.开头的 这证明你拿到的数据是一个字节是字节的话
    就需要我们手动的把这个字节换成字符串这时候就需要一个解码.decode()[谐音：第扣的]
    然后decode()括号里面放两个引号或者双引号代表字符串的意思
引号里面放什么东西呢？
    1.先运行上面的那一行代码，然后再返回栏里面按ctrl+l搜索charset(谐音：铲赛特)
    2.然后搜索到了以后charset=后面有一个东西然后就把后面的那个东西放到引号里面
        一般后面跟的都是utf-8或者是jbk
"""
print(resp.read().decode("utf-8"))
"""
通过上面的那一行代码返回过来的是页面源代码 不是代码呈现的一个效果 
如果想要页面源代码呈现出来源代码运行出来的一个效果就需要把他存到一个文件里面去
先把上面的那一行代码注释掉以后进行接下来的操作
人工智能给出的解释
打开一个名为 "mybaidu.html" 的文件
，以写入模式（mode="w"）打开，同时指定编码格式为 UTF-8。然后，它使用变量 f 来引用打开的文件对象。
在接下来的的一行中，代码调用 f.write() 方法，将 resp.read().decode("utf-8") 
的结果写入到打开的文件对象 f 中。换句话说，这段代码将 resp 对象读取的文本内容以 UTF-8 
编码格式写入到 "mybaidu.html" 文件中。
用大白话来解释
with open{打开并创建一个名为mybaidu的一个html文件 [并把他的模式="w"(mode="w")]
后面跟上他的字符集encoding="utf-8"
并将文件对象f与with open语句中的文件名"mybaidu.html"关联起来
然后用write方法把上一行里面的内容写进去 就会生成一个html文件
"""
# with open("mybaidu.html",mode="w",encoding="utf-8") as f:
#     f.write(resp.read().decode("utf-8"))




