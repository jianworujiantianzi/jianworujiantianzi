import re
s = """
<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='西游记'><span id='10086'>中国移动</span></div>
"""
"""
先预加载 然后在后面直接调用预加载的东西然后后面再放上想要用的功能 最后把参数传进去
\d 还有 .*?外面加上一个括号就是只要这括号里面的数据
正则一旦遇到小括号那么含义就不一样了
"""
obj = re.compile(r"<span id='(\d+)+'>(.*?)</span>")
a = obj.findall(s)
print(a)
"""
如果想要给匹配到的结果起一个名字的话只需要再结果的前面加上?P<要起的名字>  注意:大写
然后结果里面的内容会自动分配到要起的名字里面
然后想要把数据放到这个名字里面用findall的话放不进去要用迭代器通过循环把东西放到里面
所以这时候就要用finditer(迭代器)循环的方式把东西放进去
"""
print("="*50)
obj1 = re.compile(r"<span id='(?P<name1>\d+)+'>(?P<name2>.*?)</span>")
a1 = obj1.finditer(s)
for a2 in a1:
    """
    因为通过迭代器把数据都放到<这里面的名字里了>所以要把<这里面的>名字放到group后面的括号里面去
    操作如下
    """
    an1=a2.group("name1")
    print(an1)
    an2 = a2.group("name2")
    print(an2)

