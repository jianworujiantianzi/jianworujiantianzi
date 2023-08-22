""""""
"""
第一步安装
第二部导入
from pyquery import PyQuery
"""
from pyquery import PyQuery
"""第三步准备html内容"""
html = """
    <li><a href="http://www.baidu.com">百度</a></li>
"""
"""第四步初始化"""
p = PyQuery(html)
"""
第五步打印   注意这里面有一个坑  就是打印出来的东西很像字符串但是他不是字符串
可以用type来检查一下数据类形可以看到这里面的数据类形是一个PyQuery的一个数据类形   不是想像中的字符串
"""
print(p)
print(type(p))
"""
需求 拿到里面的a标签
pyquery的语法规则
    pyquery对象加括号(这里面写css的选择器)
    比如说想要拿到里面的a就可以用标签选择器来选择它
    操作方法如下
"""
li = p("a")
print(li)
"""
如果代码过多只拿li标签标签里面的a标签就可用下面的方法
我们称这个操作为链式操作后面还可以无限套娃
"""
li_a = p("li")("a")
print(li_a)
"""
或者用后代选择器
    这种更简洁使用方法如下     注意用空格隔开
具体使用方法还要看代码
"""
hou = p("li a")
print(hou)


















