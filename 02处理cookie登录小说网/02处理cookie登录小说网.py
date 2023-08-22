""""""
"""
对于某些网站需要登录才能够进行访问这时候我们就需要先登录再访问了主要过程如下
1.登录------>得到cookie
2.带着cookie 去请求拿到书架url-->书架内容

必修要把上面的两个操作连起来
所以我们可以使用session进行请求-->session你可以认为是一连串的请求.再这个过程中cookie不会丢失
session的使用方法    如下
这个session翻译过来叫会话    也就是有来有会的对话 对话的时候会带有上一次对话保留的信息
"""
import requests
session = requests.session()
"""登录模拟登录"""
data = {
    "loginName": "17530859373",
    "password": "zer123.."
}
"""传入登录的时候的url"""
url = "https://passport.17k.com/ck/user/login"
session.post(url,data=data)
"""查看是否登录成功"""
# print(resp.text)
"""查看cookies"""
# print(resp.cookies)

"""因为刚才的那个session中保留的有会然后那个会话里面是有cookies的所以要用session来请求"""
resp = session.get("https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919")
# print(resp.text)
print(resp.json())



"""如果要用get去请求带有密码的要把浏览器里面的那一串cookie放进去放到headers里面"""



