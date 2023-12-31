"""
HTTP协议
"""
"""
HTTP协议
协议：就是两个计算机之间为了能够流畅的进行沟通而设置的一个君子协定常见的协议有TCP/IP. SOAP协议
HTTP协议，Hype Text Transfer Protocol(超远文本传输协议) 的缩写而是用于万维网
(www.world wide web)服务器传输文本到本地浏览器的传送协议 直白点就是服务器之间的数据交互
遵守的就是HTTP协议

HTTP协议把一条消息分为三大块内容 无论请求还是响应都是三大快内容
请求：
    1. 请求行 -> 请求方式(get/post) 请求url地址 协议
    2. 请求头 -> 放一些服务器要使用附加的信息
 =====================分割线=========================
    3. 请求体 -> 一般放一些请求参数
响应：
    1.状态行 -> 协议状态码
        状态码就是当前的请求处理起开看看到底有没有问题
        可以根据状体码来看请求到底有没有问题
        国际上通用的一些状态码
            200：表示的是没问题 OK
            302：表示的是重定项
            404：基本表示你当前的url是错的服务器虽然收到了，但你当前的url是错的
            500：一般都是服务器里面错了 就是把服务器干崩了
    2.响应头 -> 放一些客户端要使用的附加信息
        响应头里面可能放一些
            cookie,的一些验证信息
            或者是解密的key
        这些都不是固定的有些服务器要加这些有些服务器不加这些
                    主要看服务器
 =====================分割线=========================
    3.响应体 -> 服务器返回真正客户端要用的内容(HTML,JSON)等
        放一些服务器返回给客户端的真数据`   
        如果想要更直观的了解，请看图片"HTTP协议笔记.png"  
"""
"""
请求头中最常见的一些重要内容(爬虫需要)
    1.User-Agent:请求载体的身份标识(用啥发的请求)
    2.Referer:防盗链(这次请求是从那个页面来的? 反爬会用到)
    3.cookie:本地字符串数据信息(用户登录信息，反爬的token   
响应头中一些重要内容
    1.cookie:本地字符串重要信息(用户登录信息，反爬的token)
    2.各种神奇奇妙的字符串(这个需要经验了，一般都是token字样，防止各种攻击和反爬)
请求方式:
    GET: 显示提交    
    POST: 隐示提交
"""






























