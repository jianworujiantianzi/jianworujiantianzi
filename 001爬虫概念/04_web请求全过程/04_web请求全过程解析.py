
"""
000
"""

"""
001
比如说你搜索百度的网址的时候 你的电脑会发送一个请求到百度的服务器里面
然后百度的服务器会收到一个请求 收到请求的时候百度这面会进行一个相关的数据检索
并把检索的内容拼装成html 拼装好了之后会把拼装好的代码返回到你的电脑当中        响应
你的电脑收到html代码之后会把代码执行一下 就会把页面上的内容给展示出来
"""



"""
002
右键鼠标 查看源代码
、要想搜索的话在源代码里面ctrl加f
"""


"""
003初始反爬
注释001里面的那种类形的爬虫比较好爬取 还有一种不太好爬取的
那种是先返回一个html框架 里面只有结构也就是框架 但是没有内容
然后框架中会带有一些脚本 然后这些脚本会再次请求服务器 进行二次请求
然后服务器会再次组织数据把数据返回过去但是这一次只有数据没有结构
然后浏览器会把数据和结构进行融合然后运行代码呈现给用户
这就是分布式
"""
import pygame

"""
004
003这样的有些拿不到想要的一些数据 这时候就要借助一些工具
推荐一款强大的工具
谷歌浏览器：；里面的
    1.Network(谐音：奶佛我可)
        这里面可以查看到所有的请求 里面所有的请求都再这里面
        点开里面的那么多内容会的第一个   
        再出现一些工具再这里面的工具里面找到Response(谐音:瑞死榜死:响应的意思)
        详细解释请看图片"Network使用.png"
    1.1Response点开之后会把html框架给显现出来但有的没有给数据
如果想要看主要数据的话
    使用XHE请求方法
    详细解释请看图片"XHR请求全过程.png"
           
"""






