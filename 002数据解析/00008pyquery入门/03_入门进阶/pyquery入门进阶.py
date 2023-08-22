"""首先导入模块"""
from pyquery import PyQuery
""""""
html = """
<HTML>
    <div class="aaa">哒哒哒</div>
    <div class="bbb">嘟嘟嘟</div>
    <div class="zzz">天天天</div>
</HTML>
"""
p = PyQuery(html)
"""
通过PyQuery来改变页面结构
"""
"""
需求
    在上面两个div中间插入一个新的div
首先
    我们先找到属性为aaa的div然后再用.after来在这个div标签后面添加一个xxxx新标签
注意：这个是再标签后面，添加一个标签如果想要再内部添标签请往下面看
"""
p("div.aaa").after("""<div class="ccc">吼吼吼</div>""")
print(p)
"""
需求
    再属性为bbb的内部添加一个标签
首先
    我们要找到这个属性为bbb的div标签
"""
p("div.bbb").append("""<span>我爱你</span>""")     #添加标签
print(p)
"""当然不光可以添加标签还可以改写属性值比如说下面的需求"""
"""
需求
    把div标签里面是aaa属性的那个标签的属性改为bbb来方便管理
理论
    我们可以通过.attr来把里面的属性值给替换掉这个.attr不光可以拿到里面的属性还可以改变里面的属性
实践
    先找到属性为aaa的标签然后用.attr工具把里面的class属性改为bbb
"""
p("div.aaa").attr("class","bbb")    #修改属性
print(p)
print("*"*50)
"""
不光可以修改属性还可以添加属性
需求
    再div标签里面找到属性为zzz的那一个标签然后添加一个id属性
实践
    通过.attr来把里面添加一个属性
"""
p("div.zzz").attr("id","jwrjtz")    #新增属性前提是该标签前提是没有这个属性
print(p)
"""
PyQuery不仅可以添加修改并且还可以删除
attr可以添加属性那么删除的话就用remove_attr来删除
需求
    把刚刚添加的id属性给删除掉
操作
    使用remove_attr想要删除的属性写再后面的括号里面不用写值了只用写一个属性就可以了
"""
print("^"*55)
p("div.zzz").remove_attr("id")  #删除属性
print(p)
"""
如果想要这一整个标签全部都删除掉那么就要用remove来删除整条标签
需求
    把属性为zzz的那一整条标签给删除了
"""
print("="*50)
p("div.zzz").remove()   #删除标签
print(p)
"""
这里面的增删改和字典是一样理论就是语法有点不一样
这个操作什么时候可以用上    也就是再页面代码不够整洁的时候需要把页面代码变得整洁的时候就可以用到
"""


